import time
# ======================================
#  Function: Check if a number is prime
# ======================================
def checkPrime(number,prime_list):
    p_plus = list()
    for p in prime_list:
        if(number % p == 0): # Not prime
            return False
        p_plus.append(number/p)
        if(p > p_plus[-1]):
            prime_list.append(number)
            return True
# --------------------------------------
# Program starts here
# --------------------------------------
PrimeList = [2] # PrimeList starts from 2
size = input('Enter range for PrimeFinder: ')
if (size.isdigit()):
    start = time.time()
    for i in range(2,int(size)):            
        checkPrime(i,PrimeList)
    end = time.time()
    print (len(PrimeList),' prime numbers found in the range')
    print ('Time consumed: '+str(round(end-start,5))+' sec')
    ans = input('Show prime list? (y/n): ')
    if (ans.lower() == 'y'):
        print (PrimeList)
else:
    print ('Input Invalid. Bye-Bye!')
