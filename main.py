from selenium import webdriver
from bs4 import BeautifulSoup
class Book:
	driver=webdriver.PhantomJS(executable_path='/Users/jameszheng/GitProj/BookPriceAnalyst/phantomjs');
	Map = {}
	def __init__(self, isbn):
		self.isbn = isbn
		self.title = ""
		self.price = []
		self.date = []
		self.store = []

	def set_name(self, name):
		self.name = name

		return
	def find_price(self):
		url = "http://bookscouter.com/prices.php?isbn=" + str(self.isbn) + "&searchbutton=Sell";
		Book.driver.get(url);
		print Book.driver.current_url
		if Book.driver.current_url == "http://bookscouter.com/?badisbn":
			print 'The isbn %d is not valid. Stopped price search.' %self.isbn
			return

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


'''
mydivs = soup.findAll("div", class_="offer")
print driver.current_url
'''
HM = {}
allBooks = []
def main():
	#list of books to be searched
	#print menu
	option = print_menu()
	#while user does not choose exit
	while(option != 0):
		switch = {0:1, 11:opt11, 1:opt1, 2:opt2, 3:opt3, 4:opt4}
		#execute corresponding choice
		switch[option]()
		option = print_menu()
		
	return
#############
def opt11():
	global allBooks
	global HM
	with open("isbn.txt", "r") as file:
		for line in file:
			line = int(line)
			if not (line in HM):
				allBooks.append(Book(line))
				HM[line] = 1
				print 'Added %d' % line
		print "length of allBooks is %d" %len(allBooks)
	return

#############
# add new book
#############
def opt1():
	#center piece
	global allBooks
	global HM
	isbn = input('Add book isbn: ')
	while(len(str(isbn)) != 13):
		print "Error isbn must be 13 digits"
		isbn = input('Add book isbn: ')
	if not isbn in HM:
		allBooks.append(Book(isbn))
		print 'Added %d' % isbn
	return

#remove book
def opt2():
	global allBooks
	global HM
	isbn = input('Remove book isbn: ')
	while(len(str(isbn)) != 13):
		print "Error isbn must be 13 digits"
		isbn = input('Remove book isbn: ')
	if isbn in HM:
	#remove the object	
		for b in allBooks:
			if(b.isbn == isbn):
				allBooks.remove(b)
	#remove the key from hashmap
		HM.pop(isbn)
	return

#print book status
def opt3():
	global allBooks
	print "Books:"
	print "length of allBooks is %d" %len(allBooks)
	for b in allBooks:
		#print isbn,title,price,company
		if not b.price:
			price = "N"
			title = "N"
			store = "N"
			print '{0:16} {1:6} {2:15} {3:25}' .format(b.isbn, price, store, title)
		else:
			print '{0:16} {1:6} {2:15} {3:25}' .format(b.isbn, b.price[0], b.store[0], b.title)
	return

def opt4():
	global allBooks
	for b in allBooks:
		#search the web for prices
		b.find_price()
		print "Finished searching"


	
'''

driver.get('http://bookscouter.com/prices.php?isbn=978013239311&searchbutton=Sell');
html = driver.page_source;
soup = BeautifulSoup(html, "html.parser")

mydivs = soup.findAll("div", class_="offer")
print driver.current_url
#nth highest price
n = 3
for i in range(1,n):
	divTitle = mydivs[i].findAll("div", class_="column-1")
	print divTitle
	print divTitle[0].text;
'''
def print_menu():
	print "\nPlease select an option:"
	print "11. Add isbn from file isbn.txt"
	print "1. Add isbn"
	print "2. Remove isbn"
	print "3. Status"
	print "4. Update book price"
	print "0. Exit"
	option = input('Select: ');
	return option


if __name__ == "__main__":
	main()