def alphabe():
	string = open('alpha.txt', 'r') #mo file alpha.txt trong che do doc va ghi
	S = ""
	for line in string: # vong lap lay tung dong trong file
		for i in line: # vong lap lay tung phan tu trong mot dong
			if i.isalpha() or i.isalnum():#kiem tra xem phan tu trong dong  co phai la chu cai hoac chu so hay khong
				S = S + i
	print S
	string.close()

if __name__ == '__main__':
	alphabe()