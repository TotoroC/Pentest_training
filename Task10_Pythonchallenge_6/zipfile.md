##ZipFile Objects
**zipfile.ZipFile(file[,mode[,compression[,allowZip64]]])** 
- Mở một file ZIP, đây là nơi mà file có thể hoặc là một đường dẫn đến một tập tin (một chuỗi) hoặc là một đối tượng như tập file. Tham số **mode** nên là 'r' để đọc một file có sẵn, 'w' để cắt bớt và ghi một file mới, hoặc 'a' để thêm vào một file có sẵn. Nếu **mode** là 'a' and file dùng để chỉ một tập tin ZIP hiện có, thì sau đó tập tin bổ sung được thêm vào nó. Nếu file không ám chỉ một tập tin ZIP, thì một kho [archive] ZIP lưu trữ mới được thêm vào tập tin. Điều này đồng nghĩa với việc thêm một kho ZIP lưu trữ vào một file khác (như python.exe)
- **compression** là một phương thức nén ZIP được sử dụng khi viết kho lưu trữ, và nên là **ZIP_STORED** hoặc **ZIP_DEFLATED**; giá trị không được xác định sẽ khiến RuntimeError được bật lên. Nếu ZIP_DEFLATED được chỉ định nhưng module zlib không có sẵn, RuntimeError cũng được bật lên. Mặc định là ZIP_STORED. Nếu **allowZip64** là đúng, zipfile sẽ tạo ra các file ZIP sử dụng các phần mở rộng ZIP64 khi zipfile lớn hơn 2GB. Nếu nó là sai (mặc định) zipfile sẽ bật một ngoại lệ khi zipfile yêu cầu các phần mở rộng ZIP64. Các phần mở rộng được tắt theo mặc định bởi các lệnh zip và unzip mặc định trên Unix không hỗ trợ những phần mở rộng này.

**ZipFile.close()**
- Đóng một file lưu trữ. Bạn phải gọi close() trước khi thoát khỏi chương trình nếu không thì những ghi chép quan trọng sẽ không được ghi 

**ZipFile.getinfo(name)**
- Trả lại một đối tượng ZipInfo với thông tin về tên thành viên kho lưu trữ. Gọi getinfo() cho một tên hiện đang không được chứa trong kho lưu trữ sẽ khiến **KeyError** bật lên

**ZipFile.infolist()**
- Trả lại một danh sách chứa mỗi đối tượng ZipInfo cho mỗi thanh viên thuộc kho lưu trữ. Các đối tượng được xếp theo thứ tự giống với thông tin đầu vào của chúng ở trong file ZIP thực trên ổ cứng nếu một kho lưu trữ hiện có đã được mở ra.

**ZipFile.namelist()**
- Trả lại một danh sách các thành viên kho lưu trữ theo tên.

**ZipFile.open(name[,mode[,pwd]])**
- Lấy ra một thành viên từ kho lưu trữ như là một đối tượng giống file (ZipExtFile). **name** là tên của file trong kho lưu trữ hoặc một đối tượng **ZipInfo**. Tham số **mode**, nếu có, phải là một trong những cái sau: 'r' (mặc định), 'U', hoặc 'rU'. Chọn 'U' hoặc 'rU' sẽ cho phép hỗ trợ xuống dòng trong đối tượng read-only.
- **pwd** là password được sử dụng cho các file được mã hóa. Gọi open() trên một ZipFile được đóng sẽ bật RuntimeError
Note:
- Một đối tượng giống file là read_only và cung cấp những phương thức sau: read(), readline(), readlines(), __iter__(), next().
- Nếu ZipFile được tạo ra đi qua một đối tượng giống tập tin như là đối số đầu tiên để đến hàm tạo [constructor], sau đó, đối tượng được open() trả lại sẽ chia sẻ con trỏ tập tin của ZipFile. Trong hoàn cảnh này, đối tượng được open() trả về không nên được sử dụng sau khi có bất kỳ hoạt động bổ sung được thực hiện trên đối tượng ZipFile. Nếu ZipFIle được tạo ra bằng cách đi qua một chuỗi (filename/ tên file) như một đối số đầu tiên để đến hàm tạo, sau đó open() sẽ tạo ra một đối tượng file mới mà được tổ chức bởi ZipExtFile. Để cho phép nó hoạt động độc lập.
- Các phương thức open(), read() và extract() có thể nhận một tên file hoặc một đối tượng ZipInfo. Bạn sẽ biết rõ điều này khi cố gắng đọc một file Zip có chứa các thành viên với tên trùng lặp

**ZipFile.extract(member[,path[,pwd]])**
- Lấy ra một thành viên từ kho lưu trữ vào thư mục làm việc hiện hành, **member** phải là tên đầy đủ của nó hoặc là một đối tượng ZipInfo. Thông tin tập tin đó được lấy ra càng chính xác càng tôt. **path** chỉ định một thư mục khác để giải nén vào. **member** có thể là tên tập tin hoặc một đối tượng ZipInfo. **pwd** là password được sử dụng cho file mã hóa.
- Trả lại đường dẫn bình thường được tạo ra (một thư mục hoặc một file mới)

**ZipFile.extractall([path[,member[,pwd]]])**
- Giải nén tất cả các thành viên từ kho lưu trữ đến thư mục thực thi hiện hành. **path** chỉ định một thứ mục khác để giải nén. **member** là tùy chọn và phải là một tập hợp con của danh sách được trả về bởi namelist(). **pwd** là password được sử dụng cho file mã hóa

**ZipFile.printdir()**
- In một bảng nội dung cho kho lưu trữ đến *sys.stdout*

**ZipFile.setpassword(pwd)**
- Đặt **pwd** như password mặc định để lấy các file được mã hõa

**ZipFile.read(name[,pwd])
- Trả lại các byte của tên file trong kho lưu trữ. **name** là tên của file trong kho lưu trữ, hoặc một đối tượng ZipInfo. Kho lưu trữ phải mở để đọc hoặc nối thêm. **pwd** là password đực sử dụng cho file mã hóa và, nếu được chỉ định, nó sẽ ghi đè lên password mặc định được thiết lập với **setpassword()**. Gọi read() trên một ZipFile đã đóng sẽ bật một RuntimeError

**ZipFile.testzip()**
- Đọc tất cả các file trong kho lưu trữ và kiểm tra CRC của chúng và các file header [đầu mục file]. Trả lại tên cùa file lỗi đầu tiên hoặc nếu không thì trả lại None. Gọi textzip() trên một ZipFile được đóng sẽ bật một RuntimeError

**ZipFile.write(filename[,arcname[,compress_type]])**
- Ghi một file được đặt tên là filename đến kho lưu trữ, đưa nó một cái tên lưu trữ gọi là **arcname** (theo mặc định, điều này giống như filename, nhưng không có một ký tự ổ đĩa và có giải phân cách đường dẫn được gỡ bỏ). Nếu được thì **compress_type** ghi đè giá trị cho tham số compression đến hàm tạo cho mục mới. Kho lưu trữ phải mở ra với chế độ w hoặc a – yêu cầu write() cho một ZipFile được tạo ra với chế độ r sẽ khiến RuntimeError bật lên. Yêu cầu write() cho một ZipFile đóng sẽ khiến RuntimeError bật.

ZipFile.comment
- Nội dung bình luận được gắn liền với file ZIP. Nếu ấn định bình luận cho một đối tượng Zipfile được tạo ra với chế độ a hoặc w, đây có thể là chuỗi không dài hơn 65535 bytes. Những bình luận dài hơn vậy sẽ được cắt bớt trong kho lưu trữ bằng chữ viết khi close() được yêu cầu.