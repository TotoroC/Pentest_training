#Tạo danh sách (list)
**Trong HTML có 3 kiểu danh sách:**
- **Ordered List**(Kiểu sắp xếp): Là kiểu hiện thị một danh sách mà các mục con của nó được sắp xếp theo thứ tự bảng số hoặc chữ cái
- **Unordered List**(Kiểu không sắp xếp): Là kiểu hiển thị danh sách mà các mục con của nó sẽ không được sắp xếp theo thứ tự mà chỉ được đánh dấu bằng một ký tự đặc trưng
- **Description List**(Kiểu mô tả): Là kiểu hiển thị danh sách mà các mục con của nó sẽ không được đánh dấu thứ tự, nhưng sẽ có kèm theo một đoạn miêu tả

####Ordered List
- Được bao bọc bởi cặp thẻ **\<ol>\</ol>**
- Bên trong cặp thẻ này sẽ là danh sách các mục con, mỗi mục sẽ được đặt trong cặp thẻ **\<li>\</li>**
- Thẻ **<ol>** cũng hỗ trợ thêm một thuộc tính là **type**, thuộc tính này là để thiết lập kiểu sắp xếp các mục con, gía trị của thuộc tính tye là `1,i,I,a,A`

####Unordered List
- Được bao bọc bởi cặp thẻ **\<ul>\</ul>**
- Các mục con bên trong sẽ được khai báo bằng cặp thẻ **\<li>\</li>**
- Thay đổi hiển thị của thẻ \<ul> bằng cách thêm thuộc tính style với thuộc tính CSS là** list-style-type** và giá trị **disc**, **square**, **circle** và **none**.

####Description List
- Được bao bọc bởi cặp thẻ **\<dl>\</dl>**
- Tên mỗi mục con sẽ được khai báo bằng cặp thẻ **\<dt>\</dt>** và mô tả cho mục con sẽ được khai báo bằng cặp thẻ **\<dd>\</dd>**

####Xếp chồng danh sách
- Xếp chồng bằng cách lồng thêm một danh sách nữa vào cặp thẻ **\<li>\</li>** của mục con cần thêm tầng.
<img src = "http://i.imgur.com/CZxShRa.png">

[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)
