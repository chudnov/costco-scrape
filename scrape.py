from bs4 import BeautifulSoup, NavigableString #extract the html from the request
from selenium import webdriver #deal with the dynamic javascript
from multiprocessing import Process
import csv

#URLs of the specific products
URLS = []

#Load the path of the driver for use
def load_driver_path():
    path_file = open('DriverPath.txt', 'r')
    path = path_file.read().strip()
    path_file.close()
    return path

#Loads all the urls from the URLS.txt file and appends them to the array of urls
def load_urls_from_text_file():
    urls_file = open('URLS.txt', 'r')
    urls = urls_file.readlines()
    for url in urls:
        URLS.append(url.strip())
    urls_file.close()

#Establish the webdriver
def link_driver(path_to_driver):
    #Establish the driver
    driver = webdriver.Chrome(path_to_driver)
    return driver

#  1. Loads the html data
#  2. Turns it into soup
def load_data(webdriver):
    for url in URLS:
        #Get the contents of the URL
        webdriver.get(url)

        #returns the inner HTML as a string
        innerHTML = webdriver.page_source

        #turns the html into an object to use with BeautifulSoup library
        soup = BeautifulSoup(innerHTML, "html.parser")

        extract_and_load_all_data(soup)

#closes the driver
def quit_driver(webdriver):
    webdriver.close()
    webdriver.quit()

## Now need to get the following from the page:
#    1. seo meta tags
#    2. product name
#    3. product description
#    4. product specifications
#    5. category
#    6. price
#    7. embedded images

# gets the seo meta tags
def get_meta_tags(soup):
    meta_tags = [tags.get('name') + " is " + tags.get('content') for tags in soup.find_all('meta')[3:8]]
    return meta_tags

# gets the product name
def get_product_name(soup):
    product_name = soup.find('meta', property="og:description").get('content')
    return product_name

# logic for getting product description/specification
def get_product_info(types, soup):
    if types == "description":
        tags = soup.find('div', class_ = "product-info-description").descendants
    elif types == "specification":
        tags = soup.find('div', id = "pdp-accordion-collapse-2").descendants
    else:
        return "Wrong String!"

    data = ""

    for tag in tags:
        if type(tag) is NavigableString and tag.string is not None:
            if(types == "description"):
                data += tag.string + "\n"
            else:
                data += tag.string
        else:
            continue

    return "\"" + data.replace("\"", "\"\"") + "\""

# gets the product description
def get_product_description(soup):
    return get_product_info("description", soup)

# gets the product specifications
def get_product_specification(soup):
    return get_product_info("specification", soup)

# gets the product category
def get_category(soup):
    tags = soup.find('ul', id = "crumbs_ul")
    data = tags.contents[-2].text

    return '\n'.join([x for x in data.split("\n") if x.strip()!=''])

# gets the product price
def get_price(soup):
    tag = soup.find('span', class_ = "op-value")
    return tag.text

# gets the product image
def get_embedded_images(soup):
    tag = soup.find('img', id = "productImage")
    return tag['src']

# Load data to csv
def extract_and_load_all_data(soup):
    field_names = ["Meta tags", "Name", "Description", "Specifications", "Category", "Price", "Image"]
    output_data = open('OutputData.csv', 'a')

    writer = csv.DictWriter(output_data, field_names,
        delimiter='\n')#,
        #dialect='excel',
        #lineterminator="\r\n")

    writer.writerow({field: field for field in field_names})

    collected_data = [
        {
            "Meta tags": get_meta_tags(soup),
            "Name": get_product_name(soup),
            "Description": get_product_description(soup),
            "Specifications": get_product_specification(soup),
            "Category": get_category(soup),
            "Price": get_price(soup),
            "Image": get_embedded_images(soup)
        }
    ]

    for item_property_dict in collected_data:
        writer.writerow(item_property_dict)

    output_data.close()

#  1. Links the driver
#  2. Loads the html data
#  3. Turns it into soup
#  4. extracts correct elements and loads it to csv file
def run():
    load_urls_from_text_file()
    path = load_driver_path()
    driver = link_driver(path)
    load_data(driver)
    quit_driver(driver)

def main():
    #create multiple threads for selenium web scraping - ASYNC
    processes = []
    p = Process(target=run, args=())
    processes.append(p)
    p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
