#SQL Injection Lab Level1
*Người thực hiện: Hoàng Quốc Cường*.
####1.Tìm hiểu lỗi
- Ta thử thêm dấu **\'** vào url như sau `http://192.168.12.20/sqli/example1.php?name=root'` thì ta được lỗi như sau:
<img src ="http://i.imgur.com/ctS3Nnu.png">
<img src ="http://i.imgur.com/BYJDKWh.png">
- Đây là dạng lỗi SQL injection xảy ra khi thiếu đoạn mã kiểm tra dữ liệu đầu vào trong truy vấn SQL. Kết quả là người dùng cuối có thể thực hiện một số truy vấn không mong muốn đối với CSDL của ứng dụng.
- `SELECT * FROM users WHERE name = '';`. Ví dụ khi ta nhập vào giá trị `null' or '1'='1` khiến câu truy vấn trên được hiểu như sau `SELECT * FROM users WHERE name = 'null' or '1'='1`; Vì 1=1 là một điều kiện đúng nên bất kỳ name là gì thì câu trên nó vẫn truy vẫn ra được kết quả đúng.
- Với đoạn code php như sau, ta có thể thực hiện đăng nhập bằng đoạn mã `null' or '1'='1` một cách bình thường. 

####2.Khắc phục
- Để khắc phục lỗi trên, ta cần xử lý các biến trong mã PHP bằng cách sử dụng hàm addslashes(): nó sẽ thêm dấu gạch chéo `\` vào trước các ký tự nháy đơn, nháy kép, null, gạch chéo. 
- Trước:
<img src ="http://i.imgur.com/A03bAdS.png">
- Và sau:
<img src ="http://i.imgur.com/t6zFccf.png">

Bạn có thể kiểm tra qua 2 đường dẫn sau:
- [Chưa khắc phục](http://taskphp01.freevnn.com/login1.php)
- [Đã khắc phục](http://taskphp01.freevnn.com/login.php)