from myclass import *
import mysql.connector
from mysql.connector import errorcode
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#Set up server connection
try:
	cnn = mysql.connector.connect(user='james', password = 'zibiaoking', host = '104.236.182.109',database='DBBook')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

def main():
	#list of books to be searched
	#print menu
	option = print_menu()
	#while user does not choose exit
	while(option != 0):
		switch = {0:1, 1:opt1, 2:opt2, 3:opt3}
		#execute corresponding choice
		switch[option]()
		option = print_menu()
	return

def opt1():
	isbn = input('Enter book isbn: ')
	global cnn 
	cursor = cnn.cursor()
	#find isbn id from book
	query = ("SELECT book_id from Book WHERE book_isbn = %s")
	cursor.execute(query, (isbn,))
	row = cursor.fetchone()
	if(not row):
		print "That book is not in the database. \n", \
		"Please run DataScraper to get the book info.\n"
		return
	book_id = row[0]
	#find all price and dates(date stamp) from book_id
	query = ("SELECT price, date_price from Book_Detail WHERE book_id = %s ORDER by book_id ASC")
	cursor.execute(query, (book_id,))
	#each row contains book's price and the datestamp
	row = cursor.fetchall()
	#x and y for plotting, x is date y is price
	y = []
	x = []
	for (price, d) in row:
		#print type(price) is <type 'float'>
		#print type(d) is <type 'datetime.datetime'>
		y.append(price)
		#need help in here
		x.append(d.date())

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.plot(x,y)
	plt.gcf().autofmt_xdate()
	plt.show()
	return
def opt2():
	x=5
	return
def opt3():
	y=3
	return
def print_menu():
	print "\n Menu"
	print "0. Exit"
	print "1. Plot book price vs date"
	option = input('Select: ');
	return option

if __name__ == "__main__":
	main()
