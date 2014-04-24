# Enter your answers for chapter 6 here
# Name: Cait

print 'Ex. 6.6'

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]		

#print middle('as')
#print middle('i')
#print middle('')
#print middle('racecar')

'''
1. If we call print middle('as'), then the function returns 
an empty string. A 'middle' of the word does not exist.

print middle('i') and print middle('') also return empty strings 
''' 

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False		
	return is_palindrome(middle(word))
	
print is_palindrome('racecar') #palindrome		
print is_palindrome('racooncar') #not a palindrome
print is_palindrome('a') #fits the <= 1 base case on first 'loop'
print ''

print 'Ex 6.8'

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b,r)

print gcd(60, 24)
