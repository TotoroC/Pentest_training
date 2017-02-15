#SQL Injection
*Người thực hiện: Hoàng Quốc Cường*

###SQLi là gì ? Xảy ra khi nào ? Tác hại ra sao ?
- SQL Injection là một kỹ thuật cho phép kẻ tấn công lợi dụng lỗ hổng của việc kiểm tra dữ liệu đầu vào trong các ứng dựng web và các thông báo lỗi của hệ quản trị được trả về để inject và thi hành các câu lệnh SQL bất hợp pháp
- Xảy ra trên các ứng dụng web có dữ liệu được quản lý bằng các hệ quản trị CSDL : SQL Server, MySQL, Oracle, DB2, Sysbase, ...
- Tác hại: Giúp Hacker chiếm đoạt quyền kiểm soát về mặt dữ liệu, cài backdoor trên server mà ứng dụng đang chạy => kiểm soát toàn bộ hệ thống

###Information_schema:
- Là cơ sở dữ liêu thông tin về tất cả các CSDL khác được lưu trữ
- Cung cấp quyền truy cập vào siêu cơ sở dữ liệu, thông tin về máy chủ MySQL cũng như tên một cơ sở dữ liêu hoặc một bảng
- Có khá nhiều bảng view trong information_schema, nhưng ta thường quan tâm đến 2 bảng chính là tables( thông tin về tất cả các bảng có trong tất cả database) và columns( thông tin về tất cả các cột có trong database)
<img src="http://i.imgur.com/vfSZLBp.png">

###Bài Lab:
**Bước 1: Kiểm tra:**
- Đầu tiên, ta truy cập vào địa chỉ của máy ảo 192.168.12.9
- Ta sẽ tìm các địa chỉ có dạng ...?id=
- Thêm dấu `' ` hoặc `and 1=0` sau số id để kiểm tra xem web có bị lỗi hay không
<img src="http://i.imgur.com/eaD4coV.png">
**Bước 2: Kiểm tra phiên bản:**
- Bước này khá quan trọng, kiểm tra phiên bản để lựa chọn cách khai thác phù hợp
- Nhúng lệnh SQL là `ORDER BY` trên URL, ta sẽ được lỗi sau
<img src="http://i.imgur.com/jVM9vQS.png">
- Ta lựa chọn 1 số lớn, rồi từ từ giảm dần đến khi nào hết lỗi, thì ta tìm được số cột trên web
<img src="http://i.imgur.com/jVM9vQS.png">
-Ta dùng lệnh `UNION SELECT 1,2,3,4` để  tiến hành truy xuất lỗi
<img src="http://i.imgur.com/MmaxXSP.png">
- Như hình, ta thấy lỗi ở cột 2, ta thay 2 = version(), ta sẽ thu được phiên bản SQL.
<img src="http://i.imgur.com/FDVO7rj.png">
**Bước 3: Truy xuất các  bảng**
- Ta dùng lệnh `UNION SELECT 1,group_concat(table_name),3,4 FROM information_schema.tables-- -`
<img src="http://i.imgur.com/P5IDxfE.png">
- Lệnh group_concat(table_name) dùng để gộp các bảng thành một đường thằng và các bảng đó ta lấy từ `information_schema`
- Ta thêm điều kiện `WHERE table_schema=database()` đề tìm các bảng có trong cơ sở dữ liệu
<img src="http://i.imgur.com/gH3BiaR.png">
**Bước 4: Truy xuât kết quả**
- Ta thấy được bảng users có khả năng chứa thông tin về admin, ta tiến hành truy xuất các cột có trong bảng đó. Ta cho điều kiện `table_name=0xusers`, ở trong hình, users cần phải được chuyển đổi thành mã hex.
<img src="http://i.imgur.com/d8zX5ij.png">
- Sau đó ta thu được kết quả gồm id, login, password. Ta tiếp tục truy xuất chúng ra.
<img src="http://i.imgur.com/23DszKy.png">
- Và kết quả cuối cùng thu được. Nhìn qua, ta có thể đoán password là một mã MD5, nên ta tiến hành decrypt nó bằng các tool trên mạng.
- login: **admin**, password: **P4ssw0rd**