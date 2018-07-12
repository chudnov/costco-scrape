from bs4 import BeautifulSoup, NavigableString #extract the html from the request
from selenium import webdriver #deal with the dynamic javascript

###VARIABLES TO CHANGE####

#URLs of the specific products
URLS = [
"https://www.costco.com/Japanese-Wagyu-New-York-Strip-Loin-Roast%2c-A-5-Grade%2c-13-lbs.product.100311362.html",
"https://www.costco.com/Oakley-OO9265-Latch-Matte-Gray-Polarized-Sunglasses.product.100406867.html",
"https://www.costco.com/ECOS-Laundry-Detergent-Free-%2526-Clear-210-fl.-oz%2c-2-count.product.100347717.html"
]

#Path to the driver
PATH_TO_DRIVER = '/Users/jacobchudnovsky/Downloads/chromedriver'

##########################

def link_driver_and_make_soup(path_to_driver, url):
    #Establish the driver
    driver = webdriver.Chrome(path_to_driver)

    #Get the contents of the URL
    driver.get(url)

    #returns the inner HTML as a string
    # innerHTML = driver.execute_script("return document.body.innerHTML")
    innerHTML = driver.page_source

    #closes the driver
    driver.close()

    #turns the html into an object to use with BeautifulSoup library
    soup = BeautifulSoup(innerHTML, "html.parser")

    return soup

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
def get_product_info(types):
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

    return data

# gets the product description
def get_product_description(soup):
    return get_product_info("description")

# gets the product specifications
def get_product_specification(soup):
    return get_product_info("specification")

# gets the product category
def get_category(soup):
    tags = soup.find('ul', id = "crumbs_ul")
    return tags.contents[-2].text

# gets the product price
def get_price(soup):
    tag = soup.find('span', class_ = "op-value")
    return tag.text

# gets the product image
def get_embedded_images(soup):
    tag = soup.find('img', id = "productImage")
    return tag['src']


# LOAD ALL DATA TO CSV
def extract_and_load_all_data():
    for url in URLS:
        #The HTML to interact with
        soup = link_driver_and_make_soup(PATH_TO_DRIVER, url)
        # get_meta_tags(soup)
        # get_product_name(soup)
        # get_product_description(soup)
        # get_product_specification(soup)
        # get_category(soup)
        # get_price(soup)
        # get_embedded_images(soup)

extract_and_load_all_data()
