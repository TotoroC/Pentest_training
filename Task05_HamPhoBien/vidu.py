import math
def gt(n):
	i = 0
	S = 1
	while i <= n:
		if i < 1:
			S = 1
		else:
			S = S*i
		i += 1
	print "Giai thua cua",n,"la",S

def chinhphuong():
	d = 0
	result = []
	for i in range(1,11):
		if i % math.sqrt(i) == 0:
			result += str(i) 
	else:
		print 'Day so chinh phuong tu 1 den 10:',result
def qua():
	pass
def timso(n,m):
	for i in range(1,n):
		if i == m:
			print 'So can tim ',m,' o chi muc thu ',i - 1,'trong day',range(1,n)
			break
		else:
			continue
def lambd(n):
	cube = lambda x: x**3
	print 'lap phuong cua ',n,' la ',cube(n)

if __name__=='__main__':
	gt(5)
	chinhphuong()
	timso(11,5)
	lambd(5)
