import pdfplumber
import pandas as pd
import time
start = time.time()
# Đường dẫn đến file PDF
pdf_path = 'D:\SaoKePython\Thong tin so tien ung ho qua so tai khoan BIDV 1261122666 tu ngay 01.09 den 12.09.2024.pdf'
# Đường dẫn đến file CSV sẽ xuất ra
csv_output = 'duong_dan_xuat_ra.csv'

# Mở file PDF
with pdfplumber.open(pdf_path) as pdf:
    all_tables = []
    
    # Duyệt qua từng trang
    for page in pdf.pages:
        # Trích xuất bảng từ trang
        tables = page.extract_tables()
        
        # Nếu có bảng trên trang, thêm vào danh sách
        for table in tables:
            # Thêm bảng vào danh sách
            all_tables.append(table)
        break
    # Chuyển đổi dữ liệu bảng thành DataFrame và lưu thành CSV
    for idx, table in enumerate(all_tables):
        df = pd.DataFrame(table)
        df.to_csv(f'table_{idx+1}_{csv_output}', index=False, header=False)

print("Đã xuất dữ liệu ra CSV.")
end = time.time()

print(f"Thời gian chạy: {end-start}")