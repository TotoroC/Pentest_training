#Tìm hiểu cấu trúc dữ liệu
*Tên tài liệu: Tìm hiểu cấu trúc dữ liệu*

*Người thực hiện: Hoàng Quốc Cường*

##Mục lục.
- [1. Tìm hiểu về Tuples, sets, dict](#tu)
<ul>
<li>		[1.1.Tìm hiểu về Tuples](#tup)</li>
<li>		[1.1.Tập hợp sets](#se)</li>
<li>		[1.1.Hàm dict()](#di)</li>
</ul>
- [2.urllib2](#url)

##Nội dung.
<a name = "tu"></a>
###1.Tìm hiểu về Tuples, set,dict.
<a name = "tup"></a>
####1.1.Tìm hiểu về Tuples.
- Tuples được hiểu nôm là là một danh sách không thay đổi : không thể gán giá trị mới cho từng phần tử của tuple. Tuples được định nghĩa tương tự như list, ngoài trừ việc tập hợp các phần tử được đặt trong dấu ngoặc đơn thay vì dấu ngoặc vuông như list, ngoài ra các quy tắc về chỉ số phần tử của tuple cũng tương tự như list. 
>>tuples = ("Hello","World",113,115,114)

- Python vẫn hiểu là tuples dù bạn bỏ dấu ngoăc đơn:
>>tuples = "Hello","World",113,115,114

- Tuple rỗng được tạo nên bởi một cặp ngoặc rỗng
>>tuples = ()

- Câu lệnh `tuples = "Hello","World",113,115,114` là một ví dụ của việc *đóng gói tuple (tuple packing)*: các giá trị  "Hello","World",113,115,114 được gói lại vào trong một tuple. Và quá trình ngược lại:
>> x,y,z,a,b = tuples

- Quá trình trên được gọi là *tháo dãy*. Việc tháo dãy yêu cầu các biến bên trái có cùng số phần tử như độ lớn của dãy. Chú ý rằng phép đa gán *(mutiple assignment)* thật ra chỉ là sự tổng hợp của việc gói tuple và tháo dãy.
- **Việc gói nhiều giá trị luôn tạo một tuple, nhưng phép tháo có thể được áp dụng cho chuỗi, danh sách, tuple.**
- Để truy cập các phần tử trong tuple, ta áp dụng tương tự như trong list,string:
```
tuples = ("Hello","World",113,115,114)
print tuples[2]
Kết quả: 113
```

<a name = "se"></a>
####.1.2 .Tập hợp sets.
- Python cũng bao gồm một kiễu dữ liệu **sets**. **Set** là tập hợp có thứ tự không có yếu tố trùng lặp. Cơ bản, nó được sử dụng để kiểm tra và loại bỏ các phần tử trùng lặp. **Set** cũng hỗ trợ các phép tình toán như hợp, giao, ....
- Cú pháp: `set()`
```
a = set('abracadabra')
b = set('alacazam')
print a
Kết quả: set(['a','r','b','c','d'])
#loại bỏ cãc phần tử có trong a nếu nó có trong b
print a - b
Kết quả : set(['r','b','d'])
#hợp phần tử của 2 tập hợp a và b
print a | b
Kết quả: set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
```

<a name = "di"></a>
####1.3.Hàm dict()
- Trước khi đến với hàm dict(), ta cần biết qua khái niệm **Dictionary**. Trong python, dictionary là một tập hợp các gặp key và value không có thứ tự. Tưởng tượng như nó là một cái tủ sách, với sách là key và các thông tin trong sách là value. Dictionary được bao quanh bởi các dấu ngoặc nhọn, mỗi cặp key-value được xem như là một item. Key mã đã truyền cho item đó phải là duy nhất, trong khi đó value có thể là bất kỳ kiểu giá trị nào.
- Cú pháp:
```
dictionary = {
	'Altar' : 1
	'Ezio' : 2
	'Connor': 3
	'Edward': 4
	}
```
- Hàm dict() dùng để tạo từ điển trực tiếp từ các danh sách các cụm khóa-giá trị chứa trong tuple.
```
dict([('Altar',1),('Ezio',2),('Connor',3),('Edward',4)])
Kết quả:
{'Altar': 1, 'Connor': 3, 'Edward': 4, 'Ezio': 2}
```

<a name = "url"></a>
###2.urllib2
Module **urllib2** định nghĩa các hàm và lớp giúp cho việc mở và thu thập URLs( chủ yếu HTTP) trong một thế giới phức tạp - gôm các xác thực căn bản và biến đổi, sự đổi hướng, cookie và những thứ khác.
Module **urllib2** định nghĩa các hàm sau:

####urllib2.urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]]])
- Mở URL, nó có thể là một chuỗi hoặc một đối tượng `Request`
- **data** có thể là một chuỗi xác định data bổ sung gửi đến máy chủ, hoặc `None` nếu không có dự liêu nào như vậy là cần thiết.Hiện nay truy vấn HTTP là truy vấn duy nhất sử dụng dữ liệu; Truy vẫn HTTP sẽ là một POST thay vì là một GET khi tham số data được cung cấp. Data nên được xem là  bộ đệm trong các định dạng chuẩn application/x-ww-form-unrlencoded. Hàm .urlencode()  nhận một mapping hoặc trình tự của  2-tuples và trả lại một chuỗi trong định dạng này. Module **urllib2** gửi truy vấn HTTP/1.1 bao gồm tiêu đề `connection:close`
- Tham số **timeout** tùy chọn chỉ định thời gian chờ đợi tính theo giây để ngăn chặn các hoạt động như cố gắng kết nối ( nếu không được chỉ định, việc cài đặt thời gian chờ đợi global sẽ được mặc định). Đó thực sự chỉ dành cho các kết nối HTTP, HTTPS và FTP. 
- Nếu phạm vi được chỉ địng, nó phải là một ssl.SSLContext mô tả các tùy chọn SSL khác. 
- Các tham số **cafile** và **capath**  tùy chọn chỉ định một tập hợp các chứng nhận CA đáng tin cậy cho truy vấn HTTPS. **cafile** nên trỏ đến một tập tin duy nhất có chứa một gói chứng nhận CA, trong khi **capath** phải trỏ đến một thư mục chứa các file chứng nhận hashed.
- Tham số cadefault được bỏ qua
Hàm này trả về một đối tượng giống như tập tin theo 3 phương pháp bổ sung sau đây:
```
geturl() : trả lại URL của tài nguyên được lấy ra, thường được sử dụng để xác định xem một chuyển hướng đã được theo sau hay chưa.
info() : trả lại một thông tin meta của trang như tiêu đề, dưới dạng mimetools.Message
getcode() : trả lại mã trạng thái HTTP của đáp ứng.
```
- Thêm URLError vào mục lỗi 
Chú ý: **None** có thể trả lại nếu bộ xử lý không xử lý các yêu cầu (mặc dù mặc định được cài đặt *OpenerDirector* toàn cục sẽ sử dụng *UnknownHandler* để đảm bảo điều đó không bao giờ xảy ra. 
- Ngoài ra, nếu thiết lập proxy được phát hiện ( ví dụ, khi một biến mỗi trường  **\*_proxy** giống như http_proxy được thiết lập), **ProxyHandler** được cài mặc định và đảm bảo các yêu cầu được xử lý thông qua proxy

---
####urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
- Lớp này là một phần của một yêu cầu URL 
- **url** nên là một chuỗi chứa các URL hợp lệ
- **data** có thể là một chuỗi dùng để chỉ định các dữ liệu bổ sung để gửi đến máy chủ, hoặc **none** nếu dữ liệu đó là không cần thiết. Hiện nay, HTTP là yêu cầu duy nhất sử dụng dữ liệu, yêu cầu HTTP sẽ là một POST thay vì GET khi thông số dữ liệu  được cung cấp. **data** nên là một bộ đệm định dạng chuẩn: application/x-www-form-urlencoded. Hàm **urllib.urlencode()** lấy một mapping hoặc trình tự của 2-tuples và trả về một chuỗi trong định dạng này.
- **headers** nên là một dictionary và sẽ là treated nếu như **add_header()** được dùng với từng khóa (key) và giá trị (value). Điều này thường được sử dụng để `spoof` giá trị **User-Agent** header, được sử dụng bởi một trình duyệt để xác định chính nó - một số máy chủ HTTP chỉ cho phép yêu cầu đến từ các trình duyệt phổ biến và điều này trái ngược với scripts. Ví dụ, Mozilla Firefox có thể xác định chính nó như *"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"*, trong khi chuỗi mặc định user-agent mặc định của urllib2 là *"Python-urllib/2.6"*
- Hai đối số cuối cùng chỉ quan tâm tới các thao tác của bên thứ 3 HTTP cookies.
- **origin_req_host** nên là request_host của giao tác gốc, theo định nghĩa của RFC 2965. Nó mặc định là cookielib.request_host(self). Đây là tên host hoặc địa chỉ ip của truy vấn gốc mà người sử dụng lần đầu. Ví dụ, nếu yêu cầu này dành cho một bản sao trong một bản ghi HTML, đó nên là request_host cho các yêu cầu cho trang chứa bản sao đó.
-**unverifiable** nên chỉ ra cho dù yêu cầu không thể xác minh được, như định nghĩa bởi RFC 2965. Nó mặc định là **False**. Một yêu cầu không được xác mình có URL mà người dùng không thể chấp nhận . Ví dụ, nếu yêu cầu này dành cho một bản sao nằm trong một bản ghi HTML, và người dùng không chấp nhận việc tự động lấy bản sao đó, điều này nên là **True**. 