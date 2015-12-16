import mysql.connector
import datetime
from mysql.connector import errorcode

try:
  cnn = mysql.connector.connect(user='nothing', password = 'nothing', host = '123',
                                database='DBBook')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnn.cursor()
#Check if book is already in DB
isbn = 978047119
title = 'Calculus of biology'
store = 'ipwoman'
price = 1.54
'''query = ("SELECT * FROM Store;")
cursor.execute(query)
for (pid, store_name) in cursor:
  print("{}, {}".format(
    pid, store_name))
'''
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

cnn.commit()
