from bs4 import BeautifulSoup
from myclass import *
import mysql.connector
import datetime
from mysql.connector import errorcode

#Set up server connection
try:
  cnn = mysql.connector.connect(user='james', password = 'zibiaoking', host = '104.236.182.109',
                                database='DBBook')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

HM = {}
allBooks = []
def main():
	#list of books to be searched
	#print menu
	hi = Book(1231231231231)
	option = print_menu()
	#while user does not choose exit
	while(option != 0):
		switch = {0:1, 11:opt11, 22:opt22, 1:opt1, 2:opt2, 3:opt3, 4:opt4}
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
#Update information into database
def opt22():
	global allBooks
	global cnn

	for b in allBooks:
		if b.store and not b.inDB:
			store = str(b.store[0])
			price = str(b.price[0])
			isbn = str(b.isbn)
			title = str(b.title)
			cursor = cnn.cursor()
			#Check if book is already in DB
			query = ("SELECT book_id from Book WHERE book_isbn = %s")
			cursor.execute(query, (isbn,))
			row = cursor.fetchone()
			#if not in database then add it
			if not row:
				query = ("INSERT INTO Book (book_isbn, book_title)"
					"VALUES (%s, %s)")
				cursor.execute(query, (isbn, title))
				print "Added isbn: {0} title: {1} to DB:Book" .format(isbn, title)
				query = ("SELECT book_id from Book WHERE book_isbn = %s");
				cursor.execute(query, (isbn,))
				row = cursor.fetchone()

			book_fkey = row[0]

			#Check if company is already in DB

			query = ("SELECT store_id from Store WHERE store_name = %s")
			cursor.execute(query, (store,))
			row = cursor.fetchone()
			#if not in database then add it

			if not row:
				query = ("INSERT INTO Store (store_name)"
					"VALUES (%s)")
				cursor.execute(query, (store,))
				print "Added store {0}" .format(store)
				query = ("SELECT store_id from Store WHERE store_name = %s")
				cursor.execute(query, (store,))
				row = cursor.fetchone()
			store_fkey = row[0]

			query = ("INSERT INTO Book_Detail ( book_id, store_id, price) VALUES"
				"(%s,%s,%s)")
			cursor.execute(query, (book_fkey, store_fkey, price));
			#insert book information

			#book has been updated
			b.inDB = True
			cnn.commit()

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
	print "22. Update all information into database"
	print "1. Add isbn"
	print "2. Remove isbn"
	print "3. Status"
	print "4. Update book price"
	print "0. Exit"
	option = input('Select: ');
	return option


if __name__ == "__main__":
	main()