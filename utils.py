def gcd(a, b):
    """
    Tìm ước chung lớn nhất của a và b bằng thuật toán Euclid
    
    Args:
        a, b: Hai số cần tìm UCLN
        
    Returns:
        UCLN của a và b
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Thuật toán Euclid mở rộng để tìm nghịch đảo modular
    
    Args:
        a, b: Hai số đầu vào
        
    Returns:
        Tuple (gcd, x, y) thỏa mãn ax + by = gcd
    """
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(e, phi):
    """
    Tìm nghịch đảo modular của e theo modulo phi
    
    Args:
        e: Số cần tìm nghịch đảo
        phi: Modulo
        
    Returns:
        Nghịch đảo modular của e theo modulo phi
    """
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Không tồn tại nghịch đảo modular")
    else:
        return (x % phi + phi) % phi

def square_and_multiply(base, exponent, modulus):
    """
    Thuật toán bình phương và nhân để tính (base^exponent) % modulus hiệu quả
    
    Args:
        base: Cơ số
        exponent: Số mũ
        modulus: Modulo
        
    Returns:
        (base^exponent) % modulus
    """
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # Nếu exponent lẻ, nhân result với base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # exponent = exponent / 2
        exponent = exponent >> 1
        
        # base = base^2
        base = (base * base) % modulus
    
    return result
