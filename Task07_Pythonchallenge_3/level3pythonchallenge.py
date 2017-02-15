import urllib2
def getcode(): #lay doan ma can thiet tu source web
	req = urllib2.Request(url = 'http://www.pythonchallenge.com/pc/def/equality.html')
	f= urllib2.urlopen(req).read()
	start = f.index('kA')
	end = f.index('-->')
	code = f[start:end]
	return code
def findresult(strings):
	result = ""
	for index in range(len(strings)):
		# kiem tra xem tai ki tu o vi tri trong chuoi co phai chu hoa hay khong
		if strings[index].isupper(): 
			#Kiem tra cac dieu kien de tim ra phan tu trong chuoi can tim
			if (strings[index - 1].islower() and strings[index + 1].isupper() 
				and strings[index + 2].isupper() and strings[index + 3].islower() 
				and strings[index + 4].isupper() and strings[index + 5].isupper()
				and strings[index + 6].isupper() and strings[index + 7].islower()):
					result = result + strings[index+3]
	print result

if __name__ == '__main__':
	var = getcode()
	findresult(var)