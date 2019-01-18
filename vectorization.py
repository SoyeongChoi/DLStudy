import numpy as np

a = np.array([1,2,3,4])
print(a)

import time

a = np.random.rand(1000000)
#이 코드는 난수로 이루어진 백만차원의 배열을 만들어줌
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized version:"+str(1000*(toc-tic))+"ms")

c = 0
tic = time.time()
for i in range (1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("for loop:"+str(1000*(toc-tic))+"ms")


