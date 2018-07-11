from bs4 import BeautifulSoup #extract the html from the request
from selenium import webdriver #deal with the dynamic javascript

###VARIABLES TO CHANGE####

#URL of the specific product
URL = "https://www.costco.com/Westport-Beautyrest-Fabric-Sleeper-Loveseat.product.100325179.html"

#Path to the driver
PATH_TO_DRIVER = '/Users/jacobchudnovsky/Downloads/chromedriver'

##########################

#Establish the driver
driver = webdriver.Chrome(PATH_TO_DRIVER)

#Get the contents of the URL
driver.get(URL)

#returns the inner HTML as a string
# innerHTML = driver.execute_script("return document.body.innerHTML")
innerHTML = driver.page_source

#closes the driver
driver.close()

#turns the html into an object to use with BeautifulSoup library
soup = BeautifulSoup(innerHTML, "html.parser")

## Now need to get the following from the page:
#    1. seo meta tags
#    2. product name
#    3. product description
#    4. category
#    5. price
#    6. embedded images


def get_meta_tags():
    for tags in soup.find_all('meta')[3:8]:
        print(tags.get('name') + " is " + tags.get('content'))

'''
def get_product_name():
    ##

def get_product_description():
    ##

def get_category():
    ##

def get_price():
    ##

def get_embedded_images():
    ##
'''
