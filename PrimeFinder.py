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
