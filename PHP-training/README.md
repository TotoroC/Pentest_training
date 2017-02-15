#Learn PHP
*Người thực hiện: Hoàng Quốc Cường*
##Nội dung
####1. Biến trong PHP

Quy tắc đặt trong PHP:

- Một biến trong PHP bắt đầu với ký tự $, theo sau nó là tên của biến
- Một biến phải bắt đầu bằng một chữ cái hoặc một dấu gạch dưới
- Một biến không thể bắt đầu bằng một số
- Một biến có thể chỉ có chữ cái, số và dấu gạch dưới
- Cùng một tên nhưng biến chữ hoa và chữ thường là hai biến khác nhau

####2.Xuất ra màn hình trong PHP
- Sử dụng hai hàm là echo và print để xuất ra màn hình
echo "Helloword!"
print "Helloword!"

####3.Kiểu dữ liệu
- PHP hỗ trợ các kiểu dữ liệu sau:
String, integer, float, boolean, array, object, null, resource
- Từ các phiên bản php 5 trở xuống thì các biến không cần khai báo kiểu dữ liệu. Còn PHP 7 thì có thể khai báo các kiểu dữ liệu

####4. String trong PHP

Các hàm xử lý chuỗi trong PHP

- strlen(): Đo độ dài của chuỗi
-  str_word_count(): đếm số từ trong một chuỗi
- strrev(): đảo ngược chuỗi
- strpos(): tìm kiếm một từ được chỉ định trong chuỗi
- str_replace(): thay đổi một vài ký tự bằng các ký tự khác được chỉ định trong chuỗi.

####5. Hằng trong PHP
- Không giống như các biến, hằng số được sữ dụng trên toàn bộ kịch bản
- Để tạo một hằng, ta sử dụng hàm define():
- define(name, value, case-insensitive)
Trong đó name là tên hằng, value là giá trị hằng, case-insensitive mặc định là false, nếu đặt là True thì khi gọi tên hằng, ta không cần chú trọng đến viết hoa hay viết thường trong tên.

####6. Toán tử trong PHP
- Toán tử trong PHP tương tự như trong python
- Trong so sánh, `$x===$y` nghĩa là trả về true nếu $x bằng $y và chúng cùng kiểu . `$x!==$y` trả về đúng nếu $x khác $y.
- Đối với chuỗi, `.` để nối 2 chuỗi lại, còn `.=` là lấy chuỗi trái = chuỗi trái nối với chuỗi phải. Ví dụ `$v1.=$v2` <=> `$v1=$v1.$v2`

####7. Điều khiển luồng trong C

Cú pháp:
```
if (điều kiện 1)
{ Khôi lệnh hoạt động khi điều kiện đúng;}
elseif(điều kiện 2)
{ Khối lệnh hoạt động khi điều kiện 2 đúng;}
else
{ Khối lệnh hoạt động khi cả hai điều kiện trên sai;}
```

####8.Câu lệnh Switch
- Thực hiện các câu lệnh khác nhau dựa trên các điều kiện khác nhau.
- Cú pháp:
```
switch(n)
{
	case 1:
		khối lệnh 1;
		break;
	case 2:
		khối lệnh 2;
		break;
	......
	case n:
		khối lệnh n;
		break;
	default:
		khối lệnh nếu n khác các case;
}
```
####9. Vòng lặp trong PHP

- Cú pháp vòng lặp while và do while:

```
while(điều kiện đúng)
{
	khối lệnh;
}
```
```
do
{
	khối lệnh
}while(điều kiện đúng);
```

- Cú pháp vòng lặp for:
```
for(điều kiện đầu, điều kiện cuối, bước nhảy)
{
	khối lệnh;
}
```
- Cú pháp vòng lặp foreach: Chỉ hoạt động trên các mảng, được lặp qua từng cặp giá trị trong một mảng.
```
foreach ($array as $value){
	khối lệnh;
}
```
####10.Hàm trong PHP

- Là một khối lệnh có thể sử dụng nhiều lần trong một chương trình
- Hàm sẽ không thực hiện ngay lập tức khi trang tải
- Hàm sẽ thực hiện khi ta gọi hàm
- Tên hàm có thể bắt đầu bằng chữ hoặc dấu gạch dưới nhưng không phải chữ
- Những tên hàm không phân biệt hoa thường.
- Cú pháp tạo hàm:
```
function tên_hàm()
{
	khối lệnh;
}
```

Có hai kiểu truyền dữ liệu vào hàm:

- Kiểu truyền khi gọi hàm
```
function vidu($chuoi)
{
	echo $chuoi;
}
vidu("Helloword!");
```
- KIểu truyền trực tiếp
```
function vidu($chuoi="Helloword!")
{
	echo $chuoi;
}
```
- Có thể trả lại giá trị cho hàm bằng câu lệnh `return giá_trị_trả_về;`

####11. Mảng trong PHP

- Một mảng lưu trữ nhiều giá trị trong một biến duy nhất
- Mảng là một biến đặc biệt có thể chứa nhiều hơn một giá trị tại một thời điểm
- Để tạo bảng trong PHP, ta sử dụng hay **array()**. Có 3 kiểu bảng:
- indexed arrays: Mảng với một chỉ số
```
$mang = array("Hello","World");
echo $mang[0]; => Hello
echo $mang[1[; => World
```
- Associative arrays: Mảng với từ khóa được đặt tên

```
$mavung = array("Ha Noi"=>"04","Da Nang"=>"0511","Ho Chi Minh"=>"08");
```

- Multidimensional arrays: mảng nhiều chiều

```
$mangnc = array
	(
		array("Valve","Dota2","CSGO");
		array("EA","BattleFiled","Fifa");
		array("Blizzard","Warcraft","Diablo");
	);
```

- Để đếm số phần tử trong mảng thì dùng hàm count()
- Sử dụng vòng lặp for đối với mảng chỉ mục và foreach đối với mảng từ khóa.
- Hàm sort() sắp xếp mảng theo thứ tự A-Z, sô tăng dần
- Hàm rsort() sắp xếp mảng theo thứ tự Z-A, số giảm dần
- Hàm asort() sắp xếp tăng dần theo giá trị trong mảng từ khóa
- Hàm ksort() sắp xếp tăng dần theo từ khóa trong mảng từ khóa
- hàm arsort() sắp xếp giảm dần theo giá trị trong mảng từ khóa
- Hàm krsort() sắp xếp giảm dần theo từ khóa trong mảng từ khóa

####12. Biến toàn cục và biến cục bộ trong PHP

- Biến cục bộ là các biến chỉ được sử dụng trong một trang, hoặc một hàm mà nó được khai báo.
- Biến toàn cục khác với biến cục bộ là không giới hạn phạm vi sử dụng.

Một số biến toàn cục thường được sử dụng:

- $GLOBALS : được sử dụng để truy cập các biến toàn cầu từ bất cứ nơi nào
- $_SERVER: biến toàn cầu nắm giữ thông tin về tiêu đề, đường dẫn, địa điểm của kịch bản. Trong biến server, có một vài thành phần quan trọng khác.
- $_REQUEST: sử dụng để thu thập dữ liệu sau khi nộp submit mẫu form HTML
- $_POST: được sử dụng rộng rãi để thu thập dữ liệu form sau khi submit form HTML với phương thức post. Nó cũng được sử dụng rộng rãi để vượt qua các biến.
- $_GET: Tương tự như $_POST, nhưng nó sử dụng phương thức get. Nó có thể thu thập dữ liệu gửi trong url.
- $_FILES
- $_ENV
- $_COOKIE
- $_SESSION

**Note:**

- Phương thức GET là phương thức gửi dữ liệu thông qua URL. Phương thức POST gửi dữ liệu qua form HTML.

####13.Kết nối PHP với Database
Cú pháp:
```
mysqli_connect('host','user database','password database','name database');
Ví dụ: mysqli_connect('localhost','root','','benh_vien');
```
- Các thông số trong hàm mysqli_connect được ta khởi tạo khi tạo một database và được nhà cung cấp dịch vụ cung cấp.
- Truy vấn cơ sở dữ liệu
```
mysqli_query() dùng để truy vấn vào cơ sở dữ liệu 
-Ví dụ:
$connect = mysqli_connect('localhost','root','','benh_vien');
$query = "SELECT * FROM Thuoc";
$result = mysqli_query($connect,$query);
Giá trị của $result sẽ là TRUE hoặc FALSE; 
```
