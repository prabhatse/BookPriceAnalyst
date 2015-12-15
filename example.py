from selenium import webdriver
from bs4 import BeautifulSoup
#example of finding the price of a book
driver=webdriver.PhantomJS(executable_path='/Users/jameszheng/GitProj/BookPriceAnalyst/phantomjs');
driver.get('http://bookscouter.com/prices.php?isbn=9780132139311&searchbutton=Sell');
html = driver.page_source;
soup = BeautifulSoup(html, "html.parser")

mydivs = soup.findAll("div", class_="offer")
print driver.current_url
companyDiv = mydivs[0].findAll("div", class_="column-1")
priceDiv = mydivs[0].findAll("div", class_="column-6")
#extract the string
company = str(companyDiv[0].text).strip()
price = str(priceDiv[0].findAll("div", class_="book-price-normal")[0].text).strip()
#remove dollar sign
price = float(price[1:])
print company
print price
