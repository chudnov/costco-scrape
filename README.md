# Costco Scrape

This web scrape utilizes the BeautifulSoup and Selenium Webdriver libraries to fetch the following data from a Costco product page and load it into a CSV file:
- SEO Meta Tags
- Product Name
- Product Description
- Product Specifications
- Category
- Price
- Embedded images

This script ONLY works for the **Costco** website. It will break for any other website. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. 

### Prerequisites:
- [Python 3.7.0](https://www.python.org/downloads/windows/) 

  Once Python 3.7 is installed:

  - [Webdriver](http://selenium-python.readthedocs.io/installation.html). Please install the **Chrome** version!
    ###### (Copy the path of the installed webdriver! You will need it in set up!)

  - Selenium: 
  
    `C:\Python37\Scripts\pip install selenium`

  - BeautifulSoup: 
  
    `C:\Python37\Scripts\pip install beautifulsoup4`

### Set Up:
1. In the **DriverPath.txt** file, paste the path of the webdriver you installed above
2. If you installed a driver other than **Chrome**, open **Scrape.py** and do the following:
   
   On line 27, by default there is `driver = webdriver.Chrome(path_to_driver)`
   - For **Firefox**: `driver = webdriver.Firefox(path_to_driver)`
   - For **Safari**:  `driver = webdriver.Safari(path_to_driver)`

### Running:
For every iteration of scraping:
  1. In the **URLS.txt** file, delete all the current urls there
  2. Paste **10** new urls, each on its own line, without quotation lines
  3. On the command line, go into the directory of this github repository and run:
  
     `python scrape.py`
  
  4. Open the **OutputData.csv** file and voila, all the data is loaded!
  
  5. Congratulations!
  
### Authors:
- CHUDDY
