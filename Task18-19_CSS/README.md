#CSS
*Người thực hiện: Hoàng Quốc Cường*

*Tài liệu dựa vào chủ yếu: https://www.thachpham.com*

##Mục lục:
- [1.Cấu trúc của 1 đoạn CSS](#1)
- [2.Nhúng CSS vào website](#2)
- [3.Vùng chọn cơ bản (selector)](#3)
- [4.Đơn vị px, pt, percentages,em và rem](#4)
- [5.CSS Color](#5)
- [6.CSS Backgrounds](#6)
- [7.CSS Borders](#7)
- [8.CSS Margin](#8)
- [9.CSS Padding](#9)
- [10.CSS Outline](#10)
- [11.CSS Text](#11)
- [12.CSS Block and Inline](#12)
- [13.Thẻ div](#13)
- [14.Chia cột với float và clear float](#14)
- [15.Reset CSS](#15)
- [16.Tùy biến list](#16)
- [17.Tùy biến loại phần tử với display](#17)

##Nội dung:

<a name="1"></a>
###1.Cấu trúc của 1 đoạn CSS
<figure>
	<center>
	<img src="https://thachpham.com/wp-content/uploads/2015/04/html-css-webpage.png">
	<figcaption>CSS có vai trò trang trí thêm cho văn bản viết bằng HTML</figcaption>
	</center>
</figure>
- Một đoạn CSS gồm 4 phần:
```
vùng chọn {
	thuộc-tính: giá trị;
	thuộc-tính: giá trị;
	....
```
- Mỗi thuộc tính sẽ luôn có một giá trị riêng, giá trị có thể là dạng số, hoặc các tên giá trị trong danh sách có săn của CSS.
- Mỗi vùng chọn không giới hạn thuộc tính

<a name="2"></a>
###2.Nhúng CSS vào website
**Có hai cách**:
<dl>
	<dt><b>Inline Styles:</b></dt>
	<dd>Nhúng trực tiếp vào tài liệu HTML thông qua cặp thẻ <b>style</b></dd>
	<dd>Thích hợp với việc chèn một vài đoạn CSS ngắn</dd>
	<dd>Trình duyệt không mất thời gian tải tập tin CSS</dd>
	<dt><b>External Styles:</b></dt>
	<dd>Tạo một tập tin .css riêng và nhúng vào tài liệu HTML thông qua cặp thẻ <b>link</b></dd>
	<dd>Thích hợp với việc chèn nhiều đoạn CSS, dễ quản lý</dd>
	<dd>Nhưng trình duyệt sẽ mất thêm thời gian để tải tập tin CSS</dd>
</dl>

- **Cách dùng Inline Styles:**

<img src="http://i.imgur.com/793wBP2.png">
<img src="http://i.imgur.com/wDqblN0.png">

- **Cách dùng External Styles:**

<img src="http://i.imgur.com/CCSZml3.png"> <img src="http://i.imgur.com/mLjo9s0.png">
<img src="http://i.imgur.com/TmwP7gL.png">

- **Note:** Khi sử dụng cách External Styles, thuộc tính src trong thẻ link là đường dẫn chính xác đến thẻ css, rel là khai báo loại tập tin nhúng.

**Nhúng tập tin CSS vào bên trong một tập tin CSS**
- Sử dụng từ khóa **@import**, và các từ khóa này được đặt ở đầu tập tin .css để nhúng tập tin CSS này vào CSS khác.

<a name="3"></a>
###3.Vùng chọn cơ bản (selector)
- Là khu vực mà bạn muốn nó sẽ được áp dụng quy tắc CSS mà bạn chỉ định cho nó.
- Vùng chọn có thể là tên thẻ HTML hoặc thuộc tính của HTML

#####Các loại vùng chọn cơ bản
**Vùng chọn dựa vào tên thẻ**

<img src="http://i.imgur.com/793wBP2.png">
<img src="http://i.imgur.com/wDqblN0.png">
- Như ví dụ trên, ta thay đổi vùng chọn cho thẻ h1, thẻ span

**Vùng chọn dựa vào ID**
- Chọn một phần tử cụ thể dựa vào giá trị của thuộc tính **id** trong thẻ HTML.
- Trên một trang tài liệu HTML, mỗi phần tử phải mang một id riêng biệt không trùng nhau.
- `id="#tên-id"`
- Ví dụ:

<img src="http://i.imgur.com/Twsu5YM.png">
<img src="http://i.imgur.com/Gy1X47c.png">
<img src="http://i.imgur.com/729cUHI.png">

**Vùng chọn dựa vào class**
- Khác với id là chỉ dùng duy nhất cho một phần tử riêng biệt thì class lại có thể được dùng cho nhiều phần tử.
- `class=".tên-class"`
- Ví dụ:

<img src="http://i.imgur.com/p1GIdwP.png">
<img src="http://i.imgur.com/Hw0Wwwo.png">
<img src="http://i.imgur.com/nklxyFT.png">

**Vùng chọn theo thứ cấp**
- Chọn một phần tử con trong phần tử mẹ nào đó
- Sử dụng thêm vùng chọn dựa vào id
- Ví dụ:

<img src="http://i.imgur.com/5RzDR9E.png">
<img src="http://i.imgur.com/k62hc9R.png">
<img src="http://i.imgur.com/iO6VYgp.png">
<img src="http://i.imgur.com/XJzO0nD.png">

**Vùng chọn theo thứ cấp liền nhau**
- Cũng tương tự như vùng chọn thứ cấp, nhưng nó sẽ chỉ áp dụng cho các phần tử nằm dưới nó một bậc
- Ví dụ:

<img src="http://i.imgur.com/8JSS1sW.png">
<img src="http://i.imgur.com/3U4bQ3e.png">
<img src="http://i.imgur.com/C77BJ7p.png">

<a name="4"></a>
###4.Đơn vị px, pt, percentages,em và rem
- Hai loại đơn vị là **Absolute Units**(đơn vị tuyệt đối) và **Relative Units**(Đơn vị tương đối)

#####Absolute Units
- Là đơn vị đã được định nghĩa sẵn và địa diện cho các đơn vị đo lường vật lý. Chúng không phụ thuộc và không hề thay đổi bởi bất cứ tác động nào.
**Các đơn vị tuyệt đối trong CSS:**

- **px**: pixel, là đơn vị được sử dụng trên màn hình hiện thỉ, một px tương ứng với một điểm ảnh trên màn hình hiển thị.
- **pt**: point. Cứ **1 ich = 72pt**

<img src="http://i.imgur.com/qMcKomD.png">

#####Relative Units
- **%**(percentages): Là đơn vị tham chiếu tỉ lệ so với một phần tử mẹ của nó dựa vào kích thước. Ví dụ một bức ảnh có height = 320px thì khi ta đổi nó thành 50%, có nghĩa height = 160px
- **em** là đơn vị tham chiếu tỷ lệ so với phần tử mẹ của nó dựa vào thuộc tính **font-size**.
- **rem** là đơn vị tham chiếu tỷ lệ so với phần tử gốc của một website dựa vào thuộc tính font-size trong thẻ <html>

<img src="http://i.imgur.com/Pu1sjEb.png">
<img src="http://i.imgur.com/ys96hN0.png">

<a name="5"></a>
###5.CSS Color
- Màu sắc trong CSS thường được thể hiện qua 3 cách:

<figure>
	<img src="http://i.imgur.com/nQ2njxd.png">
	<figcaption>Sử dụng tên màu</figcaption>
	<img src="http://i.imgur.com/y6meNNJ.png">
	<figcaption>Sử dụng giá trị RGB</figcaption>
	<img src="http://i.imgur.com/s32IaTg.png">
	<figcaption>Sử dụng giá trị Hex</figcaption>
</figure>

<a name="6"></a>
###6.CSS Backgrounds
- Dùng để tạo các hiệu ứng nền

<ul>
	<li>Tính chất của CSS Background</li>
	<ul>
		<li>background-color: Dùng màu sắc làm hiệu ứng nền</li>
		<li>background-image: Dùng hình ảnh làm hiệu ứng nền </li>
		<li>background-repeat: Thiết lập để ảnh nền được lặp lại</li>
		<li>background-attachment: Đặt một ảnh nên cố định hoặc cuộn với phần còn lại của trang</li>
		<li>background-position: Đặt vị trí ban đầu của ảnh nền</li>
	</ul>
</ul>

<a name="7"></a>
###7.CSS Borders:
- Dùng để định dạng đường viền cho thành phần

| Thuộc tính | Mô tả |
|------------|-------|
|border-color|Xác định màu sắc đường viền|
|border-style|Xác định kiểu đường viền|
|border-width|Xác định bề dày đường viền|

<img src="http://i.imgur.com/nDH9S71.png">

<a name="8"></a>
###8.CSS Margin
- Dùng để canh lề cho thành phần

<img src="http://i.imgur.com/u4cGrQ2.png">
- Thuộc tính margin ở trong hình trên là tổng hợp của các thuộc tính margin-top, margin-right, margin-left, margin-bottom.

<a name="9"></a>
###9.CSS Padding
- Dùng để thêm vào khoảng không cho thành phần 

<img src="http://i.imgur.com/alWQpfq.png">
- Tương tự như margin, thuộc tính padding tổng hợp các thuộc tích padding-top, padding-right, padding-top, padding-bottom.

<a name="10"></a>
###10.CSS Outline
- Định dạng các đường viền bao ngoài

<img src="http://i.imgur.com/QvDCpiH.png">

<a name="11"></a>
###11.CSS Text
<dl>
	<dt>text-align:</dt>
	<dd>Dùng để căn lề văn bản</dd>
	<dt>text-decoration</dt>
	<dd>Trang trí lại văn bản hiển thị trên tài liệu theo một số kiểu nhất định</dd>
	<dd>overline(gạch trên chữ), underline(gạch dưới chữ), line-through(gạch ngang chữ),none</dd>
	<dd>Có thể gộp chung tất cả các kiểu trên</dd>
	<dt>text-indent:</dt> 
	<dd>Tạo khoảng trắng bên trái của văn bản</dd>
	<dt>text-shadow:</dt>
	<dd>Tạo đổ bóng cho văn bản</dd>
	<dt>text-transform:</dt>
	<dd>Tùy chỉnh chữ thành in hoa, hoặc in thường</dd>
	<dt>font-family</dt>
	<dd>Kiểu font</dd>
	<dt>font-size</dt>
	<dd>Kích thước chữ</dd>
	<dt>color</dt>
	<dd>Màu chữ</dd>
</dl>

<a name="12"></a>
###12.CSS Block and Inline
- Block là thuật chỉ chung các thẻ HTML có chức năng tạo một khu vực (khối). Khối này có nghĩa là một thẻ khi mà bạn khai báo thì nó sẽ hiển thị ở mỗi dòng riêng biệt, giống như \<p>, \<ul>, \<li>, ... bên HTML.
- Inline là thuật ngữ chỉ chung các thẻ HTML khi mà khai báo nội dung thì nó vẫn sẽ nằm chung một dòng với các văn bản khác: \<b>, \<span>, \<i>, ....

<a name="13"></a>
###13.Thẻ div
- Thẻ \<div>(divison) được sử dụng để tạo ra một khu vực kiểu block nào đó trên một website hay bạn có thể hiểu là gom nhóm tập hợp các phần tử trên website vào một khu vực

<a name="14"></a>
###14.Chia cột với float và clear float

Chia cột trong CSS là việc thiết lập những phần tử con trong một phần tử mẹ nằm trên cùng một hàng

Các bước chia cột trong CSS

<ol>
	<li>Các cột luôn phải có một container(div), tức là phần tử mẹ bao bọc nó</li>
	<li>Thiết lập chiều rộng cho container</li>
	<li>Thiết lập cho chiều rộng cho hai cột, tổng chiều rộng trong hai cột phải luôn bằng hoặc ít hơn chiều rộng của container</li>
	<li>Nên sử dụng box-sizing: border-box để tính toán kích thước chính xác</li>
	<li>Sử dụng thuộc tính float với giá trị left và right để đẩy phần tử sang trái hoặc phải</li>
	<li>Tiến hành clear float</li>
</ol>

Cách chia cột trong CSS

<img src="http://i.imgur.com/dshsg7U.png">
- Bên cạnh đó, ta cần tính toán kích thước sao để chia cho chợp lý.

Clear float:
- Như hình trên, hai khối left và right đã ra khỏi khối container, để khác phục được điều đó, ta sử dụng cách đơn giản nhất là thêm `overflow:auto` cho container.
<img src="http://i.imgur.com/5N08rYd.png">
- Ngoài ra, ta có thẻ sử dụng thẻ \<div> rỗng

<a name="15"></a>
###15.Reset CSS
- Để đồng bộ CSS trên các trình duyệt khác nhau
- Cách reset CSS:

Trước:
<img src="http://i.imgur.com/b0LPGSi.png">
<img src="http://i.imgur.com/5S13CRT.png">

Sau:
<img src="http://i.imgur.com/FMbIFl9.png">
<img src="http://i.imgur.com/OffUx9O.png">

- Ngoài ra, có thể sử dụng bộ reset css thông dụng như [normalize.css](https://github.com/necolas/normalize.css/blob/master/normalize.css) hoặc [Reset CSS 2.0 by Eric Meyer](http://meyerweb.com/eric/tools/css/reset/).

<a name="16"></a>
###16.Tùy biến list
- Tùy biến bằng cách sử dụng thuộc tính list-style.
- 3 thuộc tính con của list-style:
<ul>
	<li>list-style-type: Thay đổi loại hiển thị của danh sách</li>
	<li>list-style-position: Tùy chỉnh vị trí hiển thị các dấu đầu dòng của mục con nằm bên trong hoặc ngoài danh sách</li>
	<li>list-style-image: Sử dụng hình ảnh làm các dấu đầu dòng</li>
</ul>

<a name="17"></a>
###17.Tùy biến loại phần tử với display

<dl>
	<dt>Thuộc tính display có một số giá trị cơ bản như:</dt>
	<dd>inline: Chuyển phần tử về hiển thị trên cùng một hàng</dd>
	<dd>inline-block: Chuyển phần tử về hiển thị trên cùng một hàng nhưng nó vẫn thừa hưởng các đặc tính của block như có thể tùy chỉnh kích thước, thêm background,...</dd>
	<dd>block: Chuyển phần tử về hiển thị kiểu block, sở hữu một hàng riêng</dd>
	<dd>list-item: Chuyển phần tử về hiển thị như một danh sách, để có thể sử dụng thuộc tính list-style</dd>
	<dd>none: Ẩn phần tử đó đi không cho hiển thị nữa.</dd>
</dl>