#Python Challenge level 7
*Người thực hiện: Hoàng Quốc Cường*

#Nội dung:
- Để hỗ trợ cho việc giải python challenge level 7, ta cần phải tìm hiểu qua thư viện [Image](https://github.com/TotoroC/python_trainings/blob/master/task11/Image.md)

**Ý tưởng giải Python Challenge level 7:**
- Ta dùng hàm open() trong thư viện Image để mở ảnh ra.
- Dùng phương thức getpixel(xy) để lấy tuple ở từng điểm ảnh
- Ta để ý rằnh, cứ 7 điểm ảnh là 1 màu, nên ta sẽ chỉ đưa ra các điểm ảnh khác nhau và cách nhau 7 đơn vị
- Nhìn hình trực quan, ta thấy rằng, vị trí các điểm màu xám nằm cắt đôi bức hình, nên ta sẽ lấy tổng số pixel chiều rộng là 94/2 ra 47 là tọa độ y của các điểm ảnh nằm trên đường xám đó. (xác định số pixel chiều dài và số pixel chiều rộng bằng cách dùng phương thức size có trong thư viện Image)
- Tại mỗi vị trí pixel, ta thu được 1 tuple có dạng [R,G,B,A]\(red, green, blue, alpha), ta thấy 3 giá trị R,G,B giống nhau nên ta lấy 1 giá trị và không chọn giá trị alpha
- Sau khi tập hợp lại các giá trị thu được và đổi nó sang ký tự theo ascii, ta thu được 1 thông điệp: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]njb
- Tiếp tục lấy bộ tuple trong chuỗi trên ra và thực hiện việc chuyển đổi ký tự, ta sẽ thu được kết quả.
- http://www.pythonchallenge.com/pc/def/integrity.html

[Sourcecode](https://github.com/TotoroC/python_trainings/blob/master/task11/pylevel7.py)
