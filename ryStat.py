# ryStat.py
# Author: Ryan Kramlich
# Last Edit: 09/08/13

import math, sys

manual = '''
ryStat is for education purposes. Please don't use it to cheat on your homework.
You totally could though.

HOW TO USE
	python ryStat.py -option data(different for each option, see below)

OPTIONS (num = number)
	-mean 'num num...num'
	-median 'num num...num'
	-variance 'num num...num'
	-sd 'num num...num'
	-trimmedmean 'num num...num' percent
	-stemandleaf 'num num...num'
'''

def main():
	check_args()
	choose_option(sys.argv[1])

def check_args():
	option_array = ['-mean','-median','-variance','-sd','trimmedmean','-stemandleaf']

	if len(sys.argv) == 1:
		print (manual)
	if len(sys.argv) > 1:
		if sys.argv[1] not in option_array:
			print (manual)

def choose_option(option):
	if option == '-mean':
		arr = destring(sys.argv[2])
		mean(True, arr)

	if option == '-median':
		arr = destring(sys.argv[2])
		median(True, arr)

	if option == '-variance':
		arr = destring(sys.argv[2])
		var_and_sd(True, arr)

	if option == '-sd':
		arr = destring(sys.argv[2])
		var_and_sd(True, arr)

	if option == '-trimmedmean':
		arr = destring(sys.argv[2])
		trimmed_mean(True, arr, sys.argv[3])

	if option == '-stemandleaf':
		arr = destring(sys.argv[2])
		stem_and_leaf(True, arr)

def destring(string):
	string = string.replace('[','')
	string = string.replace(']','')
	string = string.replace(',',' ')
	string = string.split(' ')
	for i in range(len(string)):
		if '.' in string[i]:
			string[i] = float(string[i])
		else:
			string[i] = int(string[i])
	return string

################### STAT FUNCTIONS #####################

def mean(show, num_list):
	list_length = len(num_list)
	sum = 0
	sum_equation = ''
	for i in range(list_length):
		sum_equation += (str(num_list[i]) + ' + ')
		sum = sum + num_list[i]
	sum_equation = sum_equation[:-2]
	sum_equation += ('= ' + str(sum))
	mean = sum / float(list_length)
	if show:
		print 'length n = ' + str(list_length)
		print sum_equation
		print str(sum) + '/' + str(list_length) + ' = ' + str(mean)
	return mean

def median(show, num_list):
	num_list = sorted(num_list)
	list_length = len(num_list)
	median = 0
	left = 0
	right = 0
	if(list_length % 2 == 0):
		left = num_list[(list_length / 2) - 1]
		right = num_list[list_length / 2]
		median = (left + right) / float(2)
	else:
		median = num_list[list_length / 2]
	if show:
		print 'Sorted list: ' +  str(sorted(num_list))
		if list_length % 2 == 0:
			print 'The length is even. We must take the average of the middle 2 values.'
			print '(' + str(left) + ' + ' + str(right) + ') / 2 = ' + str(median)
		else:
			print 'The length is odd. Take the middle value.'
			print median
	return median

def var_and_sd(show, num_list):
	list_length = len(num_list)
	mn = mean(False, num_list)
	numerator = 0
	if show:
		print 'xi | xi-xbar | (xi-xbar)^2'
		print '--------------------------'
	for i in range(list_length):
		xi = num_list[i]
		xi_minus = xi - mn
		xi_minus_squared = math.pow(xi_minus, 2)
		if show:
			print str(xi) + '    ' + str('%.2f' % xi_minus) + '     ' + str('%.2f' % xi_minus_squared)
		numerator += xi_minus_squared
	variance = numerator / float(list_length - 1)
	sd = math.sqrt(variance)
	if show:
		print '--------------------------'
		print '               sum = ' + str('%.2f' % numerator)
		print '               variance = ' + str('%.2f' % numerator) + '/' + str(list_length - 1) + ' = ' + str('%.2f' % variance) 
		print 'The square root of ' + str('%.2f' % variance) + ' = standard deviation = ' + str('%.2f' % sd)
	return[variance, sd]

# It was at this point that I realized I had just eaten an entire bear bottle of honey.

def trimmed_mean(show, num_list, percent):
	percent = percent / float(100)
	num_list = sorted(num_list)
	trimming = int(percent * len(num_list))
	for i in range(trimming):
		del num_list[len(num_list) - 1]
		del num_list[0]
	if show:
		print '[Steps under construction]'
		print mean(False, num_list)
	return mean(False, num_list)

def stem_and_leaf(show, num_list):
	if isinstance(num_list[0], float):
		for i in range(len(num_list)):
			num_list[i] = int(num_list[i] * 10)
	stem_leaf = ''
	num_list = sorted(num_list)
	min_stem = min(num_list)/10
	max_stem = max(num_list)/10
	for i in range(min_stem, max_stem + 1):
		if len(str(i)) == 1:
			stem_leaf += ' '
		stem_leaf += (str(i) + '|')
		try:
			while num_list[0] / 10 == i:
				stem_leaf += str(num_list[0] % 10) + ' '
				del num_list[0]
			stem_leaf += '\n'
		except IndexError:
			pass
	if show:
		print stem_leaf
	return stem_leaf

# FUNCTIONS UNDER CONSTRUCTION

def boxplot(show, num_list):
	pass

def histogram(show, num_list):
	pass

def probability():
	pass

if __name__ == '__main__':
	main()
