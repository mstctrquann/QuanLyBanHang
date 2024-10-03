import pandas as pd

# Đọc file CSV
class NguoiBanHang:
    def __init__(self, data):
        self.data = data

    def lay_gia(self, ten_san_pham):
        """Truy xuất giá của Item theo tên."""
        san_pham = self.data[self.data['Item'] == ten_san_pham]
        if not san_pham.empty:
            return san_pham.iloc[0]['Price sell']
        else:
            return f"Sản phẩm '{ten_san_pham}' không tồn tại."

    def ban_hang(self, ten_san_pham, so_luong_ban):
        """Xử lý bán hàng: giảm số lượng hàng trong kho và in thông tin."""
        san_pham = self.data[self.data['Item'] == ten_san_pham]
        if san_pham.empty:
            return f"Sản phẩm '{ten_san_pham}' không tồn tại."

        gia_tien = san_pham.iloc[0]['Price sell']
        so_luong_trong_kho = san_pham.iloc[0]['Quantity']
        so_luong_ban = int(so_luong_ban)

        if so_luong_ban > so_luong_trong_kho:
            return f"Không đủ số lượng sản phẩm '{ten_san_pham}' trong kho."

        # Cập nhật số lượng hàng trong kho sau khi bán
        self.data.loc[self.data['Item'] == ten_san_pham, 'Quantity'] -= so_luong_ban
        self.data.loc[self.data['Item'] == ten_san_pham, 'Sales quantity'] += so_luong_ban

        # In thông tin mua
        thanh_tien = gia_tien * so_luong_ban
        return {
            "Sản phẩm": ten_san_pham,
            "Giá tiền": gia_tien,
            "Số lượng mua": so_luong_ban,
            "Thành tiền": thanh_tien
        }

    def cap_nhat_file_csv(self):
        """Ghi dữ liệu đã cập nhật vào file CSV."""
        self.data.to_csv("quanlybanhang.csv", index=False)

    def in_hoa_don(self):
        """In hóa đơn với các thông tin Item, số lượng và tổng tiền."""
        hoa_don = self.data[self.data['Sales quantity'] > 0][['Item', 'Sales quantity', 'Price sell']]
        hoa_don['Thành tiền'] = hoa_don['Sales quantity'] * hoa_don['Price sell']
        tong_tien = hoa_don['Thành tiền'].sum()
        return hoa_don, tong_tien

    def reset_hoa_don(self):
        """Reset hóa đơn sau khi in bằng cách đặt lại Sales quantity về 0."""
        self.data['Sales quantity'] = 0
        self.cap_nhat_file_csv()  # Ghi lại file sau khi reset hóa đơn

# # Khởi tạo đối tượng quản lý bán hàng với dữ liệu từ file CSV
# quan_ly_ban_hang = NguoiBanHang(df)

# # Danh sách để lưu thông tin bán hàng
# thong_tin_ban_hang = []

# while True:
#     print("\nChọn lựa:")
#     print("1 = Thêm sản phẩm")
#     print("2 = Kết thúc và in hóa đơn")
    
#     lua_chon = input("Nhập lựa chọn của bạn (1 hoặc 2): ")

#     if lua_chon == '1':
#         ten_san_pham = input("Nhập tên sản phẩm: ")
#         while True:
#             try:
#                 so_luong_ban = int(input("Nhập số lượng hàng bán: "))
#                 if so_luong_ban <= 0:
#                     print("Số lượng phải lớn hơn 0. Vui lòng nhập lại.")
#                     continue
#                 break
#             except ValueError:
#                 print("Vui lòng nhập số lượng hợp lệ.")

#         # Thực hiện bán hàng
#         ket_qua_ban = quan_ly_ban_hang.ban_hang(ten_san_pham, so_luong_ban)

#         # Kiểm tra và lưu thông tin bán hàng
#         if isinstance(ket_qua_ban, dict):
#             thong_tin_ban_hang.append(ket_qua_ban)
#             print("Thông tin bán hàng:", ket_qua_ban)
#         else:
#             print(ket_qua_ban)  # In ra thông báo lỗi

#     elif lua_chon == '2':
#         # Cập nhật file CSV
#         quan_ly_ban_hang.cap_nhat_file_csv()

#         # Hiển thị kết quả và in hóa đơn
#         hoa_don, tong_tien = quan_ly_ban_hang.in_hoa_don()
#         print("\nHóa đơn:\n", hoa_don)
#         print("Tổng tiền:", tong_tien)

#         # Reset hóa đơn mới
#         quan_ly_ban_hang.reset_hoa_don()  # Gọi hàm reset đúng cách
#         thong_tin_ban_hang.clear()  # Xóa danh sách thông tin bán hàng cho khách hàng tiếp theo
#         print("Thông tin bán hàng đã được làm mới! Xin mời khách hàng tiếp theo.")

#     else:
#         print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
