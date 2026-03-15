import time
n=270361506359519402428185053473069848173

start_time = time.time()
a=isqrt(n)+1
while True:
        b2=a^2-n
        if is_square(b2):
            b=sqrt(b2)
            break
        a=a+1

p=a+b
q=a-b
print("\nTime: %s seconds" % (time.time() - start_time))


print(p.is_prime())
print(q.is_prime())
print(n==p*q)