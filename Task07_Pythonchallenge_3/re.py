# -*- coding:utf-8 -*-
import urllib2
import re
def getcode(): #lay doan ma can thiet tu source web
	req = urllib2.Request(url = 'http://www.pythonchallenge.com/pc/def/equality.html')
	f= urllib2.urlopen(req).read()
	start = f.index('kA')
	end = f.index('-->')
	code = f[start:end]
	return code
def findresult(strings):
	result = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",strings)
	#phương thức final của thư viện re trả về tất cả mẫu phù hợp không trùng lặp trong chuỗi
	#[^A-Z]:  kết nối tất cả các giá trị từ ngoại trừ [A-Z]
	#[A-Z]: kết nối tất cả các giá trị từ A-Z
	#[A-Z]{3}: gấp 3 lần [A-Z]
	#[a-z]: nhận tất cả các giá trị từ a-z
	print "".join(result)
if __name__ == "__main__":
	var = getcode()
	findresult(var)