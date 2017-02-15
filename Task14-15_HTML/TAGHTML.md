#Các thẻ khai báo thông thường trong HTML

####Khai báo tên tài liệu với cặp thẻ \<title>

- **\<title>\</title>**
- Các tác dụng khai báo tên tài liệu web
- Ứng dụng: Giúp trình duyệt hiển thị tên tài liệu khi mở lên và các cỗ máy tìm kiếm như Google cũng hiển thị nội dung trong cặp thẻ này để lấy tên tài liệu

####Khai báo dữ liệu vĩ mô với thẻ \<meta>

- **\<meta>**
- Là thẻ không có thẻ đóng nhưng có dấu gạch chéo ở cuối cùng
- Khai báo các dữ liệu vĩ mô trpng tài liệu web HTML: mô tả, từ khóa, tên tác giả, bảng mã kỹ tự sử dụng,....
- Luôn được khi báo kèm theo ít nhất là một thuộc tính và mỗi thuộc tính pải luôn có giá trị
```
<meta charset="utf-8"
charset là tên thuộc tính, utf-8 là giá trị của thuộc tính
```

**Thuộc tính charset**

- Dùng để khai báo cho trình duyệt biết bảng mã kỹ tự siêu văn bản bên trong tài liệu

**Thuộc tính name**

- Đối với thuộc tính name thì thẻ meta phải có hai thuộc tính đó là name và content. Thuộc tính content được xem là thiết lập nội dung của thuộc tính name
>><meta name="author" content="abc" />

- **author**: Khai báo tên tác giả
- **description**: Khai báo mô tả tài liệu
- **keyword**: Khai báo từ khóa của tài liệu, các từ khóa này sẽ đóng vai trò hỗ trợ tìm kiếm văn bản hoặc máy tìm kiếm website dò tìm
- **application-name**: Tên ứng dụng đại diện tài liệu web
- **generator**: Khai báo tên ứng dụng tạo ra tài liệu

[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)
