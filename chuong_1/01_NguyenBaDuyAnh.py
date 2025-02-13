import sqlite3
# Kết nối đến SQLite (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

# Tạo bảng NhanVien
cursor.execute('''
    CREATE TABLE IF NOT EXISTS NhanVien (
        MaNV INTEGER PRIMARY KEY,
        HoTen TEXT NOT NULL,
        Tuoi INTEGER NOT NULL,
        PhongBan TEXT NOT NULL
    )
''')

# Dữ liệu cần chèn vào bảng
nhanvien_data = [
    (1, 'Nguyen Van A', 30, 'Ke Toan'),
    (2, 'Tran Thi B', 25, 'Nhan Su'),
    (3, 'Le Van C', 28, 'IT'),
    (4, 'Pham Thi D', 32, 'Ke Toan'),
    (5, 'Vu Van E', 26, 'IT'),
    (6, 'Nguyen Thi F', 29, 'Marketing'),
    (7, 'Le Thi G', 27, 'Nhan Su'),
    (8, 'Hoang Van H', 35, 'Ke Toan'),
    (9, 'Pham Van I', 33, 'Marketing'),
    (10, 'Tran Van J', 24, 'IT'),
    (11, 'Dang Thi K', 31, 'Nhan Su'),
    (12, 'Nguyen Van L', 28, 'Ke Toan'),
    (13, 'Tran Thi M', 26, 'Marketing'),
    (14, 'Pham Van N', 30, 'Nhan Su'),
    (15, 'Hoang Thi O', 27, 'IT')
]
# Chèn dữ liệu vào bảng
cursor.executemany("INSERT INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan) VALUES (?, ?, ?, ?)", nhanvien_data)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
print("Dữ liệu đã được chèn thành công!")

# 3. Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien
cursor.execute("SELECT * FROM NhanVien")
info=cursor.fetchall()
print("Thông tin của nhân viên:",info)

# 4.Lấy HoTen và Tuoi của nhân viên trong phòng IT
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
it_employees = cursor.fetchall()
print("Nhân viên phòng IT:", it_employees)

# 5. Tìm nhân viên có độ tuổi lớn hơn 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
employees_above_25 = cursor.fetchall()
print("Nhân viên trên 25 tuổi:", employees_above_25)

# 6. Cho biết nhân viên lớn tuổi nhất của các PhongBan
cursor.execute('''
    SELECT PhongBan, HoTen, MAX(Tuoi) 
    FROM NhanVien 
    GROUP BY PhongBan
''')
oldest_per_department = cursor.fetchall()
print("Nhân viên lớn tuổi nhất theo phòng ban:", oldest_per_department)

# 7. Chuyển đổi thông tin PhongBan của nhân viên " Le Van C " từ "IT" sang "Marketing"
cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE HoTen = 'Le Van C'")
cursor.execute('''SELECT * FROM NhanVien WHERE HoTen="Le Van C"''')
rows=cursor.fetchall()
for row in rows:
    print(row)
    
# 8. Xóa nhân viên có MaNV = 2
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")

# Đếm số nhân viên theo từng phòng ban
cursor.execute("SELECT PhongBan, COUNT(*) FROM NhanVien GROUP BY PhongBan")
department_counts = cursor.fetchall()
print("Số nhân viên theo phòng ban:", department_counts)

cursor.execute("SELECT * FROM NhanVien WHERE HoTen LIKE '%Nguyen%'")
nguyen_employees = cursor.fetchall()
print("Nhân viên có tên chứa 'Nguyen':", nguyen_employees)
