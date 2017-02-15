#TÌm hiểu về markdown
<p>Tên tài liệu: Tìm hiểu về markdown,github</p>
<p>Thực hiện: Hoàng Quôc Cường</p>
##Mục lục:
- [Github là gì? Dùng để làm gì ?](#github)
- [Tạo Respository](#respository)
- [Markdown là gì?  Dùng để làm gì ? Các cú pháp cơ bản thường gặp](#markdown)
- [Cài đặt Sublime Text  và cài đặt các công cụ hỗ trợ markdown](#sublime)
- [Các công cụ viết markdown khác](#congcukhac)

##Nội dung:
<a name = "github"></a>
###1.Github là gì ? DÙng để làm gì?
<p><b>Github</b>  là một dịch vụ lưu trữ dựa trên web cho các dự án phát triển phần mềm trong đó sử dụng các hệ thống kiểm soát phiên bản Git</p>
<p><b>Github</b> dùng để lưu trữ, chia sẻ các source code của cá nhân </p>
<a name = "respository"></a>
###2.Tạo Respository
<p>Đầu tiên, Bạn cần đăng nhập vào trang github cá nhận của bạn, và sau đó trên màn hình nó sẽ xuất hiện hình như sau:</p>
<img src = "http://i.imgur.com/bexnITn.png">
<p>Sau đó, nhấn chọn Start a Project để bắt đầu tạo Responsitory. Sau khi nhấn, nó sẽ hiện thị ra như sau:</p>
<img src = "http://i.imgur.com/X8YVTxX.jpg">
<p>Ở trong ô <b>Responsitory Name</b> bạn đặt tên cho Responsitory của bạn. Ngoài ra bạn có thể mô tả Responsitory bằng cách điền vào ô <b>Description</b> và lựa chọn public
hay private cho Responsitory của bạn. </p>
<p>Lưu ý: Các bạn nên tích vào <b>Initialize this repository with a README </b> để tự động tạo file README.md trong Responsitory bạn tạo. Chúc các bạn thành công!</p>
<a name = "markdown"></a>
###3.Markdown  là gì ? Dùng để làm gì ? Các cú pháp cơ bản.
<ol>
<li>Markdown là gì?</li> 
<p><b>Markdown</b> là một ngôn ngữ đánh dấu với cú pháp văn bản thô, được thiết kế để có thể dễ dàng chuyển thành HTML và nhiều định dạng khác sử dụng một công cụ cùng tên.</p>
<li>Dùng để làm gì</li>
<p><b>Markdown</b> thường được dùng dể tạo các tập tin README, viết tin nhắn trên các diễn đàn, và tạo văn bản có định dạng bằng một trình biên tập thô.</p>
<li>Các cú pháp cơ bản</li>
</ol>
Để tạo bảng, chúng ta làm như sau:
```
|Cú pháp|Công dụng|
|-------|---------|
|#Tiêu đề| Tiêu đề cấp 1|
|##Tiêu đề| Tiêu đề cấp 2|
|###Tiêu đề | Tiêu đề cấp 3|
|**in đậm**| In đậm |
|*in nghiêng*| in nghiêng|
|`Chú thích`|Trích dẫn|
```
Kết quả là:

|Cú pháp|Công dụng|
|-------|---------|
|#Tiêu đề| Tiêu đề cấp 1|
|##Tiêu đề| Tiêu đề cấp 2|
|###Tiêu đề | Tiêu đề cấp 3|
|**in đậm**| In đậm |
|*in nghiêng*| in nghiêng|
|`Chú thích`|Trích dẫn|

<p><b>Lưu ý:</b>Sô dấu <b>-</b> phải bằng với số ký tự trong mỗi <b>| |</b></p>
#Tiêu đề cấp 1:

- Cú pháp: #ten_tieu_de

##Tiêu đề cấp 2:

- Cú pháp: ##ten_tieu_de

###Tiêu đề cấp 3:

- Cú pháp: ###ten_tieu_de

Ngoài ra còn có nhiều cấp tiêu đề khác, cấp tiêu đề thứ n với n dấu # ( với n từ 1-> 6)

**In đậm**

-  Cú pháp: `**từ , cụm từ hoặc câu**`

*in nghiêng* 

- Cú pháp: `*từ, cụm từ hoặc câu*`

**Để chèn ảnh, ta làm như sau:**

- Cú pháp: `<img src = "link anh cua ban">`

**Để chèn đường link, ta có thể dán trực tiếp đường link đó, hoặc dùng từ, cụm từ, câu để trỏ đến đường link**

- Cú pháp: `[ từ bạn muốn dùng để trỏ ](http://)`

<b>Trích dẫn, làm nổi bật ý từ, câu ta có hai cách đó là dùng với 2 dấu \` để làm nổi bật 1 câu, 1 từ. Còn nếu bạn muốn nhiều dòng, thì dùng 6 dấu \` </b>

- Cú pháp: \`từ,câu\`
- Cú pháp: \```đoạn văn bản \```

<b>Để thụt đầu dòng, bạn sử dụng dấu - ở trước câu mà bạn muốn thụt đầu dòng:</b>

- Cú pháp: ` - Đoạn cần thụt `

Ngoài ra còn có các cú pháp khác, bạn có thể nó tại [đây](http://daringfireball.net/projects/markdown/syntax)
<a name = "sublime"></a>
###4.Cài đặt Sublime Text và các công cụ hỗ trợ markdown
<ul>
	<li><h4>Cài đặt Sublime  Text</h4></li>
	<p>Đầu tiên, ta vào trang chủ https://www.sublimetext.com và nó sẽ hiện ra như hình dưới đây: </p>
	<img src = "http://i.imgur.com/nCShxC6.jpg">
	<p>Sau đó, kéo xuống và chọn Download sao cho phù hợp với phiên bản hệ điều hành hiện tại mà bạn đang dùng. VÌ mình dùng ubuntu nên mình sẽ chọn phiên bản cho Ubuntu</p>
	<img src = "http://i.imgur.com/Z422yuJ.jpg">
	<p>Khi tải về, bạn được 1 file .deb như trong hình:</p>
	<img src = "http://i.imgur.com/hGXayQQ.jpg">
	<p>TIếp theo, bạn mở cửa sổ Terminal bằng cách ấn tổ hợp phím <b>Ctrl Alt T</b>. Sau khi cửa sổ Terminal hiện ra, thông thường khi tải về, file sẽ được lưu vào thư mục Downloads, nên ta sẽ truy cập vào thư mục đó bằng lệnh <b>cd Downloads</b>và dùng lệnh <b>ls</b> để hiện thị tất cả các file có trong thư mục Download.</p>
	<img src = "http://i.imgur.com/UInPaoW.jpg">
	<p>Để cài đặt file .deb, ta dùng câu lệnh <b>sudo dpkg -i filename.deb</b>. Ở đây, ta tải về được file <b>sublime-text_build-3126_amd64.deb</b> nên ta dùng câu lệnh <b>sudo dpkg - i sublime-text_build-3126_amd64.deb</b>. Cuối cùng ta dùng câu lệnh `sudo apt-get update`</p>
	<img src = "http://i.imgur.com/iMW1am8.jpg">
	<p>Cuối cùng, bạn khu vực tìm kiếm bằng cách bấm <b>Super(phím windown trên bàn phím)</b> và tìm kiếm với từ khóa Sublime.</p> 
	<img src = "http://i.imgur.com/lyiHjyi.jpg">
	<p>Vậy là đã hoàn thành, chúc các bạn thành công!</p>
  <img src = "http://i.imgur.com/PtVgL2B.png">
  <li><h4>Các công cụ hỗ trợ markdown</h4></li>
  <p>Trước khi cài đặt các công cụ hỗ trợ markdown trong <b>Sublime Text</b> như <b>ExportHTML, MarkdownPreview,...</b> thì ta cần phải cài đặt <b>Package Control</b> cho Sublime Text bằng cách như sau:</p>
  <ul>
  <li><p>Ta khởi động Sublime Text lên và nhấn tổ hợp phím <b>Crt `</b> để nó hiện ra cửa sổ console như sau: </p><li>
  <img src = "http://i.imgur.com/WZI8rmB.jpg">
  <p>Vì mình xài Sublime Text 3 nên mình sẽ sử dụng đoạn mã sau để điền vào cửa sổ console:</p>
  <p><b>import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by) </b></p>
  <p>Vậy là đã hoàn thành bước cài đặt Package Control.</p>
  </ul>
  <p>Sau khi cài xong Package Control, để cài các công cụ hỗ trợ, ta làm vào như sau:</p>
  <ul>
  <li><p>Bước 1: Ta chọn Preferences --> Package Control (nằm trên thanh công cụ)</p></li>
  <img src = "http://i.imgur.com/DuqfyPI.jpg">
  <li><p>Bước 2: Ta tìm và chọn Install Package trong Packet Control<p></li>
  <li><p>Bước 3: Nó hiện ra khung Install Package, và giờ ta chỉ cần tìm và chọn các công cụ mà ta muốn cái đặt thôi, tiến trình cài đặt các công cụ là tự động.!. Chúc bạn thành công!</p></li>
  <img src = "http://i.imgur.com/HMQY5bA.jpg">
  <img src = "http://i.imgur.com/Jqzpp9S.jpg">
  <img src = "http://i.imgur.com/KZwoMxI.jpg">
  </ul>
<a name = "congcukhac"></a>
###5.Các công cụ viết markdown khác.
<p>Ngoài Sublime Text như mình đã nêu trên, còn có nhiều công cụ khác. Ở đây mình sẽ giới thiệu sơ qua 3 công cụ liên quan đến markdown</p>
[Stackedit](https://stackedit.io/editor)
<img src = "http://i.imgur.com/quJ7bkv.jpg">
[Markdown Editor](http://jbt.github.io/markdown-editor)
<img src = "http://i.imgur.com/IO97ULq.jpg">
[Markdown Tables Generator](http://www.tablesgenerator.com/markdown_tables)
<img src = "http://i.imgur.com/C0UwY5T.jpg">
<p>Nhìn chung, về mặt cơ bản thì 2 công cụ Stackedit và Markdown Editor tương đối giống nhau về cách hoạt động. Chúng đều là các công cụ viết markdown online.
Tuy vậy, đối ngược với giao diện đơn gianr của Markdown Editor thì giao diện của Stackedit khá là bắt mắt, ngoài ra nó có tích hợp thêm một số tính năng như :
<b>Chia sẻ, đồng bộ hóa với cloud, public, chuyển đổi HTML thành Markdown,...</b>. Các bạn có thể tự lựa chọn cho mình những công cụ mà mình thích nhất.</p>
<p>Còn về Markdown Tables Generator, nó là một công cụ khá hay để tạo bảng, giúp bạn có thể tạo bảng một cách dễ dàng nhanh chóng bằng cách tự lưa chọn cho mình 
một bảng với số hàng, số cột tùy ý rồi bấm <b>Generate</b> nó sẽ xuất ra cho bạn các dòng lệnh markdown, bạn chỉ cần copy + paste vào trình markdown của bạn là có thể
sử dụng được. Chúc bạn vui vẻ và thành công!</p>
