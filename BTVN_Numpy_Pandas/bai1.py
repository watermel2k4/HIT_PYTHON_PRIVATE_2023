import numpy as np

n = int(input())

a = np.random.randint(1, 15, n)

b = np.arange(0, 200, 2)[:100]

c = np.zeros((n, n))

d = np.eye(n)

e = np.diag(a)

print("Ma trận a:")
print(a)
print("ndim:", a.ndim)
print("shape:", a.shape)
print("len:", len(a))
print("itemsize:", a.itemsize)
print("dtype:", a.dtype)
print()

print("Ma trận b:")
print(b)
print("ndim:", b.ndim)
print("shape:", b.shape)
print("len:", len(b))
print("itemsize:", b.itemsize)
print("dtype:", b.dtype)
print()

print("Ma trận c:")
print(c)
print("ndim:", c.ndim)
print("shape:", c.shape)
print("len:", len(c))
print("itemsize:", c.itemsize)
print("dtype:", c.dtype)
print()

print("Ma trận d:")
print(d)
print("ndim:", d.ndim)
print("shape:", d.shape)
print("len:", len(d))
print("itemsize:", d.itemsize)
print("dtype:", d.dtype)
print()

print("Ma trận e:")
print(e)
print("ndim:", e.ndim)
print("shape:", e.shape)
print("len:", len(e))
print("itemsize:", e.itemsize)
print("dtype:", e.dtype)
