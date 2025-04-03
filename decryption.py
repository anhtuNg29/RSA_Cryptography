from utils import square_and_multiply

def decrypt(ciphertext, d, n, logger=None):
    """
    Giải mã thông điệp bằng RSA
    
    Args:
        ciphertext: Thông điệp đã mã hóa (số nguyên)
        d: Khóa bí mật
        n: Modulo
        logger: Đối tượng logger để ghi log (tùy chọn)
        
    Returns:
        Thông điệp gốc (số nguyên)
    """
    if ciphertext < 0 or ciphertext >= n:
        raise ValueError(f"Thông điệp đã mã hóa phải nằm trong khoảng [0, {n-1}]")
    
    # P = C^d mod n
    plaintext = square_and_multiply(ciphertext, d, n)
    
    print(f"\nQuá trình giải mã:")
    print(f"Thông điệp đã mã hóa (C): {ciphertext}")
    print(f"Công thức: P = C^d mod n = {ciphertext}^{d} mod {n}")
    print(f"Kết quả giải mã (P): {plaintext}")
    
    # Ghi log nếu có logger
    if logger:
        logger.log_decryption(ciphertext, d, n, plaintext)
    
    return plaintext

def decrypt_message(current_keys=None, logger=None):
    """
    Hàm xử lý quá trình giải mã từ người dùng
    
    Args:
        current_keys: Khóa hiện tại nếu có
        logger: Đối tượng logger để ghi log (tùy chọn)
    """
    try:
        if current_keys:
            # Sử dụng khóa hiện tại mà không hỏi người dùng
            n = current_keys['n']
            d = current_keys['d']
            print(f"Sử dụng khóa riêng: PR = {{d, n}} = {{{d}, {n}}}")
        else:
            print("Chưa có khóa được tạo. Vui lòng tạo khóa trước khi giải mã.")
            return
        
        ciphertext = int(input("\nNhập thông điệp đã mã hóa (dạng số nguyên): "))
        
        if ciphertext < 0 or ciphertext >= n:
            print(f"Lỗi: Thông điệp đã mã hóa phải nằm trong khoảng [0, {n-1}]")
            return
        
        plaintext = decrypt(ciphertext, d, n, logger)
        print(f"\nThông điệp gốc: {plaintext}")
        
    except ValueError as e:
        print(f"Lỗi: {e}")

