import urllib2,pickle
def result():
	source = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
	loads = pickle.load(source)
	for items in loads:
		print "".join([i[0]*i[1] for i in items])
if __name__ == '__main__':
	result()

