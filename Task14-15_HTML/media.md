#Chèn tập tin kỹ thuật số vào web
**Note**: Các tập tin kỹ thuật số được chèn vào phải có đường dẫn tuyệt đối dẫn trực tiếp đến tập tin đó.

####Chèn ảnh vào HTML
- Sử dụng thẻ **\<img>**
```
<img src = "link ảnh" title = "tiêu đề ảnh" alt="abc" />
```
		- src: đường dẫn đến tập tin hình ảnh
		- title: Tiêu đề của hình ảnh
		- alt: Tên định danh của hình ảnh

- Ngoài ra còn có các thuộc tính khác như width, height để thay đổi kích thước hiển thị ảnh

####Chèn video
- Sử dụng thẻ **\<video>\</video>** trong HTML5
```
<video width = "322" height = "322" controls>
	<source src = "link-video" type = "video/mp4"
</video
```
- Thẻ <source> trong cặp thẻ <video></video> với các thuộc tính nhắm khai báo đường dẫn tập tin video và loại tập tin.
- **Note**: Để đảm bảo tất cả các trình duyệt có thể đọc được, chỉ nên chèn video định dạng MP4

####Chèn âm thanh - nhạc
- Sử dụng cặp thẻ <audio> trong HTML5
- Tương tự như thẻ <video>

####Chèn đối tượng kỹ thuật với thẻ <object>
- Chèn các loại đối tượng số như Flash, Java, Audio, Video, PDF, ActiveX.

####Nhúng tài liệu HTML vào web
- Dùng thẻ **\<iframe>** để nhúng thẳng một trang nào đó vào tài liệu HTML
```
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ei2GAs444J4" frameborder="0" allowfullscreen></iframe>
```
- **src**: là đường dẫn của trang nhúng vào
- **width, height**: là kích thước của khung hiển thị(gọi là frame)
- Ngoài ra, có thể sử dụng thuộc tính **name** trong thẻ **\<iframe>** và thuộc tính **target** trong thẻ **<a>**

[README](https://github.com/TotoroC/web_dev/blob/master/Task14_HTML/README.md)