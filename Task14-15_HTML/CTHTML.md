#Cấu trúc của một file HTML
Một tài liệu HTML có 4 yếu tố chính:
- **Có thể khai báo loại tập tin/tài liệu**
- **CÓ thẻ đóng và mở tài liệu HTML**
- **Có thẻ đóng và mở phần thông tin website**
- **Có thể đóng và mở phần nội dung website**

####Thẻ khai báo tập tin
- Là thẻ khai báo loại tập tin của file HTML
- Khai báo đầu tiên
>><!DOCTYPE>

- Có một vài tham số đi kèm với thẻ <!DOCTYPE>. Ví dụ như để định dạng đây là tài liệu HTML5 thì cần cần khai báo thêm tham số html trong thẻ <!DOCTYPE>

####Thẻ mở đóng tài liệu HTML
- Là cặp thẻ **\<html>\</html>**
- Giúp trình duyệt biết rằng những nội dung khai báo trong thẻ này là HTML
- Thuộc tính **lang** với giá trị **vi** `<html lang="vi">` trong thẻ **<html>** giúp trình duyệt biết ngôn ngữ mà ta đang sử dụng, giá trị **vi** có nghĩa là Vietnamese
- **Note**: Thẻ **\<html>\</html>** phải bao bọc toàn bộ nội dung website, không bao gồm thẻ **\<!DOCTYPE>**

####Thẻ đóng và mở phần thông tin website
- Phần khi báo thông tin được đặt bên trong cặp thẻ **\<head></head>**
- Nội dung bên trong có thể là: thông tin website(mea), tên website(title), khai báo CSS(style), khai báo đoạn Javascript(script),....

####Thẻ đóng mở phần nội dung website
- **\<body>\</body>** là cặp thẻ xác định phần thân website, chứa nội dung của website đó

[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)