import os
import datetime

class Logger:
    def __init__(self):
        """Khởi tạo logger"""
        self.output_dir = 'output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Tạo tên file log dựa trên thời gian hiện tại
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.output_dir, f"rsa_session_{timestamp}.txt")
        
        # Khởi tạo file log
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=== PHIÊN LÀM VIỆC VỚI RSA ===\n")
            f.write(f"Thời gian bắt đầu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    def log(self, message):
        """Ghi thông điệp vào file log"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(message + "\n")
    
    def log_key_generation(self, p, q, n, phi_n, e, d):
        """Ghi thông tin về quá trình tạo khóa"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("SINH KHÓA RSA\n")
            f.write("="*50 + "\n")
            f.write(f"Số nguyên tố p: {p}\n")
            f.write(f"Số nguyên tố q: {q}\n")
            f.write(f"n = p * q = {p} * {q} = {n}\n")
            f.write(f"φ(n) = (p-1)(q-1) = ({p}-1)({q}-1) = {phi_n}\n")
            f.write(f"Khóa công khai e: {e}\n")
            f.write(f"Khóa bí mật d: {d}\n")
            f.write(f"Kiểm tra: (d*e) mod φ(n) = ({d}*{e}) mod {phi_n} = {(d*e) % phi_n}\n\n")
            f.write(f"Khóa công khai: PU = {{e, n}} = {{{e}, {n}}}\n")
            f.write(f"Khóa riêng:    PR = {{d, n}} = {{{d}, {n}}}\n")
            f.write("="*50 + "\n")
    
    def log_encryption(self, plaintext, e, n, ciphertext):
        """Ghi thông tin về quá trình mã hóa số nguyên"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("MÃ HÓA RSA (SỐ NGUYÊN)\n")
            f.write("="*50 + "\n")
            f.write(f"Thông điệp gốc (M): {plaintext}\n")
            f.write(f"Sử dụng khóa công khai: PU = {{e, n}} = {{{e}, {n}}}\n")
            f.write(f"Công thức mã hóa: C = M^e mod n = {plaintext}^{e} mod {n}\n")
            f.write(f"Kết quả mã hóa (C): {ciphertext}\n")
            f.write("="*50 + "\n")
    
    def log_decryption(self, ciphertext, d, n, plaintext):
        """Ghi thông tin về quá trình giải mã số nguyên"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("GIẢI MÃ RSA (SỐ NGUYÊN)\n")
            f.write("="*50 + "\n")
            f.write(f"Thông điệp đã mã hóa (C): {ciphertext}\n")
            f.write(f"Sử dụng khóa riêng: PR = {{d, n}} = {{{d}, {n}}}\n")
            f.write(f"Công thức giải mã: M = C^d mod n = {ciphertext}^{d} mod {n}\n")
            f.write(f"Kết quả giải mã (M): {plaintext}\n")
            f.write("="*50 + "\n")
    
    def log_text_encryption(self, plaintext, e, n, plaintext_blocks, ciphertext_blocks):
        """Ghi thông tin về quá trình mã hóa văn bản"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("MÃ HÓA RSA (VĂN BẢN)\n")
            f.write("="*50 + "\n")
            f.write(f"Văn bản gốc: {plaintext}\n")
            f.write(f"Sử dụng khóa công khai: PU = {{e, n}} = {{{e}, {n}}}\n\n")
            f.write("Chuyển đổi văn bản thành các khối số:\n")
            for i, block in enumerate(plaintext_blocks):
                f.write(f"P{i+1} = {block}\n")
            f.write("\nMã hóa từng khối:\n")
            for i, (p_block, c_block) in enumerate(zip(plaintext_blocks, ciphertext_blocks)):
                f.write(f"C{i+1} = {p_block}^{e} mod {n} = {c_block}\n")
            f.write("="*50 + "\n")
    
    def log_text_decryption(self, ciphertext_blocks, d, n, plaintext_blocks, plaintext):
        """Ghi thông tin về quá trình giải mã văn bản"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("GIẢI MÃ RSA (VĂN BẢN)\n")
            f.write("="*50 + "\n")
            f.write(f"Sử dụng khóa riêng: PR = {{d, n}} = {{{d}, {n}}}\n\n")
            f.write("Các khối đã mã hóa:\n")
            for i, block in enumerate(ciphertext_blocks):
                f.write(f"C{i+1} = {block}\n")
            f.write("\nGiải mã từng khối:\n")
            for i, (c_block, p_block) in enumerate(zip(ciphertext_blocks, plaintext_blocks)):
                f.write(f"P{i+1} = {c_block}^{d} mod {n} = {p_block}\n")
            f.write(f"\nVăn bản đã giải mã: {plaintext}\n")
            f.write("="*50 + "\n")
    
    def get_log_filename(self):
        """Trả về tên file log hiện tại"""
        return self.log_file