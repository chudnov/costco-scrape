from bs4 import BeautifulSoup, NavigableString #extract the html from the request
from selenium import webdriver #deal with the dynamic javascript

###VARIABLES TO CHANGE####

#URL of the specific product
URL = "https://www.costco.com/Oakley-OO9265-Latch-Matte-Gray-Polarized-Sunglasses.product.100406867.html"

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

#The soup
soup = link_driver_and_make_soup(PATH_TO_DRIVER, URL)

## Now need to get the following from the page:
#    1. seo meta tags FINISHED
#    2. product name FINISHED
#    3. product description FINISHED
#    4. product specifications
#    5. category
#    6. price
#    7. embedded images


def get_meta_tags():
    meta_tags = [tags.get('name') + " is " + tags.get('content') for tags in soup.find_all('meta')[3:8]]
    return meta_tags


def get_product_name():
    product_name = soup.find('meta', property="og:description").get('content')
    return product_name


def get_product_description():
    tags = list(soup.find('div', class_ = "product-info-description").descendants)
    description = ""

    for tag in tags:
        if type(tag) is NavigableString:
            if tag.string is not None:
                description += tag.string + "\n"
        else:
            continue

    return description

'''
def get_category():
    ##

def get_price():
    ##

def get_embedded_images():
    ##
'''
