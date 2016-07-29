import string
import time
import math


def isPrime(n):
	count = 2
	large = math.floor(math.sqrt(n)) + 1
	while count <= large:     
		if n % count is 0:
			return False
			break
		count = count + 1
	return True


def Dec2Bin(dec):
	temp = []
	result = ''
	while dec:
		quo = dec % 2
		dec = dec // 2    
		temp.append(quo)
	while temp:
		result += str(temp.pop())
	return result


while True:
	if __name__=='__main__':
		inbox = raw_input("input a number: ")

		box = int(inbox)
		log = 1
		tab = []  
		while (10 ** log) <= (10 * box) :  
			tencount = (box / (10 ** log)) * (10 ** log )
			tappon = (box - tencount) / (10 ** (log - 1))
			taptab = [tappon]
			tab = tab + taptab
			log = log + 1    
		tab.reverse()
		print 'the digitboom is', tab
		
		
		decbin = str(Dec2Bin(box))
		print 'the bin is '+ decbin
		

		if(isPrime(box)):      
			print 'is a prime'
		else:
			print 'is not a prime'	


		inbox = string.atoi(inbox)
		makodo = 0
		primetab = [2]
		for makodo in range(2, inbox+1):    
			if(isPrime(makodo)):
				tab_cache = [makodo]
				primetab = primetab + tab_cache
		prel = []
		for element in primetab:
			if inbox % element == 0:        
				prel = prel + [element]
		print 'all prime eliment is' ,	prel		
