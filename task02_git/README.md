#Tìm hiểu về Git/Github
*Tên tài liệu: Tìm hiểu và sử dụng Git/Github*
*Người làm: Hoàng Quốc Cường*
##Mục lục:
- [1. Git là gì ? Dùng để làm gì ?](#git)
- [2.Cài đặt trên máy tính.](#install)
- [3.Sử dụng Git trên terminal](#use)
- [4.Sử dụng git để commit , push file README.md lên Github](#commit)

##Nội dung:
<a name = "git"></a>
##1.Git là gì ? Dùng để làm gì ?
<ul>
	<li><p><b>Git</b> là một phần mêm quản lý mã nguồn, được phát triển bởi Linus Torvalds vào năm 2005.</p></li>
	<li><p>Sử dụng Git để lưu trữ các file cấu hình(đối với systems admin), hoặc có thể  tùy ý làm việc với source code mà không bị các xung đột trong quá trình tách/nhập.</p></li>
</ul>
<a name = "install"></a>
##2.Cài đặt Git trên máy tính?
Vì máy mình dùng hệ điều hành Ubuntu, nên mình sẽ tiến hành cài đặt nó trên cửa sổ Terminal:

-  Đầu tiên, bạn mở cửa sổ Terminal bằng cách nhấn tổ hợp phím `Ctr Alt T`
-  Tiếp theo, bạn gõ câu lệnh để tiến hành cài đặt git vào máy.
>sudo apt-get install git

Bước cài đặt đã xong, tiếp theo bạn tiến hành config username, email, lựa chọn trình soạn thảo mặc định:

- Để config username, ta dùng câu lệnh: 
>git config --global user.name "tên bạn muốn"
- Config email, ta dùng câu lệnh: 
>git config --global user.email emailcuaban@gmail.com
- Config trình soạn thảo mặc định. Vì mình dùng Sublime Text nên mình sẽ để mặc định là `subl`: 
>git config --global core.editor subl 
- Để xem các thiết lập bạn vừa đặt, bạn gõ lệnh:
>git config --list

<a name = "use""></a>
##3.Sử dụng Git trên Terminal
<b>Liên kết tài khoản bằng SSH:</b>
`SSH Key là một phương thức chứng thực người dùng bằng cách đối chiều Public Key và Private Key`
-Đầu tiên ta gõ lệnh:
>ssh-keygen -t rsa

-Sau đó nó sẽ hiển thị như sau 
>Enter file in which to save the key (/root/.ssh/id_rsa): [Press enter]
Enter passphrase (empty for no passphrase): [Press enter]
Enter same passphrase again: [Press enter]
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.

Nếu bạn nhập vào ô pasphrase thì hãy nhớ lấy nó.

- Để xem kết quả:
>ls ~/.ssh/

<img src = "http://i.imgur.com/BtTv0Na.jpg">
-Tiếp theo là lấy SSH key, bạn gõ các câu lệnh sau vào cửa sổ terminal:
>ssh-agent -s
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub

-Kết quả nó sẽ hiển thị như trong hình dưới đây:
<img src = "http://i.imgur.com/SCDJCtM.png">
-Bạn copy đoạn mã bắt đầu từ `ssh-rsa .....` và truy cập vào https://github.com/settings/ssh (với điều kiện là bạn đã đăng nhập github). Sau đó chọn Add key , vì mình đã có rồi nên nó sẽ hiện New SSH key:
<img src ="http://i.imgur.com/wuSzFxA.jpg">
-Cuối cùng bấm vào nút **Add SSH Key** để hoàn tất.

**Tạo clone respo**
Để tạo 1 clone, trước tiên bạn phải vào respository . Đối với Respository mới tạo thì nó sẽ hiện thị ra SSH, HTTPS như sau:
<img src = "http://i.imgur.com/54SN7uA.jpg">
<img src = "http://i.imgur.com/jyJyLqA.jpg">

Sau khi lấy được SSH, HTTPS, ta tạo Clone respo như sau: 
-Đối với SSH
>git clone git@github.com:TotoroC/python_trainings.git
hoặc
git clone git@github.com:TotoroC/python_trainings.git /opt/A để clone respo vào thư mục /opt/A

-Đối với HTTPS
>git clone https://github.com/TotoroC/python_trainings.git
hoặc
git clone https://github.com/TotoroC/python_trainings.git /opt/A để clone respo vào thư mục /opt/A

-Bạn có thể lựa chọn 1 trong hai cách.

Tiếp theo, ta dùng lệnh `cd python_trainings` để chuyển vào thư mục python_trainings

Để tạo 1 file README.md hoặc một thư mục mới, ta làm như sau:
-Vì mình sử dụng Sublime, nên file README.md tạo như sau:
>subl README.md

-Còn tạo 1 thư mục mới, ta dùng câu lệnh:
>mkdir thumucmoi/

-Để xóa thư mục, ta dùng lệnh
>rm -d tenthumuc

Vậy là xong bước tạo Clone respo!

<a name = "commit"></a>
###4.Sử dụng Git để commit, push file README.md lên github
-Trước khi `commit`, ta cần phải chuyển trạng thái của file README.md từ `Untracked` sang `Tracked` bằng cách thêm file README.md vào khu vực `Staging Area`, sử dụng câu lệnh:
>git add README.md


-Sau khi đưa file README.md vào khu vực `Staging Area`, ta tiến hành commit file bằng câu lệnh:
>git commit README.md -m "lời nhắn"
Với -m là để thêm comment  cho hành động commit file

-Cuối cùng, để đồng bộ lên server Github, ta dùng câu lệnh:
>git push origin master

-Lúc này, ta sẽ thấy các file commit của ta đã được đẩy lên.
Đây là toàn bộ tiến trình làm việc:
<img src = "http://i.imgur.com/ahTpbOT.jpg">
Và đây là kết quả:
<img src = "http://i.imgur.com/wl3Dma0.jpg">
<h3>Chúc bạn thành công!</h3>



