#Khái niệm Pick, Unpick
*Tên tài liệu: Tìm hiểu khái niệm Pick, Unpick*

*Người thực hiện: Hoàng Quốc Cường*

##Mục lục:
- [1.Pickle là gì?](#pig)
- [2.dump() và load()](#trump)

##Nội dung:
<a name = "pig" />
###1.Pickle là gì?
- Module **Pickle** thực hiện một thuật toán cơ bản, nhưng là thuật toán mạnh mẽ cho việc serializing và de-serializing một cấu trúc đối tượng python. **Picking** là quá trình mà hệ thống phân cấp đối tượng cho python được chuyển đổi thành một dòng byte, và **unpickling** là hoạt động ngược lại, nhờ đó dòng byte được chuyển đổi thành một hệ thống phân cấp đối tượng. Pickling( và unpickling) được gọi khác như "serialization", "marchaling", hoặc "flattening", tuy nhiên, để tránh nhầm lẫn, được quy ước là "pickling" và "unpickling"
- Module Pickle không an toán đối với dữ liệu sai sót hoặc được xây dựng hiểm độc. Chưa bao giờ dữ liệu unpickle nhận được từ nguồn không tin cậy hoặc không được thẩm định.

<a name = "trump" />
###2.Hàm dump() và load()
**pickle.dump(obj, file[, protocol])**
- Viết một đại diện được ngâm của đối tượng để mở tệp "file object". Điều này tương đương với Pickler(file, protocol).dump(obj)
- Nếu tham số protocol được bỏ qua, protocol 0 được sử dụng. Nếu protocol được chỉ định như giá trị âm hoặc HIGHEST_PROTOCOL, phiên bản protocol cao nhất sẽ được sử dụng
- File phải có phương thức write() chấp nhận đối số chuỗi đơn lẻ. Do đó nó có thể là đối tượng tệp được mở cho văn bản, một đối tượng StringIO, hoặc bất kỳ đối tượng được tùy chọn nào có thể đáp ứng được interface này

**pickle.load(file)**
- Đọc một chuỗi từ tập tin đối tượng và giải thích nó như một dòng dữ liệu pickle, xây dựng lại và trả về hệ thống phân cấp đối tượng. Điều này tương đương với **Unpicker(file).load()**
-Tập tin phải có 2 phương thức, một phương thức read() mà có một đối số nguyên và một phương thức readline() sẽ không cần đối số. Cả hai phương thức này cần trả về một chuỗi. Dó đó, tập tin có thể là một đối tượng tập tin mở, một đối tương **stringIO**, hoặc các đối tượng tùy chọn khác để đáp ứng interface này.
- Hàm này tự động xác định liệu các dòng dữ liệu có được ghi trong chế đó nhị phân hay không

**pickle.dumps(obj[,protocol])**
- Trả lại đại diện đối tượng pickled như một chuỗi, thay vì viết nó vào một tập tin
- Nếu tham số protocol được bỏ qua, protocol 0 được sử dụng. Nếu protocol được chỉ định như một giá trị âm hoặc HIGHEST_PROTOCOL, phiên bản giao thức cao nhất được sử dụng

**pickle.loads(strings)**
- Đọc một hệ thống phân cấp đối tượng pickled từ một chuỗi. Ký tự trong chuỗi qua đại diện các đối tượng pickled được bỏ quả