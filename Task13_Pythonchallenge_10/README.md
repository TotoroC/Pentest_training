#Python Challenge Level 10
*Người thực hiện: Hoàng Quốc Cường*

##Nội dung:
###Ý tưởng giải:
- Truy cập vào trang python challenge level 10, đầu tiên ta sẽ nhìn thấy dòng chữ vàng **len(a[30])**. Vẫy có nghĩa là ta cần tìm độ dài của phần tử thứ 30 trong a.
- Xem source của trang vào truy cập vào file **sequence.txt**, có trong source, ta sẽ tìm được chuỗi *a = [1, 11, 21, 1211, 111221,* nhưng nó mới chỉ có 5 phần tử, cái ta cần tìm là các phần tử còn lại và độ dài của phần tử thứ 30.
- a được gọi là dãy [Lock-and-say](https://en.wikipedia.org/wiki/Look-and-say_sequence)
```
'1' đọc là '1 số 1' hay '11' 
'11' đọc là '2 số 1' hay '21'
'21' đọc là '1 số 2, 2 số 1' hay '1211'
'1211' đọc là '1 số 1, 1 số 2, 2 số 1' hay '111221'
```
- Đầu tiên, ta gán biến string có chuỗi là '1'. Gán vị trí đầu tiên là idx0 = string[0].
- Cho i chạy từ vị trí thứ 2, đến độ dài của chuỗi string. Kiểm tra, nếu vị trí thứ 2 khác vị trí đầu tiên, lẫy chuỗi rỗng khởi tạo ban đầu, cộng với sô lần ( số lần chỉ sự xuất hiện của ký tự đang xét xuất hiện liên tiếp nhau trong chuỗi) và cộng với vị trí ban đầu. Ta lấy vị dụ ở trên, vì vị trí đầu tiên là **1**, khác vị trí thứ hai là **rỗng**, nên, số luần xuất hiện của nó chỉ có 1, nên chuỗi mới sẽ là '11'. Nếu vị trí thứ nhất bằng vị trí thứ 2, số lần xuất hiện của ký tự đó cộng thêm 1.
- Để xuất ra màn hình đến phần tử thứ 30, ta chỉ cần đặt nó bên trong vòng lặp, cứ mỗi lần kết thúc vòng lặp thì string sẽ bằng chuỗi mới được tạo ra.
- Kết quả thu được là **len(a[30]) = 5808**

[sourcecode](https://github.com/TotoroC/python_trainings/blob/master/task13/pylevel10.py) 
