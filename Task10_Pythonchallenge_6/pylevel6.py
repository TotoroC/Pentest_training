#-*- coding: utf-8 -*-
import zipfile,re
def find():
	source = zipfile.ZipFile('channel.zip') # mở file zip
	number = ['90052'] # file đầu tiên cần mở theo gợi ý trong file readme.txt ở trong file zip
	comment = ''
	while True:
		text = source.read(number[0]+'.txt') #đọc nội dung của file trong file zip
		comment += source.getinfo(number[0]+'.txt').comment #getinfo(): trả về vị trí của file(thuộc file zip), comment là phần gắn liền với file zip, nó thuộc phần thông tin của file trong file zip, nó được lấy thông qua vị trí của file
		if 'Next' in text:
			number = re.findall("[0-9]+",text) #lấy số trong nội dung file để mở file tiếp theo
		else:
			print text
			break
	print comment
if __name__ == '__main__':
	find()
