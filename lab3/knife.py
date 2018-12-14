import random

def knifeDict(l, f):
	a = dict()
	b = dict()

	for i in l.items():
		if f(i):
			a.update({i[0]: i[1]})
		else:
			b.update({i[0]: i[1]})
	return a, b


d = {
	"amiga": {"isOpenSource":False, "unixLike": False},
	"osx": {"isOpenSource":False, "unixLike": True},
	"linux": {"isOpenSource":True, "unixLike": True},
	"windows": {"isOpenSource":False, "unixLike": False},
}
a, b = knifeDict(d, lambda item: item[1]['unixLike'] == True)

print("source: \n", d)
print("unixLike YES: \n", a)
print("unixLike NO: \n", b)