import time

# Initialize variables
x = 2
n = 11302120010051186159

# Start timer
start_time = time.time()

# Brute force loop to find factors
while x < n:
    if n % x == 0:
        print(x, n//x)
        break
    x += 1

# Print time
print("\nTime: %s seconds" % (time.time() - start_time))
