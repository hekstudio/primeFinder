import time
# ======================================
#  Function: Check if a number is prime
# ======================================
def checkPrime(number,prime_list):
    for p in prime_list:
        if(number % p == 0): # Not prime
            return False
        if(p > (number/p)):
            prime_list.append(number)
            return True
# ======================================
#  Function: Find all <= number
# ======================================
def generatePrimes(number):
    tempList = [2]
    for i in range(3,number+1):
        checkPrime(i,tempList)
    return tempList
# --------------------------------------
# Program starts here
# --------------------------------------
PrimeList = [2] # PrimeList starts from 2
size = input('Enter range for PrimeFinder: ')
if (size.isdigit()):
    start = time.time()
    # --------------- CORE ---------------
    PrimeList = generatePrimes(int(size))
    # --------------- CORE ---------------
    end = time.time()
    print (len(PrimeList),' prime numbers found in the range')
    print ('Time consumed: '+str(round(end-start,5))+' sec')
    ans = input('Show prime list? (y/n): ')
    if (ans.lower() == 'y'):
        print (PrimeList)
else:
    print ('Input Invalid. Bye-Bye!')
