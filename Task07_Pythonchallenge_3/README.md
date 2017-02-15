#Pythonchallenge.com
*Tên tài liệu: Tìm hiểu Pythonchallenge*

*Người làm: Hoàng Quốc Cường*

##Mục lục:
- [1.Ý tưởng làm challenge](#challenge)
- [2. re Module](#re)

##Nội dung:

<a name = "challenge" />
###1.Ý tưởng làm challenge:
####Phân tích: 
"One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."Dựa vào đoạn mã trong source web và gợi ý bên, ta có thể đoán rắng kết quả sẽ là một chuỗi chữ cái in thường có nghĩa và mỗi chữ cái cấu thành lên chuỗi đó sẽ được bao bọc bởi chính xác 3 chữ cái in hoa ở trong đoạn mà source web. Giờ vấn đề đặt ra là tìm được các chữ cái thường thỏa điều kiện là nó được bao bọc bởi duy nhất 3 chữ cái in hoa ở mỗi mặt, có nghĩa nó sẽ được bao bọc tổng cộng 6 chữ cái in hoa ở hai bên. Ví dụ: `m-A-I-L-a-A-N-H-e`, trong chuỗi bên, 'a' chính là một thành phần trong chuỗi cần tìm vì đó đáp ứng đủ yêu cầu đề cho.
####Ý tưởng giải:
Ta sẽ dùng vòng lặp và dựa vào chỉ mục của chuỗi. Đầu tiên, ta sẽ cho i chạy từ 0 đến độ dài của chuỗi. Sau đó kiểm tra xem ở vị trí i trong chuỗi là ký tự in hoa hay in thường, nếu in thường thì qua chỉ mục tiếp theo, nếu in HOA, thì ta sẽ kiểm tra xem các điều kiện sau:
```
Vị trí i - 1: là chữ thường
Vị trí i + 1: là chữ in hoa
Vị trí i + 2: là chữ in hoa
Vị trí i + 3: là chữ thường
Vị trí i + 4: là chữ in hoa
Vị trí i + 5: là chữ in hoa
Vị trí i + 6: là chữ in hoa
Vị trí i + 7: là chữ thường
```
Từ các điều kiện trên và kết hợp điều kiện vị trí i là chữ in HOA, ta có thể thấy rằng vị trí i+3 sẽ là một phần tử trong chuỗi cần tìm và ta add vào chuỗi rỗng để cuối cùng là thu được kết quả.

<a name = 're' />
###.2.re Module
####re- Reqular Expression operations
- Module này cung cấp biểu thức chính quy phù hợp với các hoạt động tương tự như tìm thấy trong Perl. Cả hai mô hình và chuỗi được tìm kiếm có thể là chuỗi Unicode cũng như chuỗi 8-bit.

- biểu thức chính quy sử dụng ký tự ('\') để chỉ ra các form đặc biệt hoặc cho phép các ký tự đặc biệt được sử dụng mà không cần gọi ý nghĩa đặc biệt của chúng. Điều này đối lập với Python cách sử dụng một vài ký tự giống nhau cho cùng một mục định trong chuỗi bằng chữ; Ví dụ, để  phù hợp với một dấu gạch chéo, một trong nhũng cách có thể viết \\\ như chuỗi mô hình, bởi vì biểu thức chính quy phải là \\ và mỗi dấu gạch chèo ngược phải được thể hiện như \\ bên trong một chuỗi Python thường

- Giải pháp là sử dụng nguyên chuỗi kí hiệu của python cho các mẫu biểu thức chính quy; các dấu gạch chéo ngược không được xử lý bất kỳ phương pháp đặc biệt nào trong một chuỗi chữ với tiền tố 'r'. Vì vậy r"\n" là một chuỗi có chứa hai kí tự '\' và '\n', trong khi '\n' là một chuỗi chứa một kí tự cho phép xuống dòng. Thông thường, mẫu sẽ được thể hiện trong mã python bằng cách sử dụng ký hiệu nguyên chuỗi này.

- Nó là quan trọng để lưu ý rằng các hoạt động biểu thức chính quy là các biến  như là cac hàm cấp-module và phương thức RegexObject. Các hàm là phím tắt mà không yêu cầu bạn để biên dịch một đối tượng regex đầu tiên, nhưng bỏ lỡ một vài tham số fine-tuning

####Regular Expreesion Syntax

- Một biểu thức chính quy (hoặc RE) chỉ định một tổ hợp của chuỗi mà hợp với nó; các hàm trong module này cho phép bạn kiểm tra nếu một chuỗi riêng biện hợp lệ, một biểu thức chính quy được cung cấp ( hoặc nếu một biểu thức chính quy được cung cấp khớp với một chuỗi riêng biệt, nó đi xuống điều tương tự.

- biểu thức chính quy có thể được nối với mẫu biểu thức chính quy mới; nếu A và B là hai biểu thức chính quy, thì sau đó AB cũng là một biểu thức chính quy. Nói chung, nếu một chuỗi p khớp với A mà một chuỗi q khác khớp với B, chuỗi pq sẽ khớp với AB. Điều này đúng trừ khi A hoặc B chứa các hoạt đông ưu tiên thấp; giới hạn điều kiện giữa A và B, hoặc đã được đánh số tham chiếu nhóm. Do đó, các biểu thức phức tạp có thể dễ dàng xây dựng từ biểu thức nguyên hàm đơn giản như những mô tả ở đây. 

- biểu thức chính quy có thể chứa đựng các ký tự đặc biệt vào thông thương. Nhiều ký tự thông thường như 'A', 'a', or '0' là các từ ngữ thông thường đơn giản nhất; chúng chỉ đơn giản phù hợp với bản thân. Bạn có thể ghép các ký tự thường, vì vậy 'last' khớp với chuỗi 'last'.

- Một số ký tự khác như '|' hoặc '(' là đặc biệt. Các ký tự đặc biệt có thể đại diện cho lớp của các ký tự thường, hoặc ảnh hưởng đến các biểu thức chính quy xung quanh chúng được giải thích.  Mẫu chuỗi biểu thức chính quy có thể không chứ null byte, nhưng có thể chỉ định null byte sử dụng các ký hiệu \number

- Vòng lặp (*,+,?,{m,n}, etc) không thể được lòng trực tiếp. Điều này trán sự 


#####Các ký tự đặc biệt

**' . '**
- Trong chế độ mặc định. Điều này phù hợp với bất kỳ ký tự nào ngoại trừ một dòng mới. Nếu flag của DOTALL đã được quy định, điều này phù hợp với bất kỳ ký tự nào bao gôm một dòng mới

**'^'**
- Phù hợp với sự khởi đầu của chuỗi, và trong MULTILINE, chế độ cũng phù hợp ngay lập tức sau mỗi lần xuống dòng.

**'$'**
- Phù hợp với sự kết thúc của chuỗi hoặc ngay trước khi các dòng mới vào cuỗi chuỗi, và trong chế độ MULTILINE  cũng phù hợp trước một dòng mới. 'foo' phù hợp với cả 'foo' và 'foobar', trong khi biểu thức chính quy foo$ chỉ phù hợp với 'foo'. Nhiều thú vị hơn, tìm kiếm 'foo.$' trong 'foo1\nfoo2\n'thường phù hợp với 'foo2', nhưng 'foo1' trong chế độ MULTILINE; tìm kiếm một $ trong 'foo\n' sẽ tìm thấy hai phù hợp, một ngay trước khi xuống dòng, và một ở cuối của chuỗi.

**'*'**
- Nguyên nhân các RE kết quả phù hợp với 0 hoặc nhiều lần lặp lại của RE trước, như nhiều lần lặp lại như thế là khả thi. ab* sẽ phù hợp với 'a', 'ab', hoặc 'a' sẽ theo sau bởi bất kỳ số lượng 'b'

**'?'**
- Nguyên nhân các kết quả RE phù hợp với 0 và 1, nhiều lần lặp lại của RE. ab? sẽ phù hợp với cả 'a' hoặc 'ab'

**'+'**
- Nguyên nhân các kết quả RE để phù hợp với 1 hoặc nhiều lần lặp lại của RE. ab+ sẽ phù hợp với 'a' theo sau bởi một bài số khác 0 của 'b's

**\*?,+?,??**
- Chúng phù hợp với nhiều văn bản khả thi. Đôi khi cách xử lý này là không mong muốn; nếu RE <.*> là xuất hiện với `<a> b <c>`, nó sẽ phù hợp với toàn bộ chuỗi, và không chỉ `<a>`. Thêm ? sau khi điều kiện làm cho nó thực hiện phù hợp trong non-greedy hoặc minimal fashion, như một vài kí tự khác có thể sẽ hợp lệ.

**{m}**
- Chỉ định chính xác m bản RE trước đó nên hợp lệ; ít hợp lệ gây ra toàn bộ RE không phù hợp. VÍ dụ, {6} sẽ phù hợp chính xác 6 kí tự 'a', nhưng không phải năm

**{m,n}**
- Nguyên nhân kết quả RE phù hợp từ m đến n lần lặp của RE trước, cố gắng phù hợp với nhiều lần lặp lại càng tốt. Ví dụ, {3,5} sẽ phù hợp với 3-5 ký tự 'a'. Bỏ qua m xác định bởi giới hạn dưới 0, và bỏ qua n xác định một vô hạn hạn ràng buộc trên. Như một ví dụ, {b} sẽ phù hợp aaaab hoặc một ngàn ký tự 'a' tiếp theo là b, nhưng không phải aaab. Dấu phẩy có thể không được bỏ qua hoặc sửa đổi sẽ bị nhầm lẫn với hác hình thức mô trước.

**{m,n}?**
- Nguyên nhân kết quả RE phù hợp từ m đến n lặp lại của RE trước, cố gắng phù hợp với lài vẫn lặp lại là có thể. Đây là phiên bản non-greedy của vòng loại điều kiện. VÍ dụ, trên chuỗi 'aaaaaa', {3,5} sẽ khớp với 5 ký tự 'a', trong khi {3,5}? sẽ chỉ có 3 ký tự phù hợp

**'\'**
- Hoặc là thoát kỳ tự đặc biệt, hoặc báo hiệu một trình tự đặc biệt.
Nếu bạn không sử dụng chuỗi nguyên để chỉ ra mẫu, hãy nhớ răng Python cũng sử dụng dấu gạch chéo như một tiến trình trong xâu; nếu trình tự không được công hận bởi phân tích cú pháp của Python. Tuy nhiêu, Nếu Python nhận ra chuỗi kết quả, dấu chéo ngược nên được lặp lại hai lần. Điều này phức tạp và khó hiểu, vì vậy nó rất khuyến kích bạn sử dụng chuỗi nguyên cho tất cả các biểu thức đơn giản

**[]**
-Được sử dụng để chỉ ra một tập hợp các ký tự.
- Ký tự có thể được liệt kê riêng
- Phạm vi của ký tự có thể được chỉ định bằng cách cho hai ký tự và tách chúng bằng một '-', ví dụ [a-z] sẽ phù hợp với bất kỳ bản ASCII chữ thường, [0-5][0-9] sẽ phù hợp với tất cả các số có hai chữ số từ 00-59, và [0-9A-Fa-f] sẽ phù hợp với bất kỳ chữ số hexa. Nếu '-' được thoát  hoặc nếu nó được đặt như là ký tự đâu tiên hoặc cuối cùng, nó sẽ phù hợp với '-
- Các ký tự đặc biệt mất đi ý nghĩa trong tập hợp.
- Các lớp ký tự như \w hoặc \s cũng được chấp nhận trong một tập hợp, mặc dù những những ký tự phù hợp với chúng phụ thuộc vào việc LOCALE hay UNICODE ở chế độ có hiệu lực
- Ký tự đó không phải là trong một phạm vi có thể được thể hiện bằng việc bổ sung tập hợp. Nếu ký tự đầu tiên của tập hợp là '^', tất cả các ký tự không có trong tập hợp sẽ được xuất hiện. Ví dụ, [^5] sẽ phù hợp với bất kỳ ký tự nào ngoại trừ '5', và [^^] sẽ phù hợp với bất kỳ ký tự nào ngoại trừ '^'. ^ không có ý nghĩa đặc biệt nếu nó không phải là ký tự đầu tiền trong tập hợp.
- Để phù hợp với một ký tự ']' bên trong tập hợp, trước nó phải là dấu '\' .

**'|'**
- A|B, trong đó A và B có thể REs tùy ý, tạo ra một biểu thức chính quy sẽ phù hợp hoặc A hoặc B. Một số tùy ý của REs có thể được tách bằng bởi dấu '|'.
- Điều này có thể được sử dụng trong các nhóm. Như chuỗi mục tiêu được quét, RÉ phân cách bằng '|' từ trái sang pải. Khi một mẫu hoàn toàn phù hợp, nhánh đó được chấp nhận. Điều này có ý nghĩa rằn một khi A phù hợp, B sẽ không được tiếp tục kiểm tra, ngay cả nó sẽ tạo ra .......

**(....)**
- Bất cứ biểu thức chính quy nào đặt bên trong các dâu ngoặc đơn là phù hợp và chỉ bắt đầu và kết thúc trong một nhóm; các nội dung của nhóm có thể được lấy ra sau khi một ký tự phù hợp được thực hiện và có thể được xuất hiện sau đó trong chuỗi với các trình tự đặc biệt \number.

**(?...)**
- Đây là một ký hiệu mở rộng. Các ký tự đầu tiên sau '?' khi xác định những gì ý nghĩă và cú phắp ..........

####Module COntents
- Module định nghĩa một số chức năng, hằng số và một ngoại lệ. Một vài hàm là phiên bản giản tiện của các phương thức đầy đủ tính năng cho biên soạn biểu thức chính quys. Nhiều ứng dụng non-trivial luôn luôn sử dụng mẫu biên dịch

**re.complie(pattern, flags = 0)**
- Biên dịch một dấu hiện biểu thức chính quy trong một đối tượng biểu thức chính quy, mà có thể được sử dụng phù hợp với các phương thức match() và search(). 
- Các phiên bản biên dịch của nhiều mô hình mới gần đây được thông qua re.match(), re.search() hoặc re.compile() được lưu trữ, vì vậy các chương trình sử dụng chỉ một vài biểu thức chính quy tại một thời điểm mà không cần phải lo lắng về biên dịch re

**re.DEBUG**
- Hiện thị thông tin debug về biên dịch biểu thức

**re.IGNORECASE**
- Thực hiện trường hợp không nhạy cảm, biểu thức như [A-Z] sẽ phù hợp với chữ thường. Điều này không bị ảnh hưởng bởi những khu vực hiện tại

**re.LOCALE**
- Làm \w, \W, \b, \B, \s và \S phụ thuộc vào khu vực hiện tại

**re.MULTILINE**
- Khi chỉ định, mẫu ký tự '^' phù hợp tại lúc bắt đầu chuỗi và bắt đầu mỗi dòng; và mẫu ký tự '$' phù hợp lúc kết thúc chuỗi và kết thúc mỗi dòng. Mặc định, '^' chỉ phù hợp khi bắt đầu chuỗi và '$' lúc kết thúc chuỗi và ngay trước dòng mới tại kết thúc của chuỗi

**re.DOTALL**
- Làm ký tự đặc biệt '.' phù hợp bất kỳ ký tự nào, bao gồm một dòng mới, không có flag này, '.' sẽ phù hợp với bất cứ điều gì ngoại trừ dòng mới.

**re.UNICODE**
- Làm \w, \W, \b, \B, \d, \D , \s và \S phụ thuốc vào cơ sở dữ liệu thuộc tính UNICODE

**re.VERBOSE**
- flag này cho phép bạn viết biểu thức chính quys trông đẹp mắt và dễ đọc hơn bằng cách cho phép bạn phân biệt phần logic trực quan của mẫu và thêm ý kiến. Khảng trắng ở trong mẫu sẽ được bỏ qua, loại trừ khi trong một lớp ký tự hoặc đứng trước bởi một dấu chéo ngược. Khi một dòng chưa '#' mà không phải là trong một lớp ký tự và không được bắt đầu bởi dấu gạch chéo, tất cả các nhân tật tận trùng bên trái # thông qua sự kết thúc của dòng được bỏ qua

**re.search(pattern, string, flags=0)**
- quét qua chuỗi tìm kiếm khu vực đầu tiên mà các mẫu biểu thức chính quy tạo ra phù hợp, và trả lại một trường hợp MatchObject tương ứng. Trả lại giá trị None nếu không có điểm nào phù hợp với mẫu; lưu ý rằng điều này khác nhau từ việc tìm kiếm một độ dài không phù hợp tại vài điểm trong chuỗi

**re.match(pattern,string,flags = 0)**
- Nếu 0 hoặc nhiều ký tự bắt đầu trong chuỗi phù hợp với dấu hiện biểu thức chính quy; trả lại một trường hợp MatchObject tương ứng. Trả lại None nếu chuỗi không khớp với mẫu, chú ý 

**re.split(mẫu, chuỗi, maxsplit = 0, flags = 0)**
- Chia chuỗi bằng những lần xuất hiện của mẫu. Nếu dấu ngoặc tròn được sử dụng trong mẫu, sau đó các văn bản của các nhóm trong mẫu cũng được trả về như một phần của danh sách kết quả. Nếu maxsplit khác không, tại hầu hết các phần chia nhỏ maxsplit xảy ra, và phần còn lại của chuỗi được trả lại như là yếu tố của danh sách

**re.findall(pattern,string,flags = 0)**
- Trả lại tất cả những so sánh mẫu không trùng lặp trong chuỗi, như danh sách các chuỗi. Các chuỗi được quét từ trái sang phải, và các so sánh được trả về theo thứ tự tìm thấy. Nếu một hoặc nhiều nhóm được hiện diện trong mẫu, trả lại một danh sách các nhóm; đó sẽ là một danh sách tập hợp nếu mẫu có nhiều hơn một nhóm. Kết quả sẽ bao gồm so sánh rỗng bao gồm kết quả nếu như chúng không chạm vào phần đầu của so sánh khác.

**re.finditer(pattern, string, flags = 0)**
- Trả lại một lượng iterator hợp MatchObject trên tất cả phù hợp không chồng chéo cho các mẫu Re trong chuỗi. Chuỗi được quét từ trái sang phải, phù hợp được trả về theo thứ tự tìm thấy. Phù hợp rỗng được bao gôm kết quả trừ khi chúng chạm vào phù hợp bắt đầu

**re.sub(pattern,repl,string, count = 0, flags = 0)**
- Trả lại chuỗi  thu được bằng cách thay thế những sự cố không chồng chéo tận cùng bên trái của mẫu trong chuỗi bằng các repl thay thế. Nếu mẫu không tìm được, chuỗi được trả về không thay đổi. repl có thể là một chuỗi hoặc một hàm; nếu nó là một chuỗi, bất kỳ dấu gạch chéo thoát trong nó được xử lý. Đó là \n được chuyển đổi sang một ký tự dòng duy nhất, \r được chuyển đổi sang trả về vận chuyển, và vv. Thoát không xác định như \j còn lại một mình. Backreferences, như \6, được thay thế bởi chuỗi con hợp lệ bởi nhóm 6 trong mẫu
- Nếu repl là một hàm, nó được gọi cho mỗi lần xuất hiện không chồng chéo của mẫu. Các hàm có một số đối tượng phù hợp, và trả về chuỗi thay thế.
- mẫu có thể là một chuỗi hoặc một đối tượng RE
-  Các đối số tùy chọn được số lượng tối đã, mẫu phải được thay thế; số phải là một số nguyên không âm. Nếu bỏ qua hoặc 0, tất cả các lần xuất hiện sẽ được thay thế.

**re.subn(pattern, repl, string count = 0, flags = 0)**
- Hoạt đông như sub() nhưng trả lại một tuple (new_string, number_of_subs_made)

**re.escape(string)**
- Trả lại chuỗi với tất cả các phi chữ cái và số được gạch chéo; điều này hữu dụng nếu bạn muôn kết hợp một chuỗi chữ tùy ý rằng có thể có siêu ký tự biểu hiện thường huyên trong đó.

**re.purge()**
- xóa bộ nhớ đệm biểu thức chính quy

**re.eror**
- Ngoại lệ khi một chuỗi thông qua để một trong những hàm ở đây không phải là một biểu thức chính quy hoặc khi có một số lỗi xảy ra trong qua trình biên dịch hoặc kết hợp. Nó không bao giờ là lỗi nếu một chuỗi chữa mẫu không phù hợp



