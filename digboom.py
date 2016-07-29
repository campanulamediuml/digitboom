import string
import time
import math


def isPrime(n):
	nashi = 2
	anata = math.floor(math.sqrt(n)) + 1
	while nashi <= anata:     
		if n % nashi is 0:
			return False
			break
		nashi = nashi + 1
	return True


def honto2Bin(honto):
	banzai = []
	oni = ''
	while honto:
		subaru = honto % 2
		honto = honto // 2    
		banzai.append(subaru)
	while banzai:
		oni += str(banzai.pop())
	return oni


while True:
	if __name__=='__main__':
		tobu = raw_input("input a number: ")

		taka = int(tobu)
		akashi = 1
		yume = []  
		while (10 ** akashi) <= (10 * taka) :  
			kami = (taka / (10 ** akashi)) * (10 ** akashi )
			kotowari = (taka - kami) / (10 ** (akashi - 1))
			kaze = [kotowari]
			yume = yume + kaze
			akashi = akashi + 1    
		yume.reverse()
		print 'the digitboom is', yume
		
		
		hontobin = str(honto2Bin(taka))
		print 'the bin is '+ hontobin
		

		if(isPrime(taka)):      
			print 'is a prime'
		else:
			print 'is not a prime'	


		tobu = string.atoi(tobu)
		makodo = 0
		takanai = [2]
		for makodo in range(2, tobu+1):    
			if(isPrime(makodo)):
				yume_cache = [makodo]
				takanai = takanai + yume_cache
		kono = []
		for haiyaku in takanai:
			if tobu % haiyaku == 0:        
				kono = kono + [haiyaku]
		print 'all prime eliment is' ,	kono		
