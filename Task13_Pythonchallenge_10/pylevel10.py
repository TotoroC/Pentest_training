#-*- coding:utf-8 -*-
def level10():
	string = '1'+' '
	j = 1
	while j<=30:	
		count = 1
		idx0 = string[0]
		result = ''
		for i in range(1,len(string)):
			if string[i] != idx0:
				result += str(count) + idx0
				idx0 = string[i] #gán giá trị của vị trí đầu tiên bằng giá trị của vị trí thứ i đang xét để tiến hành so sánh với i tiếp theo
				count = 1
			else:
				count +=1
		print len(result)
		string = result + ' '
		result = ''
		j +=1
if __name__ == '__main__':
	level10()