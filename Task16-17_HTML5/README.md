#HTML5
##Nội dung
###Sự khác nhau giữa HTML và HTML5

Khai báo <!DOCTYPE> đối với HTML5 đơn giản hơn, chỉ cần <!DOCTYPE html> là trình duyệt sẽ hiểu là bạn đang dùng HTML5, còn các phiên bản HTML cũ, phải khai báo khá dài.

```
HTML5
<!DOCTYPE html>
XHTML 1.1
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```
Ta có thể thấy sự khác nhau giữa HTML5 với HTML qua 2 hình dưới đây:

- Cấu trúc HTML5:

<img src="http://i.imgur.com/Y05pnmv.png">

- Cấu trúc HTML:

<img src="http://i.imgur.com/Xz8JDYy.png" width="320" height="320">

HTML bổ sung thêm rất nhiều thẻ đánh dấu:

- Các thẻ \<header> và \<footer> giúp tách các phần trên và dưới của các block nột dung. Để có thẻ sử dụng nhiều lần trên trang duy nhất.
- Thẻ \<article> giúp xác định một phần cụ thể về nội dung, ví dụ một bài blog hoặc một bình luận
- Thẻ \<nav> để xác định phần nào được coi là khối điều hướng ( có các link điều hướng, có thể hiểu đây là một thẻ menu)
- Thẻ \<section> cho phép bạn xác định một phần nội dung nào đó, tương thẻ như các thẻ \<div>
- Các thẻ \<audio> và \<video> để đánh dấu những nội dung bao gôm âm thanh oặc video
- Thẻ \<canvas> cho phép vẽ đồ họa sử dụng một ngôn ngữ kịch bản riêng biệt
- Thẻ \<embed> dùng để nhúng các nội dung hoặc ứng dụng bên ngoài vào web

HTML5 cũng bỏ đi một số thẻ: \<acronym>, \<applet>, \<font>, \<frameset>, \<noframes>,....

- Nhìn sơ qua ví dụ của các thẻ:

<img src="http://i.imgur.com/xbHAxiE.png">
<img src="http://i.imgur.com/uuOwurH.png">
###Tổng hợp các thẻ HTML

| Tag | Description | Version |
|-----|-------------|---------|
|\<!--....-->| Định nghĩa một comment |         |
| <!DOCTYPE> | Định dạng loại tập tin HTML |         |
|\<a>		 | Đường link liên kết |         |
|\<abbr>	 | Định nghĩa một chữ viết tắt hoặc viết tắt |         |  
|\<address>	 | Xác định thông tin tác giả |         |
|\<area>	 | Định nghĩa một khu vực trong Image-map |         |
|\<article>  | Định nghĩa một bài báo | HTML5 |
|\<aside>	 | Xác định nội dung ngoài các nội dung trang | HTML5 |
|\<audio>| Thẻ âm thanh | HTML5 |
|\<b> |	In đậm | HTML5 |
|\<base> | Chỉ định URL/mục tiêu cho tất cả URL tương đối trong tài liệu| |
|\<blockquote>| Định nghĩa một phần được trích từ nguồn khác | |
|\<body>| Thẻ thân tài liệu | |
|\<br> | Xuống dòng | |
|\<button> | Tạo nút bấm | |
|\<canvas> | tạo hình | HTML5 |
|\<caption>| Chú thích bảng | |
|\<code>| Thẻ code | |
|\<col>| Thẻ con của thẻ \<colgroup> | |
|\<colgroup>| Chỉ định một nhóm gồm một hoặc nhiều cột trong một bảng để định dạng | |
|\<datalist>| Chỉ định một danh sách các tùy chọn | HTLM5 |
|\<dd>| Description List | |
|\<del>| Gạch ngang chữ | |
|\<details>| Xác định các chi tiết khác mà người dùng có thể xem hoặc ẩn | |
|\<dialog>| Xác định một hộp thoại hoặc cửa sổ | HTML5 |
|\<div>| Xác định một phần trong tài liệu | |
|\<form>| Xác định một form HTML cho người dùng nhập vào| |
|\<fieldset>| Xác định nội dung khép kín | |
|\<figure>| Tạo nội dung khép kín như hình minh họa, biểu đồ, hình ảnh | HTML5 | 
|\<figcaption>|Tạo chú thích cho thẻ \<figure>| HTML5 |
|\<footer>| Phần cuối của một trang hoặc một khu vực trang| HTML5 |
|\<header>| Phần đầu của trang hoặc khu vực trong trang | HTML5 |
|\<h1>to\<h6>| Kích thước chữ tiêu đề | | 
|\<head>| Xác định các thông tin về tài liệu | |
|\<header>| Tiêu đề HTML | |
|\<hr> | Đường kẻ ngang | |
|\<html>| Xác định tài liệu HTML | |
|\<i>| In nghiêng | |
|\<iframe>| Đinh nghĩa khung nội tuyến | |
|\<img>| Thẻ chèn ảnh | |
|\<input>| Trường nhập dữ liệu | |
|\<legend>| Xác định chú thích cho thẻ \<fieldset> | |
|\<li>| Xác định danh sách item | |
|\<link>| Xác định mỗi quan hệ giữa một tài liệu HTML với nguồn bên ngoài | |
|\<main>| Xác định nội dung chính của một tài liệu | HTML5 |
|\<map>| xác định image-map của khách ||
|\<mark>| Highlight | HTML5 |
|\<menu>| ĐỊnh nghĩa danh sách, menu các lệnh | |
|\<menuitem>| Định nghĩa một lệnh, menu các item mà người dùng có thể gọi từ một menu popup | HTML5 |
|\<meta>| Thẻ khai báo siêu dữ liệu | |
|\<nav>| xác định khối điều hướng | HTML5 |
|\<object>| Đối tượng nhúng ||
|\<ol>| Ordered List ||
|\<option>| Tùy chọn của danh sách xổ ||
|\<output>| Xác định kết quả của một phép tính ||
|\<p>| Thẻ văn bản ||
|\<pre>| Thẻ định dạng sẵn ||
|\<progress>| Tạo thanh tiến trình | HTML5 |
|\<q>| Xác định một đoan văn ngắn | |
|\<quote>| Thẻ trích dẫn | |
|\<section>| Xác định một phần trong tài liệu | HTML5 |
|\<select>| Tạo danh sách xổ | |
|\<source>| Định nghĩa nhiều nguồn media ||
|\<span>| xác định một phần trong tài liệu | |
|\<strong>| in đậm | |
|\<style>| Xác định thông tin phong cách cho tài liệu | |
|\<summary>| Tạo thẻ tiêu đề cho thẻ \details | HTML5 |
|\<table>| Tạo bảng | |
|\<td>| cột trong bảng | |
|\<textarea>| Vùng văn bản ||
|\<th>| Ô tiêu đề trong bảng | |
|\<title>| Tiêu đề | |
|\<tr>| hàng trong bảng | |
|\<u>| gạch dưới | |
|\<ul>| Unordred List | |
|\<video>| Thẻ video | HTML5 |
