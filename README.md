# Chương trình mã hóa/giải mã RSA

## Giới thiệu

Đây là chương trình mã hóa và giải mã sử dụng thuật toán RSA, một hệ mật mã khóa công khai được phát triển bởi Rivest, Shamir và Adleman vào năm 1977. RSA là một trong những thuật toán mã hóa khóa công khai đầu tiên và được sử dụng rộng rãi cho việc truyền dữ liệu an toàn.

## Nguyên lý hoạt động của RSA

### 1. Sinh khóa

1. **Chọn hai số nguyên tố p và q**
   - Hai số này cần khác nhau và đủ lớn để đảm bảo an toàn

2. **Tính n = p × q**
   - n là modulo được sử dụng trong cả quá trình mã hóa và giải mã

3. **Tính φ(n) = (p-1)(q-1)**
   - φ(n) là hàm Euler, đếm số nguyên dương nhỏ hơn n và nguyên tố cùng nhau với n

4. **Chọn số e sao cho 1 < e < φ(n) và gcd(e, φ(n)) = 1**
   - e là số mũ mã hóa công khai
   - e và φ(n) phải nguyên tố cùng nhau (UCLN = 1)

5. **Tính d sao cho d × e ≡ 1 (mod φ(n))**
   - d là số mũ giải mã bí mật
   - d là nghịch đảo modular của e theo modulo φ(n)

6. **Khóa công khai: PU = {e, n}**
   - Được công khai cho mọi người để mã hóa thông điệp

7. **Khóa riêng: PR = {d, n}**
   - Được giữ bí mật để giải mã thông điệp

### 2. Mã hóa

1. **Thông điệp gốc M phải thỏa mãn M < n**
   - Nếu thông điệp dài, cần chia thành các khối nhỏ hơn n

2. **Công thức mã hóa: C = M^e mod n**
   - C là thông điệp đã mã hóa
   - Sử dụng thuật toán bình phương và nhân để tính hiệu quả

### 3. Giải mã

1. **Công thức giải mã: M = C^d mod n**
   - Khôi phục thông điệp gốc M từ thông điệp đã mã hóa C
   - Sử dụng thuật toán bình phương và nhân để tính hiệu quả

## Tính an toàn của RSA

Độ an toàn của RSA dựa trên độ khó của bài toán phân tích số nguyên lớn thành thừa số nguyên tố. Khi p và q là các số nguyên tố lớn (thường là 2048 bit trở lên trong ứng dụng thực tế), việc tìm ra p và q từ n = p × q là cực kỳ khó khăn với công nghệ hiện tại.

## Các thuật toán quan trọng được sử dụng

### 1. Kiểm tra số nguyên tố (Miller-Rabin)

Thuật toán Miller-Rabin là một thuật toán xác suất để kiểm tra một số có phải là số nguyên tố hay không. Thuật toán này nhanh và có độ chính xác cao khi số lần kiểm tra đủ lớn.

### 2. Thuật toán Euclid mở rộng

Được sử dụng để tìm UCLN của hai số và tính nghịch đảo modular. Công thức:
- gcd(a, b) = gcd(b, a mod b)
- ax + by = gcd(a, b)

### 3. Thuật toán bình phương và nhân (Square and Multiply)

Thuật toán hiệu quả để tính a^b mod n với độ phức tạp O(log b), thay vì O(b) khi tính trực tiếp.

## Cấu trúc chương trình

- **main.py**: File chính điều khiển chương trình
- **prime_check.py**: Kiểm tra số nguyên tố (Miller-Rabin)
- **key_generation.py**: Tạo khóa RSA
- **encryption.py**: Mã hóa RSA
- **decryption.py**: Giải mã RSA
- **utils.py**: Các hàm tiện ích
- **output/**: Thư mục lưu trữ kết quả sau mỗi lần chạy

## Hướng dẫn sử dụng

1. Chạy file `main.py`
2. Nhập hai số nguyên tố p và q
3. Chọn giá trị e thỏa mãn điều kiện
4. Sử dụng menu để thực hiện các chức năng:
   - Mã hóa thông điệp
   - Giải mã thông điệp
   - Hiển thị lại cặp khóa
   - Tạo cặp khóa mới
   - Thoát

## Lưu ý

- Chương trình này chỉ xử lý thông điệp dưới dạng số nguyên để đơn giản hóa. Trong ứng dụng thực tế, thông điệp văn bản sẽ được chuyển đổi thành dạng số trước khi mã hóa.
- Để đảm bảo an toàn trong thực tế, nên sử dụng các số nguyên tố có kích thước lớn (ít nhất 1024 bit).
