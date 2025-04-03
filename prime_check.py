import random

def is_probably_prime(n, k=40):
    """
    Kiểm tra số nguyên tố bằng thuật toán Miller-Rabin
    
    Args:
        n: Số cần kiểm tra
        k: Số lần kiểm tra (càng cao càng chính xác)
        
    Returns:
        True nếu n có khả năng là số nguyên tố, False nếu n chắc chắn là hợp số
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Viết n-1 dưới dạng 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Thực hiện k lần kiểm tra Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def get_prime_input(prompt):
    """
    Nhận đầu vào từ người dùng và kiểm tra xem có phải số nguyên tố không
    
    Args:
        prompt: Thông báo hiển thị cho người dùng
        
    Returns:
        Số nguyên tố được nhập bởi người dùng
    """
    while True:
        try:
            num = int(input(prompt))
            if num <= 1:
                print("Vui lòng nhập số lớn hơn 1.")
                continue
                
            print(f"Đang kiểm tra tính nguyên tố của {num}...")
            if is_probably_prime(num):
                print(f"{num} là số nguyên tố.")
                return num
            else:
                print(f"{num} không phải là số nguyên tố. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
