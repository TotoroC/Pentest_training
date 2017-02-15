#Python Challenge Level 8 & 9
*Người thực hiện: Hoàng Quốc Cường*

##Nội dung:
###Ý tưởng thực hiện:
**Challenge Level 8:**
- Mở source trang http://www.pythonchallenge.com/pc/def/integrity.html , khi bấm vào ../return/good.html ở dưới list coords, ta sẽ chuyển qua 1 trang với yêu cầu cần phải có username và password.
- Để ý xuống phần comments trong source web, ta thấy hai dòng:
```
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
```
- un tương ứng với username, pw tương ứng với password, ta sử dụng thư viện [bz2](https://docs.python.org/2/library/bz2.html) để giải nén.
- Dùng hàm decompress() trong thư viện bz2, ta có thể dễ dàng thu được kết quả:
```
huge
file
```
- Cuối cùng, bấm vào ../return/good.html để nhập un,pw và qua challenge tiếp theo.

[sourcelevel8](https://github.com/TotoroC/python_trainings/blob/master/task12/pylevel8.py)

**Challenge Level 9:**
- Nhìn bức hình và tiêu đề có tên là **connect the dots**, ta nghĩ ngay đến việc nối các điểm lại với nhau
- Mở source trang http://www.pythonchallenge.com/pc/return/good.html , nhìn xuống phần comment, ta có hai biến *first* và *second* có rất nhiều số, những con số đó chính là tọa độ những điểm mà ta cần nối lại với nhau.
- Có hai các để giải quyết bài này, cách 1 là dùng phương thức putpixel của thư viện Image, cách hai là dùng module ImageDraw.
- Kết quả cách 1:
<img src = "http://i.imgur.com/yUCEAj1.png">

- Kết quả cách 2:
<img src = "http://i.imgur.com/2lwxx4X.png">

- **bull** chính là kết quả của level 9.

[sourcelevel9](https://github.com/TotoroC/python_trainings/blob/master/task12/pylevel9.py)
