# def isLeapYear(year):
# 	result = False
# 	if year % 4 == 0:
# 		if year % 100 == 0: # common year
# 			if year % 400 == 0:
# 				# daysOfMonths[1] = 29 # leap year
# 				result = True
# 		else:
# 			# daysOfMonths[1] = 29 #leap year
# 			result = True
# 	return result #common year

# def daysOfMonths(result):
# 	daysOfMonths1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	print daysOfMonths1
# 	if result == True:
# 		daysOfMonths1[1] = 29
# 	else:
# 		daysOfMonths1[1] = 28
# 	return daysOfMonths1


# Days Alive

# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def isLeapYear(year):

# 	if year % 4 == 0:
# 		if year % 100 == 0:
# 			if year % 400 == 0:
# 				daysOfMonths[1] = 29
# 				return True
# 			else:
# 				# daysOfMonths[1] = 28
# 				return False
# 		else:
# 			daysOfMonths[1] = 29
# 			return True
# 	else:
# 		# daysOfMonths[1] = 28
# 		return False

def isLeapYear(year):
	result = False
	if year % 4 == 0:
		if year % 100 == 0: # common year
			if year % 400 == 0:
				result = True
		else:
			result = True
	return result #common year

# def daysInMiddleYears(y1, y2):
# 	# yearsBetween = range (y1 + 1, y2 - 1)
# 	i = y1 + 1
# 	daysBetween = 0
# 	while i < y2:
# 	# for e in yearsBetween:
# 		if isLeapYear(i) == True:
# 			daysBetween += 366
# 			i += 1
# 		else:
# 			daysBetween += 365
# 			i += 1
# 	print daysBetween
# 	return daysBetween
	
# def daysInStartYear(y1, m1, d1):
# 	daysStart = daysOfMonths[m1 - 1] - d1
# 	i = m1
# 	while i < 11:
# 		daysStart += daysOfMonths[i] # need to factor in leap or common
# 		i += 1
# 	print daysStart
# 	return daysStart

# def daysInEndYear(y2, m2, d2):
# 	daysEnd = d2
# 	i = 0
# 	while i < m2 - 1:
# 		daysEnd += daysOfMonths[i]
# 	print daysEnd
# 	return daysEnd

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def diffrentiateDaysofMonths(year):
	
	# print 'Flerp: ', daysOfMonths1
	if isLeapYear(year):
		daysOfMonths[1] = 29
	return daysOfMonths

def daysBetweenDates(y1, m1, d1, y2, m2, d2):

# days in year 1

	days = daysOfMonths[m1 - 1] - d1
	# print 'days at end of first month: ', days # works!
	i = m1
	while i < 12:
		diffrentiateDaysofMonths(y1)
		days += daysOfMonths[i]
		i += 1
		# print 'monthly day increment', i, days # works!

	print 'days in first year: ', days #works!

# days in years between

	i = y1 + 1
	while i < y2:
	# for e in yearsBetween:
		if isLeapYear(i) == True:
			days += 366
			print 'middle year increment: ', i, days
			i += 1
		else:
			days += 365
			print 'middle year increment: ', i, days
			i += 1

	print 'days up to last year: ', days # works !

# days in last year

	i = 0
	while i < m2 - 1:
		diffrentiateDaysofMonths(y2)
		days += daysOfMonths[i]
		# print 'increment days of month last year: ', y2, i, days # works !
		i += 1
	days += d2

	# print days
	return days


# print '1601, 1, 1, 2017, 4, 25', daysBetweenDates(1601, 1, 1, 2017, 4, 25)

print '1556, 6, 12, 2016, 4, 25', daysBetweenDates(1556, 6, 12, 2016, 4, 25)
	#days by end of year = 202
	#days in years between = 167636 >> 167838
	#days in end year = 
	#>>> 167954

print '1000, 10, 30, 2000, 3, 20', daysBetweenDates(1000, 10, 30, 2000, 3, 20)



# print 'True! ', isLeapYear(2016), daysOfMonths

# print 'False :( ', isLeapYear(2015), daysOfMonths

# print 'True! ', isLeapYear(1600), daysOfMonths

# print 'False :( ', isLeapYear(1700), daysOfMonths

#find out why these are all returning days of the month wrong!