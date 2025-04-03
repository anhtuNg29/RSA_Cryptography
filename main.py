from prime_check import get_prime_input
from key_generation import generate_keys
from encryption import encrypt_message
from decryption import decrypt_message
from text_rsa_implementation import encrypt_text_message, decrypt_text_message
from logger import Logger
import os

def main():
    # Tạo logger
    logger = Logger()
    print(f"Kết quả sẽ được lưu vào file: {logger.get_log_filename()}")
    
    print("=" * 60)
    print("| " + "CHƯƠNG TRÌNH MÃ HÓA/GIẢI MÃ RSA".center(56) + " |")
    print("=" * 60)
    logger.log("CHƯƠNG TRÌNH MÃ HÓA/GIẢI MÃ RSA")
    
    # Biến lưu trữ khóa
    current_keys = None
    
    # Bước 1: Nhập p, q và kiểm tra tính nguyên tố
    print("\nBước 1: Nhập hai số nguyên tố p và q")
    logger.log("\nBước 1: Nhập hai số nguyên tố p và q")
    p = get_prime_input("Nhập số nguyên tố p: ")
    q = get_prime_input("Nhập số nguyên tố q: ")
    
    # Bước 2: Tạo khóa RSA
    print("\nBước 2: Tạo khóa RSA")
    logger.log("\nBước 2: Tạo khóa RSA")
    n, e, d, phi_n = generate_keys(p, q, logger)
    current_keys = {'n': n, 'e': e, 'd': d, 'phi_n': phi_n}
    
    # Lưu thông tin cho phiên mã hóa/giải mã văn bản
    current_block_size = None
    current_encrypted_blocks = None
    
    # Bước 3: Menu chức năng
    while True:
        print("\n" + "=" * 60)
        print("| " + "MENU CHỨC NĂNG".center(56) + " |")
        print("=" * 60)
        print("1. Mã hóa số nguyên")
        print("2. Giải mã số nguyên")
        print("3. Mã hóa văn bản")
        print("4. Giải mã văn bản")
        print("5. Hiển thị lại cặp khóa")
        print("6. Tạo cặp khóa mới")
        print("7. Mở file log hiện tại")
        print("8. Thoát")
        
        choice = input("\nNhập lựa chọn của bạn (1-8): ")
        
        if choice == '1':
            print("\n--- MÃ HÓA RSA (SỐ NGUYÊN) ---")
            logger.log("\n--- MÃ HÓA RSA (SỐ NGUYÊN) ---")
            if current_keys:
                encrypt_message(current_keys, logger)
            else:
                print("Chưa có khóa nào được tạo! Vui lòng tạo khóa trước.")
                logger.log("Yêu cầu mã hóa nhưng chưa có khóa nào được tạo")
        elif choice == '2':
            print("\n--- GIẢI MÃ RSA (SỐ NGUYÊN) ---")
            logger.log("\n--- GIẢI MÃ RSA (SỐ NGUYÊN) ---")
            if current_keys:
                decrypt_message(current_keys, logger)
            else:
                print("Chưa có khóa nào được tạo! Vui lòng tạo khóa trước.")
                logger.log("Yêu cầu giải mã nhưng chưa có khóa nào được tạo")
        elif choice == '3':
            print("\n--- MÃ HÓA RSA (VĂN BẢN) ---")
            logger.log("\n--- MÃ HÓA RSA (VĂN BẢN) ---")
            if current_keys:
                result = encrypt_text_message(current_keys, logger)
                if result:
                    current_encrypted_blocks, current_block_size = result
            else:
                print("Chưa có khóa nào được tạo! Vui lòng tạo khóa trước.")
                logger.log("Yêu cầu mã hóa văn bản nhưng chưa có khóa nào được tạo")
        elif choice == '4':
            print("\n--- GIẢI MÃ RSA (VĂN BẢN) ---")
            logger.log("\n--- GIẢI MÃ RSA (VĂN BẢN) ---")
            if current_keys:
                # Tùy chọn sử dụng kết quả mã hóa trước đó
                if current_encrypted_blocks and current_block_size:
                    use_previous = input("Bạn có muốn sử dụng kết quả mã hóa văn bản trước đó không? (y/n): ")
                    if use_previous.lower() == 'y':
                        print(f"\nSử dụng khóa riêng: PR = {{d, n}} = {{{current_keys['d']}, {current_keys['n']}}}")
                        print("\nCác khối đã mã hóa từ lần trước:")
                        for i, block in enumerate(current_encrypted_blocks):
                            print(f"C{i+1}: {block}")
                        plaintext = decrypt_text(current_encrypted_blocks, current_keys['d'], current_keys['n'], current_block_size, logger)
                        print(f"\nVăn bản đã giải mã: {plaintext}")
                        continue
                
                decrypt_text_message(current_keys, logger)
            else:
                print("Chưa có khóa nào được tạo! Vui lòng tạo khóa trước.")
                logger.log("Yêu cầu giải mã văn bản nhưng chưa có khóa nào được tạo")
        elif choice == '5':
            if current_keys:
                print("\n" + "=" * 50)
                print("CẶP KHÓA RSA HIỆN TẠI:")
                print("=" * 50)
                print(f"Khóa công khai: PU = {{e, n}} = {{{current_keys['e']}, {current_keys['n']}}}")
                print(f"Khóa riêng:    PR = {{d, n}} = {{{current_keys['d']}, {current_keys['n']}}}")
                print("=" * 50)
                logger.log("\nHiển thị lại cặp khóa hiện tại")
            else:
                print("\nChưa có cặp khóa nào được tạo!")
                logger.log("\nYêu cầu hiển thị khóa nhưng chưa có khóa nào được tạo")
        elif choice == '6':
            print("\n--- TẠO CẶP KHÓA MỚI ---")
            logger.log("\n--- TẠO CẶP KHÓA MỚI ---")
            p = get_prime_input("Nhập số nguyên tố p: ")
            q = get_prime_input("Nhập số nguyên tố q: ")
            n, e, d, phi_n = generate_keys(p, q, logger)
            current_keys = {'n': n, 'e': e, 'd': d, 'phi_n': phi_n}
            
            # Reset thông tin mã hóa văn bản khi tạo khóa mới
            current_block_size = None
            current_encrypted_blocks = None
        elif choice == '7':
            print(f"\nMở file log: {logger.get_log_filename()}")
            try:
                # Mở file log với trình xem mặc định của hệ điều hành
                if os.name == 'nt':  # Windows
                    os.system(f'start {logger.get_log_filename()}')
                elif os.name == 'posix':  # macOS, Linux
                    os.system(f'open {logger.get_log_filename()}')
                else:
                    print("Không thể tự động mở file. Vui lòng mở thủ công tại:", logger.get_log_filename())
            except Exception as e:
                print(f"Lỗi khi mở file: {e}")
        elif choice == '8':
            print("\nCảm ơn bạn đã sử dụng chương trình!")
            logger.log("\nKết thúc phiên làm việc")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-8.")

if __name__ == "__main__":
    main()