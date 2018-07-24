
# ======================================
#  Function: Check if a number is prime
# ======================================
def checkPrime(number,prime_list):
    for p in prime_list:
        if(number % p == 0): # Not prime
            return False
    prime_list.append(number)
    return True
# --------------------------------------
# Program starts here
# --------------------------------------
PrimeList = [2] # PrimeList starts from 2
size = input('Enter range for PrimeFinder: ')
if (size.isdigit()):
    for i in range(2,int(size)):            
        checkPrime(i,PrimeList)
    print (len(PrimeList),' prime numbers found in the range')
    ans = input('Show prime list? (y/n): ')
    if (ans.lower() == 'y'):
        print (PrimeList)
else:
    print ('Input Invalid. Bye-Bye!')
