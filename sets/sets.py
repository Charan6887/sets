odds={1,3,5,7}
evens={2,4,6,8,9,0,3,1,5,7}
primes={2,3,5,7}
u=odds.union(evens)
print(u)
v=odds.intersection(primes)
print(v)
z=odds.difference(evens)
print(z)
x=odds.symmetric_difference(evens)
print(x)
print(odds.issubset(evens))
print(evens.isdisjoint(primes))