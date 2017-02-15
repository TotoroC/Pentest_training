#Tìm hiểu "Hello World!" - Chương trình đầu tiên
Tên tài liệu: "Hello World!" - Chương trình đầu tiên

Thực hiện: Hoàng Quốc Cường

##Mục lục
- [1.Cài đặt Python trên Windows](#settup)
- [2.Cài đặt và tìm hiểu về pip](#pip)
- [3.Cằi đặt biến môi trường đối với Windows](#bmt)
- [4.Khái niệm về thông dịch và biên dịch](#tdbd)
- [5.Viết chương trình hello world bằng biên dịch và thông dịch](#helloworld)

##Nội dung:

<a name = "settup"></a>
###1.Cài đặt Python trên Windows.
Để cài đặt `Python`, đầu tiên ta phải xác định được phiên bản mà ta muốn cái. Hiện tại, `Python` đang có hai phiên bản đang được sử dụng là `Python 2.x` và `Python 3.x`. Ở đây, mình sẽ tiến hành cài đặt `Python 2.x` cụ thể là phiên bản `Python 2.7.12`.

 Đầu tiên, để có được bộ cài đặt, ta cần lên trang chủ của Python : https://python.org . Sau đó, chỉ vào khung Download trên màn hình là chọn phiên bản `Python 2.7.12` để tải về:

<img src = "http://i.imgur.com/hzSbl4M.jpg">

- Sau khi tải về, ta tiến hành chạy file cài đặt. Nhìn vào hình, ta có thể thấy hai dòng lựa chọn : `Install for all users` và `Install for just me`. Ở đây mình chọn như trong hình:

<img src = "http://i.imgur.com/lU1lEyp.jpg">

- Tiếp theo là lựa chọn đường dẫn nơi cài đặt chương trình `Python`. MÌnh để mặc định là `C:\Python27` để sau này thuận tiện cho việc cài đặt biến trên môi trường windows

<img src = "http://i.imgur.com/jSeFmbH.jpg">

- Sau khi lựa chọn đường dẫn nơi cài đặt chương trình `Python`, tiếp theo là đến phần lựa chọn các chức năng đi kèm, mình để mặc định và bấm next:

<img src = "http://i.imgur.com/DUelbqN.jpg">

- Như vậy tiến trình cài đặt đã hoàn thành. Để kiểm tra, mĩnh sẽ khởi động `Python` lên như trong hình:

<img src ="http://i.imgur.com/w62A1hL.jpg">
<img src = "http://i.imgur.com/9FLay7H.jpg">

- Vậy là đã xong bước cài đặt `Python` trên windows. Chúc bạn thành công!

<a name = "pip"></a>
###2.Cài đặt và tìm hiểu về pip
**2.1.Trước khi bước vào cài đặt `pip`, chúng ta sẽ cùng tìm hiểu một số thông tin về `pip`.**

-  `Pip` là một trình quản lý gói (package manager) thư viện cho python. Pip có mặt từ phiên bản Python 2.7.9 trở lên (đối với phiên bản `Python 2.x`) và Pytho 3.4 trở lên (đối với phiên bản `Python 3.x`). `Pip` có thể là viết tắt của `Pip Install Package` , `Pip Install Python`,... Việc cài đặt một Package với pip khá đơn giản, ta chỉ cần sử dụng câu lệnh:
>>pip install package-name

-  `Pip` mang lại cho chúng ta khá nhiều tính năng như instal Package, Download Package, Uninstall Package, Show( hiện thị thông tin về gói được cài đặt), ....
- Cú pháp của `pip`:
>> `pip <command> [options]`

<img src = "http://i.imgur.com/kzH6a5u.jpg">

**2.2.Cài đặt pip**

- Chúng ta sẽ tải file [get-pip.py](https://bootstrap.pypa.io/get-pip.py) về và tiến hành chạy để cài đặt `pip`.
- Ngoài ra, chúng ta có thể sử dụng câu lệnh:

>>
Đối với Linux:
pip install -U pip setup tools

>>Đối với Windows:
python -m pip install -U pip setuptools

**Lưu ý: đối với Windows, để thực hiện câu lệnh trên, ta cần tiến hành cài đặt biến đối với môi trường Windows, cách cài đặt sẽ được nhắc đến ở mục 3.**

<a name = "bmt"></a>
###3.Cài đặt biến môi trường đối với Windows:
Để có thể sử dụng trực tiếp lệnh `python` hay `pit` trên của sổ command line thì ta cần phải tiến hành cài đặt biến môi trường và cách làm như sau:

- Đầu tiên, ta chuột phải vào biểu tượng Windows và chọn System để vào của sổ System:

<img src = "http://i.imgur.com/wYODW15.jpg">

- Tiếp theo, ở trong của sổ `System`, ta chọn `Advanced system settings` ở cột bên phải của cửa sổ `System`. Nó sẽ xuất hiện một cửa số `System Properties`. Trong tab `Advanced`, ta  sẽ chọn `Environment Variables`.

<img src = "http://i.imgur.com/b2KAwk3.jpg">

- Trong cửa sổ `Environment Variables`, ta nhìn vào khung `System variables`, tìm một biến bên cột Variable với tên là **Path**, sau đó chọn edit rồi edit text.

<img src = "http://i.imgur.com/paWim4d.jpg">

- Tiếp theo, sau khi chọn edit text, ta thêm đoạn đường dẫn `;C:\Python27;C:\Python27\Scripts` . Đó là lí do tại sao khi cài đặt, mình lại để đường dẫn mặc định vì nó ngắn gọn. 

<img src = "http://i.imgur.com/yhuIWer.jpg">

- Cuối cùng, ta bấm **OK** để hoàn tất việc cài đặt biến, giờ ta sẽ mở cửa sổ  Command Line lên để tiến hành kiểm tra xem **pip và python** đã hoạt động chưa. **Lưu ý: ta nên khởi động cửa sổ Command Line với quyền hạn của Admin**.

<img src = "http://i.imgur.com/rNLuZmK.jpg">

Như vậy, ta có thể dụng lệnh **pip, python** trực tiếp mà không gặp bất cứ trở ngại gì.

<a name = "tdbd"></a>
###4.Khái niệm về Thông dịch và Biên dịch
- **Thông dịch(Interpreter)** : sau khi soạn thảo một chương trình bằng một ngôn ngữ lập trình nào đấy, thì quá trình thông dịch sẽ dịch từng lệnh của chương trình mà bạn đang thực thi. Lần sau muốn chạy lại chương trình thì phải thông dịch lại.
- **Biên dịch(compiler)**: làm công việc chuyển đổi các câu lệnh được gõ bằng ngôn ngữ lập trình nào đấy sang ngôn ngữ máy tính để máy tính có thể hiểu và thực hiện. Cuối cùng tạo ra một file thực thi mà bạn có thể chạy được, sau này chỉ cần chạy lại file đó để thực thi.

<a name = "helloworld"></a>
###5.Viết chương trình HelloWorld bằng trình biên dịch và trình thông dịch.
Đầu tiên, mình sẽ viết chương trình bằng trình **thông dịch** và viêt nó trong cửa sổ `Terminal` của hệ điều hành Ubuntu.

- Mở cửa sổ `Terminal` và gõ lệnh `python` để vào màn hình làm việc:
<img src = "http://i.imgur.com/zkOe6PN.jpg">

- Sau đó, để hiện thị câu "Hello World!" ra màn hình, ta dùng lệnh:
>>print "Hello Word!"

<img src = "http://i.imgur.com/4ZBELo9.jpg">

-  Bạn có thể thấy khi ta thoát khỏi chương trình và vào lại, muốn hiện câu "Hello World!" thì chúng ta phải ghi lại từ đầu, ta có thể thấy rằng đó chính là trình biên dịch.

Tiếp theo, mình sẽ viết bằng trình **biên dịch**, ở đây mình sử dụng trình soạn thảo Sublime Text.

- Đầu tiên, ta mở trình soạn thảo Sublime Text, gõ câu lệnh `print "Hello World!". Sau đó, ta sẽ lưu file với cái tên hello.py (file .py là file của python). Sau khi tạo file hello.py và biết được vị trí đặt file, ở đây mình để nó ở **Desktop**. Ta sẽ mở cửa sổ Terminal lên, di chuyển đến thư mục chứa file cần thực thi, gõ câu lệnh:
>>python hello.py

<img src = "http://i.imgur.com/OvVlOTx.jpg">

- Ở đây, cửa sổ Terminal sẽ đóng vai trò là một trình biên dịch file hello.py.

Vậy qua hai mục 4 và 5, ta có thể hiểu phần nào về biên dịch và thông dịch, đồng thời có thể viết một chương trình đơn giản thông qua trình biên dịch và trình thông dịch. Chúc bạn thành công ! 
