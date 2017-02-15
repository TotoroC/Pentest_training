#Python Challenge level 6
*Người thực hiện: Hoàng Quốc Cường*
##Nội dung
Ý tưởng:
- Truy cập: www.pythonchallenge.com/pc/def/channel.html
- Xem source của web, và ta để ý đến phần comment ở dòng đầu tiên : \<\!-- <\-\- zip -->
- Zip, đoán chắc là file zip rồi, nhưng lấy file zip đó ở đâu ?
- Đổi đường dẫn www.pythonchallenge.com/pc/def/channel.html thành www.pythonchallenge.com/pc/def/channel.zip thì ta sẽ tải được 1 file channel.zip về
- Mở file zip ra, thấy toàn tệp txt có tên là các con số và 1 file txt có tên là readme
- Mở file readme lên thì thấy có hai gợi ý, trước hết ta chú ý đến gợi ý đầu tiên là mở một tệp txt có tên số là '90052.txt'
- Mở file '90052.txt' thì thấy ở trong nó ghi 'Next nothing is 94191'. Ngẫm lại, challenge này khá giống với challenge level 4, nhưng thay vì thay đổi đường dẫn trên url thì ở đây ta sẽ mở từng file theo gợi ý, cách thức làm thì tương tự, nhưng ở đây ta sẽ sử dụng thư viện zipfile để thực hiện mở các file có trong file zip và đọc nội dung của nó.
- Kết quả thu được là: **Collect the comments**. Hmm, nó còn thiếu cái gì đó.
- Thu thập comment của mỗi file bằng cách sử dụng getinfo() để lấy thông tin của file và .comment để lấy comment của file đó thông qua getinfo(), xong thì ta được:
<img src = "http://i.imgur.com/ubrSVx0.png">
- www.pythonchallenge.com/pc/def/hockey.html thì nhận được **it's in the air. look at the letters**. Nhìn kỹ lại vào kết quả thu được bên trên, sau khi ghép các chữ thu được từ kết quả trên, ta được kết quả là **oxygen**. Next level: http://www.pythonchallenge.com/pc/def/oxygen.html

[Sourcecode](https://github.com/TotoroC/python_trainings/blob/master/task10/pylevel6.py)
