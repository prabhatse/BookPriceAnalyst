from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import time
class Book:
	driver=webdriver.PhantomJS(executable_path='/Users/jameszheng/GitProj/BookPriceAnalyst/phantomjs');
	#driver = webdriver.Firefox()

	def __init__(self, isbn):
		self.isbn = isbn
		self.title = ""
		self.price = []
		self.date = []
		self.store = []
		self.inDB = False

	def set_name(self, name):
		self.name = name

		return
	def find_price(self):
		url = "http://bookscouter.com/prices.php?isbn=" + str(self.isbn) + "&searchbutton=Sell";
		Book.driver.get(url);
		#Book.driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
		print Book.driver.current_url
		if Book.driver.current_url == "http://bookscouter.com/?badisbn":
			print 'The isbn %d is not valid. Stopped price search.' %self.isbn
			return
		#get entire source code
		html = Book.driver.page_source;
		#parse them nicely
		soup = BeautifulSoup(html, "html.parser")
		#allow time to load page or else throw exception
		problem = False
		try:
			element = WebDriverWait(Book.driver, 15).until(
        		expected_conditions.presence_of_element_located((By.ID, "faux-featBox")))
		except:
			problem = True
			pass
		if problem == True:
			print "Timed out no result for this one."
			return
		#get entire source code
		html = Book.driver.page_source;
		#parse them nicely
		soup = BeautifulSoup(html, "html.parser")

		#see if there already a title if not then find title of book and add it
		if not self.title:
			mydivs = soup.findAll("div", class_="search-result")
			if not mydivs:
				return
			self.title = str(mydivs[0].findAll("h1")[0].text).strip()
		
		#extract the list of offer divs
		mydivs = soup.findAll("div", class_="offer")
		#extract two columns which contain company name and price
		companyDiv = mydivs[0].findAll("div", class_="column-1")
		priceDiv = mydivs[0].findAll("div", class_="column-6")
		#extract them into string format
		company = str(companyDiv[0].text).strip()
		price = str(priceDiv[0].findAll("div", class_="book-price-normal")[0].text).strip()
		#remove dollar sign and turn price into a float
		price = float(price[1:])

		#update propertie values
		self.store.append(company)
		self.price.append(price)
		return
