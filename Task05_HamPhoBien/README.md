#Một số hàm phổ biến
*Tên tài liệu: Một số hàm phổ biến*

*Người thực hiện: Hoàng Quốc Cường*

##Mục lục:
- [1.Tìm hiểu về cú pháp If else, for else, while.](#if)
<ul>
<li>	[1.1.Cú pháp if else](#il)</il>
<li>	[1.2.Cú pháp for else](#fo)</li>
<li>	[1.3.Cú pháp While](#while)</li>
</ul>
- [2.Tìm hiểu các hàm, câu lệnh: range(), break, continue, pass](#range)
<ul>
<li>	[2.1.Hàm range()](#re)</li>
<li>	[2.2.Câu lệnh break, continue, pass](#br)</li>
</ul>
- [3.Cách khai báo hàm? Đặt giá trị mặc định cho tham số truyền vào? VÍ dụ minh họa.](#func)
- [4.TÌm hiểu về biến toàn cục **\__name\__**. Và cú pháp **\__name\__** = **'\__main\__'**](#btc)
- [5.Cú pháp Lambda. Ví dụ minh họa.](#lam) 

##Nội dung
<a name = "if"></a>
###1.Tìm hiểu về cú pháp If else, for else, while
<a name = "il"></a>
####1.1.Cú pháp if else
- Cũng giống như các ngôn ngữ lập C, câu lệnh if else được sử dụng để kiếm tra điều kiện, nếu điều kiện của if là True thì nó sẽ thực hiện khối lệnh trong if, còn nếu False thì nó sẽ thực hiện khối lệnh của else. Ở sau mỗi dòng lệnh if, else cần phải có dấu (**:**) thì câu lệnh mới thực hiện.
```
	if a > b:
	           print "Dung"
	else:
	           print "Sai"
```
- Ngoài **if, else** ra còn có một câu lệnh là **elif** ( viết tắt của else if). Cách thức thực hiện của lệnh elif cũng giống như if, nó cũng kiểm tra điều kiện của nó, nếu đúng sẽ thực hiện khối lệnh trong elif, nếu sai, nó sẽ chuyển qua câu lệnh tiếp theo. Không giống như else chỉ có thể đặt một lần sau if, elif có thể đặt nhiều lần.
```
if a > b and a > c:
	print "a la so lon nhat"
elif b > c and b > a:
	print "b la so lon nhat"
else:
	print "c la so lon nhat"
```
- Trong python, không cung cấp các lệnh Switch hoặc case như các ngôn ngữ khác, nhưng ta có thể sử dụng các câu lệnh if ... elif để thực hiện vai trò của switch hoặc case.

<a name = "fo"></a>
####1.2.Cú pháp For else.
- Cú pháp For trong python khác một chút so với C. Thay vì cho phép người dùng tự định nghĩa bước lặp và điều kiện dừng như trong C,  câu lệnh for trong python lặp qua các phần tử của một dãy bất kỳ (list, string) theo thứ tự mà chúng xuất hiện trong dãy.
```
a = ['Ka','Me','Ka','Me','Ha']
for i in a:
	print i
```
Kết quả thu được:
```
Ka
Me
Ka
Me
Ha
```
-Trong Python, ta có thể dùng lệnh else đi kèm với vòng lặp for, câu lệnh else được thực thi khi vòng lặp dừng lại.
```
#kiem tra so chan
a = [10,11,12,13,14,15,16,17,18,19,20]
d = 0
for i in a:
	if a % 2 == 0:
		d += 1
else:
	print 'Co tong cong co ',d,' so chan.'
```

<a name = "while"></a>
####1.3.Câu lệnh While.
- Vòng lặp While sẽ thực hiện lặp đi lặp lại khối lệnh trong nó khi điều kiện của nó là True. Khi điều kiện là False thì sẽ thoát ra khỏi vòng lặp.
```
while (biểu_thức_điều_kiện):
	#khối lệnh
```
- VÍ dụ:
```
i = 20
S = 0
while (i != 0):
	S +=i
	i -=1
print "Tong day so la",S
```

<a name = "range"></a>
###2.Tìm hiểu hàm, câu lệnh: range(), break, continue, pass.
<a name = "re"></a>
####2.1.Hàm range()
- Hàm range() dùng để tạo một list số học. Ví dụ, để tạo 1 danh sách từ có 10 phần tử liên tiếp nhau, thay vì ghi ra cụ thể ra, ta có thể làm như sau:
>>a = range[10]

Kết quả:
>>a = [0,1,2,3,4,5,6,7,8]

-Cú pháp
```
range(a) : tạo ra một dãy có a phần tử
range(10) -> [0,1,2,3,4,5,6,7,8,9]

range(a:b): tạo ra một dãy có a phần tử bắt đầu từ a
range(4,9) -> [4,5,6,7,8]

range(a:b:c) tạo ra một dãy bắt đầu từ a sao cho mỗi phần tử cách nhau c đơn vị và các phần tử đó thuộc khoảng [a,b).
range(0,8,3) - > [0,3,6]
```
<a name = "br"></a>
####2.2.Câu lệnh break, continue, pass
- Cách thức hoạt động của câu lệnh break, continue trong Python tương tự như trong C.
- Lệnh break, nhảy ra khỏi vòng lặp nhỏ nhất chứa nó. Khi xét đến 1 vòng lặp, khi thực hiện đến câu lệnh trên trong vòng lặp mà gặp lệnh break, thì nó sẽ kết thúc vòng lặp và nhảy ra ngoài. Đối với vòng lặp lồng vòng lặp, nó sẽ thoát ra khỏi vòng lặp con và bắt đầu thực thi dòng code tiếp theo trong vòng lặp lớn.
```
#Tim so chan dau tien
for i in range(20):
	if i % 2 == 0:
		print i,'la so chan dau tien'
		break
```
- Lệnh continue, tiếp tục vòng lặp kế của vòng lặp. Thông thường trong một vòng lặp, các câu lệnh sẽ được thực hiện lần lượt từ trên xuống dưới, nhưng khi trong các câu lệnh đó có một câu lệnh continue, thì nó sẽ chỉ thực hiện đến câu lệnh continue và tiếp tục vòng lặp mới, cho dù sau câu lệnh continue còn các câu lệnh khác đi chăng nữa.
```
d = 0
for i in range(20):
	if i % 2 != 0:
		d +=1
		continue
		print i," la so chan."
```
- Câu lệnh pass là một hoạt động null và không có gì xảy ra khi nó thực thi. Nó được sử dụng khi cú pháp cần một câu lệnh nhưng chương trình không cần tác vụ nào.
```
While 5 != 0:
	pass
```

<a name = "func"></a>
###3.Cách khai báo hàm? Đặt giá trị mặc định cho tham số truyền vào? Ví dụ minh họa.
- Để khai báo một hàm, ta sử dụng cú pháp như sau:
```
def ten_ham(giatri1,giatri2,...):
	#Khối lệnh
```
- Trong đó, def được sử dụng để bắt đầu phần định nghĩa hàm. Def xác định phần bắt đầu của khối hàm.
-Ví dụ:
```
#Hàm tính giai thưa
def giaithua(n)
	if n < 1: 
		return 1
	else:
		return n*(giaithua(n-1))
```
- Tham số mặc định là tham số cung cấp giá trị mặc định cho các tham số được truyền vào trong hàm, trong trường hợp giá trị không được cung cấp trong lời gọi hàm.
```
def giaithua(n = 6)
	if n < 1: 
		return 1
	else:
		return n*(giaithua(n-1))
print  giaithua()
--> 720
```

<a name = "btc"></a>
###4.TÌm hiểu về biến toàn cục **__name__**. Và cú pháp **__name__** = **'__main__'**
- Biến được định nghĩa bên ngoài gọi là biến toàn cục. BIến toàn cục có thể được truy cập bởi tất cả các hàm ở khắp nơi trong chương trình. DO đó phạm vi của biến toàn cục là rộng nhất.
```
a = 18
def tong():
	b = 25
	print "Tong cua a va b la",a + b
print tong()
```
- *__name__* là biến lưu trữ tên của module đang được sử dụng, hay nói các khác là lưu trữ tên file. Tên của module chính sẽ luôn là main, các module khác được thêm vào sẽ là tên file module đó.
```
task04.py
#khong co chi ca

vidu.py
import task04
print __name__
print task04.__name__

Kết quả:
__main__
task04
```
- Khi viếì**if __name__ =  '__main__':** thì python sẽ thực thi phần lệnh phía sau của lệnh if nếu file này được thực thi bằng lệnh python.
<img src = "http://i.imgur.com/VWBGdVQ.jpg">
<img src = "http://i.imgur.com/5UZ4wxh.jpg">

<a name = "lambda"></a>
###5.Cú pháp Lambda. Ví dụ minh họa.
- Hàm không có tên và chúng không được khai báo theo cách chính thực bởi từ khóa **def** gọi là hàm vô danh. Để khai báo hàm này, ta sử dụng từ khóa **lambda**. Nó nhận bất kỳ tham số nào và chỉ trả về giá trị trong dạng một biểu thức được ước lượng.
```
s = lambda x: x*5
print s(5)

Kết quả:
25
```
Cú pháp:
>>lambda variable: bieu_thuc

