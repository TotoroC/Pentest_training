#Tìm hiểu: Kiểu dữ liệu cơ bản
*Tên tài liệu: Kiểu dữ liệu cơ bản*

*Người làm: Hoàng Quốc Cường*
##Mục lục:
- [1.Sử dụng python như 1 máy tính (calculator)](#calculator)
- [2.Tìm hiểu kiểu dữ liệu Number. Khác với C chỗ nào?](#number)
- [3. Tìm hiểu về string: nối chuỗi, cắt lát (slicing)](#string)
- [4. Tìm hiểu list 1 chiều và nhiều chiều: nối danh sách, cắt lát](#list)
- [5. Tìm hiểu boolean](#boolean)

##Nội dung:
<a name = "calculator"></a>
###1.Sử dụng python như 1 máy tính.
**Python** là một ngôn ngữ lập trình dạng thông dịch, do đó có thể tiếp kiệm vời gian phát triển ứng dụng vì không cần phải thực hiện biên dịch và liên kết. Trình thông dịch có thể sử dụng để chạy file script, hoặc cũng có thể được sử dụng theo các tương tác khác, trong đó có một đặc điểm là ta nhập từng biểu thức rồi nhấm phím **Enter** và kết quả sẽ được hiển thị ngay lập tức. Chính vì vậy, ta có thể tận dụng đặc điểm này để thực hiện các phép tính như một máy tính bỏ túi.

<img src = "http://i.imgur.com/iqBQ8iy.jpg">

Qua hình ảnh trên, bạn có thể thấy rằng trình thông dịch của python như một máy tính bỏ túi, có thể thực hiện các phép tính đơn giản .

 Các toán tử số học cơ bản:

| Toán tử | Miêu tả|
|---------|--------|
| +       | phép cộng |
| -       | phép trừ |
| *       | phép chia |
| /       | phép chia |
| //      | phép chia lấy phần thương |
| %       | phép chia lấy phần dư  |
| **      | phép lấy số mũ |

<a name = "number"></a>
###2.Tìm hiểu kiểu dữ liệu Number. Khác với C chỗ nào?
 **Python** sử dụng hệ thống kiểu *duck typing*, còn gọi là latent typing (tự động xác định kiểu dữ liệu). Nghĩa là, Python không kiểm tra các ràng bược về kiểu dữ liệu tại thời điểm dịch, mà là tại thời điểm thực thi.

- Kiểu dữ liệu Number lưu trữ các giá trị số. Chúng là các kiểu dữ liệu immutable, hay là kiểu dữ liệu không thay đổi, nghĩa là các thay đổi về giá trị của kiểu dữ liệu sẽ tạo ra một đối tượng cấp phát mới.

**Python** hỗ trợ 4 kiểu dữ liệu số:

- Kiểu int: kiểu số nguyên
- Kiểu long: là các số nguyên không giới hạn kích cỡ, được theo sau bởi chữ l hoặc chữ L.
- Kiểu float: kiểu số thực
- Kiểu complex: kiểu số phức

Trong trình thông dịch, biểu thức in cuối cùng được gán vào biến **_**. Ví dụ.

<img src = "http://i.imgur.com/OsGcCwk.jpg">

Ngôn ngữ Python khác với ngôn ngữ C ở một vài điểm như sau:

- Trong C ta phải khai báo kiểu dữ liệu còn trong Python thì không cần phải làm vậy.
- Trong Python, khi khai báo một biến ví dụ như `a = 5.0` thì biến a sẽ tự động là kiểu `float`
- Python có hỗ trợ kiểu số phức, còn C thì không

<a name = "string"></a>
###3. Tìm hiểu về string: nối chuỗi, cắt lát (slicing)
String là một trong các kiểu phổ biến nhất trong Python.Chúng ta có thể tạo các chuỗi bằng cách bao một text trong dấu nháy đơn **\' \'** hoặc dấu nháy kép **\" \"**. Nếu muốn xuất các đấu nháy đơn, nháy kép thì ta thêm **\ ** vào trước ký tự đó.
<img src = "http://i.imgur.com/bGEwbF4.jpg">

Toán tử nỗi chuỗi: 

- Được sử dụng để nối hai chuỗi giống nhau và tạo nên chuỗi mới. Cú pháp như sau:
>>`a = "Text1" + "Text2" ` thì kết quả sẽ là a = "Text1Text2"

- hoặc
>>`a = "Text1" "Text2"` thì kết quả sẽ tương tự như trên

<img src = "http://i.imgur.com/wUM4Dr3.jpg">

- Để nối chuỗi vào một biến chứa chuỗi, ta làm như sau:
>>`newvariable = variable + "text"`

<img src = "http://i.imgur.com/e0bnKX6.jpg">

Chia chuỗi(cắt lát - slicing):

- Chuỗi có thể được lập chỉ mục, với ký tự đầu tiền có chỉ mục là 0 và chỉ mục cuối cùng sẽ bằng `độ dài chuỗi -  1`.

<img src = "http://i.imgur.com/pXIgxBn.jpg">

- Để chia chuỗi, ta sử dụng cú pháp như sau:
>>`tên_chuỗi[chỉ mục đầu:chỉ mục sau]`

- Ví dụ, ta có một chuỗi `a = 'Python' `, và ta muốn chia thành `Py` và `thon` thì ta sẽ làm như sau:

<img src = "http://i.imgur.com/1FMMUPw.jpg">

<a name = "list"></a>
###4. Tìm hiểu list 1 chiều và nhiều chiều: nối danh sách, cắt lát
**List** là một kiểu dữ liệu phức hợp linh hoạt, List chứa những phần tử được ngăn cách nhau bỏi đấu **,** và nằm trong cặp dấu **[ ]**. Các phần tử của List có thể tồn tại nhiều kiểu dữ liệu khác nhau. Trong một list có thể chứa nhiều list khác, và ta gọi đó là list nhiều chiều.

Nối list và chia list tương đối giống nối chuỗi và chia chuỗi:

Nối List:

- List 1 chiều:
```
lista = [1,2,3,4]
print lista + [5,6,7,8]
Kết quả: [1,2,3,4,5,6,7,8]
```
- List nhiều chiều (cụ thể ở đây là 2 chiều)
``` 
lista = ["Bonjour",[1,2,3,4,5],"Merci"]
print lista + ["Q","W","E","R","T","Y"]
print lista[1] + ["Q","W","E","R","T","Y"]
Kết quả:
["Bonjour",[1,2,3,4,5],"Merci","Q","W","E","R","T","Y"]
["Bonjour",[1,2,3,4,5,"Q","W","E","R","T","Y"],"Merci"]
```

Chia list:

- List 1 chiều:
```
listb = [1,2,3,4,5,6,7,8]
print listb[2:5]
Kết quả:  [3,4]
```
- List nhiều chiều (cụ thể là list 2 chiều):
```
listc = ["Bonjour",[1,2,3,4,5,"Q","W","E","R","T","Y"],"Merci"] 
print listc[2][5:]
Kết quả là: ["Q","W","E","R","T","Y"]
```

<a name = "boolean"></a>
###5. Tìm hiểu boolean
Kiểu Boolean là kiểu chỉ có 2 giá trị **True**(đúng) và **False**(sai).
Trong Python, có hai toán tử cơ bản liên quan đến boolean là  **Toán tử so sánh** và **Toán tử logic**.

- Toán tử so sánh

<img src = "http://i.imgur.com/WOXontI.jpg">

- Toán tử logic:

| Toán tử | Miêu tả    |
|---------|------------|
| and     | phép và    |
| or      | phép hoặc  |
| not     | phép không |

```
True and True is True
True and False is False
False and False is True

True or True is True
True or False is True
False or False is False

not True is False
not False is True
```




