import datetime as dtmodule
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main():


	#x and y for plotting, x is date y is price
	y = []
	x= []
	y.append(50.5)
	y.append(60)
	y.append(30)
	y.append(20)
	y.append(10.5)
	#there are the x values return from my database, it is in datetime object
	#datetime(year,month,date,hour,minute,second)
	x.append(dtmodule.datetime(2015,12,22,11,30,59))
	x.append(dtmodule.datetime(2015,12,23,11,23,23))
	x.append(dtmodule.datetime(2015,12,24,11,23,23))
	x.append(dtmodule.datetime(2015,12,25,11,23,23))
	x.append(dtmodule.datetime(2015,12,26,11,23,23))
	
	#use the above to plot x and y where x is the date not time
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	newx = []
	for d in x:
		#dates = str(d.month) + '/' + str(d.day) +'/' + str(d.year);
		
		newx.append(d.date())

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.plot(x,y)
	plt.gcf().autofmt_xdate()
	plt.show()
	return


if __name__ == "__main__":
	main()
