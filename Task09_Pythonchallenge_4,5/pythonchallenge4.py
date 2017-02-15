import urllib2,re
def find():
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
	text = 'and the next nothing is (\d+)'
	number = '12345'#8022
	while True:
		try:
			source = urllib2.urlopen(url % number).read()
			number = re.search(text,source).group(1)
			print number
			if number == '16044':
				number = 16044/2
		except:
			print source
			break
		
if __name__ == '__main__':
	find()


