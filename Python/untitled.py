def isLeapYear(year):
	result = False
	if year % 4 == 0:
		if year % 100 == 0: # common year
			if year % 400 == 0:
				result = True
		else:
			result = True
	return result #common year

def diffrentiateDaysofMonths(year):
	daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# print 'Flerp: ', daysOfMonths1
	if isLeapYear(year):
		daysOfMonths[1] = 29
	return daysOfMonths



print 'True! ', diffrentiateDaysofMonths(2016)

print 'False :( ', diffrentiateDaysofMonths(2015)

print 'True! ', diffrentiateDaysofMonths(1600)

print 'False :( ', diffrentiateDaysofMonths(1700)