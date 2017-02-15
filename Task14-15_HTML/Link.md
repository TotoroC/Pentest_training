#Thẻ tạo liên kết và liên kết neo
- Sử dụng cặp thẻ **\<a>\</a>** để tạo ra các đường liên kết trong HTML

>><a href = "https://www.google.com" title = "Google-sensei" target = "_blank">bấm vô đây</a>

**Các thuộc tính thường gặp**

- **href**: Địa chỉ của tài liệu muốn liên kết đến, đây có thể là một đường dẫn thư mục hoặc địa chỉ website. Nếu muốn truy cập một tài liệu trên cùng một cấp thư mục thì chỉ cần ghi tên tập tin đó ra (abc.html)
- **title**: Tiêu đề của liên kết, tiêu đề sẽ hiển thị như một thông tin them khi rê chuột vào liên kết
- **target**: Xác định nơi mở tài liệu, nó có các giá trị như **_blank** (mở tài liệu trên cửa sổ mới), **_self**(mở tài liệu trên của sổ hiện tại, nếu không khai báo thuộc tính **target** thì nó sẽ sử dụng gía trị này làm mặc định), **_self**(mở tài liệu trong nội dung trang hiện tại), **_parent**(mở tài liệu trên khung trình duyệt)

- **Note**: Nội dung trong cặp thẻ \<a> có thể là một nội dung siêu văn bản nào, bao gồm các thẻ tiêu đề, hình ảnh,...

####Liên kết neo(Anchor Link)
- Là một liên kết trong siêu văn bản sẽ chỉ dẫn đến một vị trí đặc biệt trong cùng tài liệu mà không phải tải lại hoặc mở một tài liệu mới. Một liên kết neo sẽ có hai phần:
		
		- Khu vực được neo, được khai báo bằng thẻ bất kỳ với thuộc tính id (<p id="noi-dung"></p>)
		- Liên kết neo, được khai báo bằng thẻ <a> nhưng có thuộc tính **href** nhưng giá trị là có dấu *#* và tên id của khu vực cần truy cập đến (<a href="#noi-dung">xem nội dung</a>)
		
[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)