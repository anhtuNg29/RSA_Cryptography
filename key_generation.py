from utils import gcd, mod_inverse

def generate_keys(p, q, logger=None):
    """
    Tạo khóa RSA từ hai số nguyên tố p và q
    
    Args:
        p, q: Hai số nguyên tố
        logger: Đối tượng logger để ghi log (tùy chọn)
        
    Returns:
        Tuple (n, e, d, phi_n) - Các thông số của khóa RSA
    """
    # Tính n = p*q
    n = p * q
    
    # Tính phi(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    print(f"\nCác thông số đã tính toán:")
    print(f"n = p * q = {p} * {q} = {n}")
    print(f"φ(n) = (p-1)(q-1) = ({p}-1)({q}-1) = {phi_n}")
    
    # Chọn e sao cho 1 < e < phi(n) và gcd(e, phi(n)) = 1
    print("\nBây giờ bạn cần chọn e sao cho:")
    print("1. 1 < e < φ(n)")
    print("2. gcd(e, φ(n)) = 1 (e và φ(n) nguyên tố cùng nhau)")
    
    while True:
        try:
            e = int(input(f"\nNhập giá trị e (1 < e < {phi_n}): "))
            
            if e <= 1 or e >= phi_n:
                print(f"Lỗi: e phải nằm trong khoảng (1, {phi_n})")
                continue
                
            if gcd(e, phi_n) != 1:
                print(f"Lỗi: {e} và {phi_n} không nguyên tố cùng nhau. gcd({e}, {phi_n}) = {gcd(e, phi_n)}")
                continue
                
            break
            
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    
    # Tính d sao cho d*e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)
    
    print(f"\nTính toán d = e^(-1) mod φ(n) = {e}^(-1) mod {phi_n} = {d}")
    print(f"Kiểm tra: (d*e) mod φ(n) = ({d}*{e}) mod {phi_n} = {(d*e) % phi_n}")
    
    # In ra cặp khóa theo định dạng yêu cầu
    print("\n" + "=" * 50)
    print("CẶP KHÓA RSA ĐÃ TẠO THÀNH CÔNG:")
    print("=" * 50)
    print(f"Khóa công khai: PU = {{e, n}} = {{{e}, {n}}}")
    print(f"Khóa riêng:    PR = {{d, n}} = {{{d}, {n}}}")
    print("=" * 50)
    
    # Ghi log nếu có logger
    if logger:
        logger.log_key_generation(p, q, n, phi_n, e, d)
    
    return (n, e, d, phi_n)
