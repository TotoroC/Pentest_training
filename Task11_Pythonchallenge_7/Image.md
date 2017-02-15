#Image Module
- Module Image cung cấp 1 lớp với têm tương tự được sử dụng để đại diện cho một PIL image. Module cũng cung cấp một số hàm, bao gồm các hàm load ảnh từ các file và tạo các file ảnh mới.

##Functions
**Image.new(mode,size,color)**
- Tạo một ảnh mới với mode và size nhất định. Size được cho là một (chiều rộng, chiều cao), trong pixels. Color được cho là một giá trị duy nhất cho hình ảnh đơn băng tần và một bộ cho hình ảnh đa băng tần ( với giá trị cho mỗi băng).

**Image.open(file,mode)**
- Mở và xác định cho một file ảnh. Nếu đối số mode được cho, nó phải là 'r'
- Có thể sử dụng một chuỗi hoặc một đối tượng như một đối số file.
- Trong trường hợp sau, đối tượng file phải thực hiện các phương thức read, seek, tell và được mở trong chế độ nhị phân.

**Image.blend(image1,image2,alpha)**
- Tạo một hình ảnh mới bằng cách nội suy giữa các hình ảnh nhất định, sử dụng số alpha không đổi. Cả hai hình ảnh phải có kích thước và cùng một chế độ.
	out = image1 * (1.0 - alpha) + image2 * alpha
- Nếu alpha là 0.0, một bản sao chép của hình ảnh đâu tiên được trả lại. Nếu alpha là 1, một bản sao chép thứ 2 được trả lại. Nếu cần thiết, kết quả được cắt để phù hợp với phạm vi cho phép.

**Image.composite(image1, image2, mask)**
- Tạo một hình ảnh mới bằng cách nội suy giữa các hình ảnh, sử dụng các điểm ảnh tương ứng từ hình ảnh mặt nạ như alpha. Mask có thể là chế độ '1','L', hoặc 'RGBA'. Tất cả hình ảnh phải có cùng kích thước

**Image.eval(image,function)**
- Áp dụng hàm ( mà nó nên nhận một đối số) cho mỗi điểm ảnh trong hình ảnh nhất định. Nếu hình ảnh có nhiều hơn một 

**Image.frombuffer(mode,size,data)**
- Tạo một bộ nhớ hình ảnh từ dữ liệu pixel trong một chuỗi hoặc đối tượng vùng đệm, sử dụng bộ giải mã chuẩn "raw".
- Không phải tất cả các mode đều có thể chia sẻ bộ nhớ, các mode được hỗ trợ bao gồm "L","RGBX","RGBA","CMYK".
- Mở rộng: **Image.frombuffer(mode, size, data, decoder, parameters**

**Image.fromstring(mode,size,data)**
**Image.fromstring(mode,size,data,decoder,parameters)
- Tạo một bộ nhớ hình ảnh từ dữ liệu pixel trong một chỗi, sử dụng bộ giải mã chuẩn "raw"
- Lưu ý rằng hàm này giả mã dữ liệu pixel duy nhất, không phải toàn bộ ảnh. Nếu bạn có cả một file anh trong một chuỗi, bọc nó trong một đối tượng StringIO, và sử dụng open để tải nó

**Image.merge(mode,bands)**
- Tạo một hình ảnh mới từ một số băng thông hình ảnh duy nhất. Các băng thông này được cho là một tuple hoặc list của các hình ảnh, một trong mỗi băng thông được mô tổ bởi chế độ. Tất cả band phải có cùng kích thước

##Methods
**im.convert(mode)**
- Chuyển đổi một hình ảnh sang mode khác và trả hình mới.
- Khi chuyển đổi từ một bảng màu hình ảnh, điều này chuyển các pixel thông quả bảng màu. Nếu mode được bỏ qua, một mode được chọn sao cho tất cả thông tin trong hình ảnh và trong bảng màu có thể được biểu diễn mà không có bảng màu.

**im.convert("P",**options)**
- Tương tự nhưng cung cấp điều khiển tốt hơn khi đang chuyển đổi một ảnh "RGB" sang một hình ảnh 8-bit. options sắn có:
- **dither**=. Điều khiển khối màu
- **palette**=. Điều khiển hệ bảng. Mặc định là WEB
- **colors**=. Điều khiển một số màu được sử dụng cho bảng khi **palette** là **ADAPTIVE**

**imconver(mode,matrix)**
- Chuyển đổi một ảnh "RGB" sang "L" hoặc "RGB" sử dụng một ma trận chuyển đổi. Ma trận là 4 hoặc 16 tuple

**im.copy(box)**
- Sao chép một hình ảnh

**im.crop(box)**
- Trở lại một bản sao khu vực hình chữ nhật từ hình ảnh hiện tại.  
**im.draft(mode,size)**
- Cấu hình bộ nạp file ảnh sao cho nó trả về một phiên bản của ảnh càng chặt chẽ có thể phù hợp với mode và size nhất định.
- Phương pháp này thay đổi đối tượng hình ảnh tại chỗ

**im.filter(filter)**
- Trả về một bản copy của một hình ảnh được lọc bởi bộ lọc nhất định.

**im.fromstring(data,decoder,parameters)**
- Tương tự như hàm fromstring, nhưng tải dữ liệu vào hình ảnh hiện tại.

**im.getbands()**
- Trả lại một tupe chứa tên mỗi băng

**im.getbbox()**
- Tính toán khung giới hạn của các vùng trống trong hình ảnh. Trả về **None** nếu hình ảnh hoàn toàn trống.

**im.getcolors(maxcolors)**
- Trả lại một danh sách không sắp xếp (count,color) của tuples, count là số lần tương ứng xảy ra trong hình ảnh.

**im.getdata()**
- TRả lại nôi dung của một hình ảnh như một đối tượng chuỗi có chứa các giá trị pixel
- Đối tượng chuỗi trả về bởi phương pháp này là một kiểu dữ liệu PIL nội bộ, mà chỉ hỗ trợ các hoạt động trình tự nhất định, bao gồm sự lặp lại và truy cập tuần tự cơ bản.

**im.getextrema()**
- Trả lại một 2-tuple chứa các giá trị tối thiểu và tối đa của hình ảnh.

**im.getpixel(xy)**
- Trả về pixel tại vị trí nhất định. Nếu hình ảnh là một hình ảnh đa lớp , phương pháp này trả về một tuple

**im.histogram()**
- Trả về một biểu đồ cho hình ảnh. Các biểu đồ được trả về là một danh sách các count pixel, một trong mỗi giá trị pixel trong hình ảnh nguồn.

**im.histogram(mask)**
- Trả về một biểu đồ cho các phần của hình ảnh mà hình ảnh mặt nạ khác không.

**im.load()**
- Phân bố lưu trữ hình ảnh và tải nó từ tập tin.

**im.offset(xoffset,yoffset)**
- Trả lại một bản sao hình ảnh nơi mà dữ liệu đã được bù đắp bởi những khoảng cách nhất định.

**im.paste(image,box)**
- Dán hình ảnh khác vào hình ảnh này

**im.paste(colour,box)**
- Tương tự ở trên, nhưng lấp đầy khu vực với một màu duy nhất.

**im.paste(image,box,mask)**
- Tương tự như trên nhưng chỉ cập nhật các vùng nếu bởi mask

**im.paste(colour,box,mask)**
- Tương tự như trên, nhưng lấp đầy khu vực được chỉ định bởi mask với một màu nhất định

**im.point(table)**
**im.point(function)**
- Trả về một bản sao của hình ảnh mà mỗi pixel được ánh xạ thông qua các bảng tra cưu nhất định.

**im.point(table,mode)**
**im.point(function,mode)** 
- Tương tự như trên nhưng chỉ định một chế độ mới cho đầu ra hình ảnh

**im.putalpha(band)**
- Sao chép các band cho đến lớp alpha của hình ảnh hiện tại

**im.putdata(data)**
**im.putdata(data,scale,offset)**
- Sao chép lại các giá trị pixel từ một chuỗi hình thành đối tượng trong hình ảnh, bắt đầu từ góc trên bên trái (0,0).

**im.putpalette(sequence)**
- Đính kèm một bảng với một "P" hoặc "L" hình ảnh.

**im.putpixel(xy,colour)**
- Sửa đổi các điểm ảnh ở các vị trí nhất định.

**im.quantize(colors,**option)**
- Chuyển đổi một "L" hoặc "RGB" hình ảnh vào một "P" hình ảnh với số lượng các màu sắc nhất định và trả về hình ảnh mới.

**im.resize(size,filter)**
- Trả lại một bản sao thay đổi kích cỡ của hình ảnh.

**im.rotate(angle,filter=NEAREST,expand=0)**
- Trả về một bản sao chép của hình ảnh được xoay số lượng nhất định theo chiều ngược kim đồng hồ.

**im.save(outfile,format,options)**
- Lưu hình ảnh dưới tên file nhất định.

**im.seek(frame)**
- Tìm cách đưa ra khung trong một trình tự file.

**im.show()**
- Hiển thị hình ảnh