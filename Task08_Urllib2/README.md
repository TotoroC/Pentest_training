#Module Urllib2 nâng cao
*Tên tài liệu: Module Urllib2 nâng cao*

*Người thực hiện: Hoàng Quốc Cường*

##Mục lục
- [1.Tìm hiểu addon Live HTTP Headers trên firefox](#1)
- [2.Ý tưởng giải challenge programing hackthissite.org](#2)

##Nội dung:

<a name ="1" />
###1.Tìm hiểu add-on Live HTTP Headers trên firefox
- Live HTTP Headers là một add-on giúp chúng ta xem "header" của trang web (trong header có các thông số như cookie, referer, user-agent,...)khi đang duyệt. Ngoài ra, nó có thể Replay - tái tạo lại truy vấn bất kỳ và cho phép bạn chỉnh sửa các thông tin header cũng như nộ dung, dữ liệu cua truy vấn đó.

<img src = "http://i.imgur.com/MOHw6tJ.png">

<a name = "2" />
###2.Ý tưởng giải challenge programing hackthissite.org
Thuật toán:
- Lấy từng phần tử trong danh sách unscrambled và wordlist
- Chuyển phần tử vừa lấy được từ dạng chuỗi về dạng list và sắp xếp chúng bằng phương thức sort() 
- So sánh từng phần tử của danh sách unscrambled với các phần tử của wordlist sau khi các phần từ đó được sắp xếp
- Nếu 2 phần từ được so sánh cấu thành từ các phần tử con giống nhau thì lấy phần tử đó của wordlist khi chưa được sắp xếp làm kết quả.

Ý tưởng:
- Sau khi có được thuật toán, ta sử dụng đến thư viện urllib2, re và add-on Live HTTP Header.
- dùng urllib2.Request() và urllib2.urlopen() để đưa source web về.
- Sử dụng tham số data để truy 
- Ta dùng module re.findall trong thư viện re để tiến hành lọc và lấy list unscrambled có trong challenge programing 1 hackthissite. 
- dùng urllib2.Request() kèm theo kết quả cần tìm truy vấn lên web để hoàn thành challenge
- Sử dụng add-on Live HTTP Headers để lấy cookie, referer, submit.

Xem source tại [đây](https://github.com/TotoroC/python_trainings/blob/master/task08/programingHTS1.py)
