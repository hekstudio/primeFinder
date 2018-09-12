from PrimeFinder import generatePrimes
import time

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