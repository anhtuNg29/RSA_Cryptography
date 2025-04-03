from utils import square_and_multiply, gcd, mod_inverse


def encrypt(plaintext, e, n, logger=None):
    """
    Mã hóa thông điệp bằng RSA
    
    Args:
        plaintext: Thông điệp cần mã hóa (số nguyên)
        e: Khóa công khai
        n: Modulo
        logger: Đối tượng logger để ghi log (tùy chọn)
        
    Returns:
        Thông điệp đã mã hóa (số nguyên)
    """
    if plaintext < 0 or plaintext >= n:
        raise ValueError(f"Thông điệp phải nằm trong khoảng [0, {n-1}]")
    
    # C = P^e mod n
    ciphertext = square_and_multiply(plaintext, e, n)
    
    print(f"\nQuá trình mã hóa:")
    print(f"Thông điệp gốc (P): {plaintext}")
    print(f"Công thức: C = P^e mod n = {plaintext}^{e} mod {n}")
    print(f"Kết quả mã hóa (C): {ciphertext}")
    
    # Ghi log nếu có logger
    if logger:
        logger.log_encryption(plaintext, e, n, ciphertext)
    
    return ciphertext

def encrypt_message(current_keys=None, logger=None):
    """
    Hàm xử lý quá trình mã hóa từ người dùng
    
    Args:
        current_keys: Khóa hiện tại nếu có
        logger: Đối tượng logger để ghi log (tùy chọn)
    """
    try:
        if current_keys:
            # Sử dụng khóa hiện tại mà không hỏi người dùng
            n = current_keys['n']
            e = current_keys['e']
            print(f"Sử dụng khóa công khai: PU = {{e, n}} = {{{e}, {n}}}")
        else:
            print("Chưa có khóa được tạo. Vui lòng tạo khóa trước khi mã hóa.")
            return
        
        print("\nLưu ý: Trong RSA thực tế, thông điệp được chuyển đổi thành số trước khi mã hóa.")
        print(f"Thông điệp phải nằm trong khoảng [0, {n-1}]")
        
        plaintext = int(input("\nNhập thông điệp (dạng số nguyên): "))
        
        if plaintext < 0 or plaintext >= n:
            print(f"Lỗi: Thông điệp phải nằm trong khoảng [0, {n-1}]")
            return
        
        ciphertext = encrypt(plaintext, e, n, logger)
        print(f"\nThông điệp đã mã hóa: {ciphertext}")
        
    except ValueError as e:
        print(f"Lỗi: {e}")

