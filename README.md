# BookPriceAnalyst
Purpose:

This program will search for the highest offer 
for used textbooks from 45 book companies.
The purpose is to help analyze and predict the price of future
prices and to make a profit from investing in used books.

Requirements:

Python 2.7 or higher

Modules:

Selenium, helps data scraping information from websites
PhantomJS, hides the browser triggered by Selenium which speeds up
	the data scraping process because it avoid all the css rendering
BeautifulSoup, helps organize and parse the html source 
mysql.connector, helps interact with mysql database

BEWARE: PhantomJS takes 30 minutes to compile, therefore
	just use the binary executable in the same directory 
	and include to use it

Instructions:
	The program will only accept 13 digits isbn.
	You can add it to a list and run the program to
		find the prices.
	If you want to record the data for future analysis you must
		set up a database.

python DataScraper.py
