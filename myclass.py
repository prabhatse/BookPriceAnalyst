from selenium import webdriver
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

		#make sure page loaded before moving on
		#wait 1 sec and try again if page not loaded
		soup.find("div", {"id": "faux-featBox"})
		while(not soup.find("div", {"id": "faux-featBox"})):
			time.sleep(5)
			print "Sleep 5 sec let until page load."
			#get entire source code
			html = Book.driver.page_source;
			#parse them nicely
			soup = BeautifulSoup(html, "html.parser")

		#see if there already a title if not then find title of book and add it
		if not self.title:
			mydivs = soup.findAll("div", class_="search-result")
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
