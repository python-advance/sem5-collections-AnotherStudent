import random

def knifeList(l, f):
	a = list()
	b = list()

	for i in l:
		if f(i):
			a.append(i)
		else:
			b.append(i)
	return a, b


array = [random.randint(-99, 99) for _ in range(10)]

a, b = knifeList(array, lambda item: item >= 0)

print("source: \n", array)
print("knife 1: \n", a)
print("knife 2: \n", b)