#Các thẻ định dạng chữ viết và văn bản
####Tiêu đề và đoạn văn bản
- Headline(tiêu đề) và Paragraph(đoạn văn bản)
- Các thẻ tiêu đề được định dạng bằng cặp thẻ **<hn>** trong đó n là số từ 1 đến 6, độ lớn của tiêu đề giảm dần từ 1 đến 6.
- Đoạn văn bản được khai báo bằng cặp thẻ **\<p>\</p>**. Các văn bản nàm trong cặp thẻ này được hiểu là một đoạn văn bản, mỗi đoạn sẽ được xuống dòng và cách nhau tỉ lệ nhất định.

####Các thẻ định dạng chữ viết
- \<strong> hoặc \<b>: in đậm chữ viết
- \<i>: in nghiêng
- \<u>: gạch dưới
- \<strike>: gạch ngang chữ viết
- \<em>: Nhấn mạnh câu
- \<code>: Định dạng cho một đoạn mã nào đó
- \<hr>: thước kẻ ngang trên tài liệu
- \<mark>: Tô sáng chữ viết 

####Thẻ trích dẫn
- **Quote**(trích dẫn) 
- Hay được sử dụng trong viết báo hay phóng sự
- Mục địch: Định dạng 1 câu nói như một câu trính dẫn
- Thẻ trích dẫn được quy định là \<quote> và tên tác gỉa được quy định là \<cite>
- **Note**: thẻ \<cite> thường chỉ nên dùng đặt trong thẻ \<quote>.

####Thẻ định dạng sẵn
- **Preformatted**: \<pre>\</pre>
- Nội dung bên trong cặp thẻ được tự động định dạng về kích thước chữ, khoảng cách, kiểu chữ,...
- Thường được dùng để đăng một câu đối thoại hoặc in một đoạn mã để cho phân biệt với văn bản thường

####Thuộc tính style để định dạng chữ viết
- Thêm màu sắc cho chữ
- Có thể đặt trong bất cữ thẻ nào và giá trị của thuộc tính đó là các thuộc tính CSS

####Màu chữ
- sử dụng thuộc tính color
>><p style="color:red">Chữ đỏ</p>

####Màu nền
- sử dụng thuộc tính background-color
>><p style="background-color:red">Chữ có nền màu đỏ</p>

####Kích thước chữ
- sử dụng thuộc tính font-size và giá trị là số kèm đơn vị. Các đơn vị có thể sử dụng: px, %, pt hoặc em
<p style="font-size:18px">Chữ có kích thước 18px</p>

####Font chữ
- Sử dụng thuộc tính font-family với giá trị tên font chữ có trên máy tính để thay đổi font chữ khác so với font mặc định
>><p style="font-family: Arial">Font Arial</p>
- Ngoài ra, có thể thêm font dự phòng bằng cách khai báo nhiều font khác nhau và được ngăn cách bởi đấu phẩy

####Căn lề văn bản
- Sử dụng thuộc tính text-align với các giá trị left, center, right hoặc justify
>><p style="text-align:center">Canh giữa văn bản</p>
[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)
