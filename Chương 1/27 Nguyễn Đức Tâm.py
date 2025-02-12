import sqlite3
#1 Tạo bảng

conn = sqlite3.connect("nhanvien.db")


cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
)
""")
conn.commit()

#2 Chèn bản ghi vào bảng
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

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


cursor.executemany("INSERT INTO NhanVien VALUES (?, ?, ?, ?)", nhanvien_data)
conn.commit()


cursor.execute("SELECT * FROM NhanVien")
rows = cursor.fetchall()


for row in rows:
    print(row)

conn.close()

#3 Lấy thông tin nhân viên trong bảng NhanVien
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM NhanVien
""")

cursor.fetchall()

#4 HoTen và Tuoi của các nhân viên trong phòng IT
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

query = """
SELECT HoTen,Tuoi
FROM NhanVien
Where PhongBan = 'IT'
"""
cursor.execute(query)
rows = cursor.fetchall()

print()
for row in rows:
    print(row)

conn.close()

#5 Nhân viên tuổi >25
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

query = """
SELECT MaNV,HoTen,Tuoi,PhongBan
FROM NhanVien
Where Tuoi > 25
"""
cursor.execute(query)
rows = cursor.fetchall()

print()
for row in rows:
    print(row)

conn.close()

#6 Nhân viên lớn tuổi nhất các phòng ban
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
query = """
SELECT PhongBan, Max(Tuoi) AS TuoiMax
FROM NhanVien
GROUP BY PhongBan
"""
cursor.execute(query)
rows = cursor.fetchall()

print()
for row in rows:
    print(row)

conn.close()

#7 Đổi Phòng Ban Lê Văn C sang Marketing
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
query = """
Update NhanVien
Set PhongBan = 'Marketing'
Where HoTen = 'Le Van C'
"""
conn.commit()
cursor.execute(query)
rows = cursor.fetchall()
print()
for row in rows:
    print(row)

conn.close()

# Hiện Lê Văn C
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
query = """
Select MaNV,HoTen,Tuoi,PhongBan
From NhanVien
Where HoTen = 'Le Van C'
"""
conn.commit()
cursor.execute(query)
rows = cursor.fetchall()
print()
for row in rows:
    print(row)

conn.close()

#8 Xóa nhân viên có “MaSV = 2”
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
query = """
Delete From NhanVien Where MaNV=2
"""
conn.commit()
cursor.execute(query)
rows = cursor.fetchall()
print()
for row in rows:
    print(row)

conn.close()

# Cho biết mỗi phòng ban có bao nhiêu người
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
query = """
Select PhongBan,Count(*)
From NhanVien
Group By PhongBan
"""
cursor.execute(query)
rows = cursor.fetchall()
print()
for row in rows:
    print(row)

conn.close()

#9 Các bước kết nối đến SQLite trong Python

import sqlite3

# 1. Kết nối đến database
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

# 2. Tạo bảng nếu chưa có
cursor.execute("""
CREATE TABLE IF NOT EXISTS NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
)
""")
conn.commit()

# 3. Chèn dữ liệu vào bảng
cursor.execute("INSERT INTO NhanVien VALUES (1, 'Nguyen Van A', 30, 'Ke Toan')")
conn.commit()

# 4. Truy vấn dữ liệu
cursor.execute("SELECT * FROM NhanVien")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. Đóng kết nối
conn.close()
