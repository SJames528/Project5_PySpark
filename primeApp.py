from pyspark import SparkContext
import numpy as np
import time
import math
sc = SparkContext("local", "test app")

#Set desired bits of security
k=16

#Generate a random number of roughly size 2^k. We achieve this by uniformly sampling an exponent close to k (but generated random number not uniform on [2^(k-1),2^(k+1)]).
u=np.random.uniform(k-1,k+1)
n=math.ceil(2**u)

#Alternatively, use a fixed prime n since it is unlikely that a randomly chosen integer is prime

#n=13

q=math.ceil(math.sqrt(n))
r=sc.parallelize(list(range(2,q+1)))

#To see how long this takes, we start a timer
timeStrt=time.time()

#We now perform the mapping parts of the algorithm. We test in parallel if each member of the list is a divisor of n, and then add up how many return true.
div=r.map(lambda a: (n%a)==0)
totDiv=div.reduce(lambda a,b:a+b)

#If our total number of divisors is zero, we have a prime. Otherwise, there is a divisor of n, so we do not have a prime
if totDiv==0:
    print("%i is prime" % n)
else:
    print("%i is not prime" % n)

#Stop our timer, and print the total duration
timeElpsd=time.time()-timeStrt
print("Time Elapsed = %f seconds" % timeElpsd)
