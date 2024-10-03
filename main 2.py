import pandas as pd
from nguoibanhang2 import NguoiBanHang
from nhaphang import NguoiNhapHang
from quanli import NguoiQuanLi
df = pd.read_csv('Manage.csv', encoding='utf-8-sig')
def main():
    print("Chọn tư cách đăng nhập:")
    print("1. Người bán hàng")
    print("2. Người nhập hàng")
    print("3. Người quản lý")
    
    role = int(input("Nhập tư cách đăng nhập (1-3): "))

    if role == 1:
        # Khởi tạo đối tượng quản lý bán hàng với dữ liệu từ file CSV
        quan_ly_ban_hang = NguoiBanHang(df)
        # Danh sách để lưu thông tin bán hàng
        thong_tin_ban_hang = []
        while True:
            print("\nChọn lựa:")
            print("1 = Thêm sản phẩm")
            print("2 = Kết thúc và in hóa đơn")
            
            lua_chon = input("Nhập lựa chọn của bạn (1 hoặc 2): ")

            if lua_chon == '1':
                ten_san_pham = input("Nhập tên sản phẩm: ")
                while True:
                    try:
                        so_luong_ban = int(input("Nhập số lượng hàng bán: "))
                        if so_luong_ban <= 0:
                            print("Số lượng phải lớn hơn 0. Vui lòng nhập lại.")
                            continue
                        break
                    except ValueError:
                        print("Vui lòng nhập số lượng hợp lệ.")

                # Thực hiện bán hàng
                ket_qua_ban = quan_ly_ban_hang.ban_hang(ten_san_pham, so_luong_ban)

                # Kiểm tra và lưu thông tin bán hàng
                if isinstance(ket_qua_ban, dict):
                    thong_tin_ban_hang.append(ket_qua_ban)
                    print("Thông tin bán hàng:", ket_qua_ban)
                else:
                    print(ket_qua_ban)  # In ra thông báo lỗi

            elif lua_chon == '2':
                # Cập nhật file CSV
                quan_ly_ban_hang.cap_nhat_file_csv()

                # Hiển thị kết quả và in hóa đơn
                hoa_don, tong_tien = quan_ly_ban_hang.in_hoa_don()
                print("\nHóa đơn:\n", hoa_don)
                print("Tổng tiền:", tong_tien)

                # Reset hóa đơn mới
                quan_ly_ban_hang.reset_hoa_don()  # Gọi hàm reset đúng cách
                thong_tin_ban_hang.clear()  # Xóa danh sách thông tin bán hàng cho khách hàng tiếp theo
                print("Thông tin bán hàng đã được làm mới! Xin mời khách hàng tiếp theo.")

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
    elif role == 2:
        nguoi_nhap_hang = NguoiNhapHang('Manage.csv')
        nguoi_nhap_hang.nhap_hang()
    elif role == 3:
        nguoi_quan_ly = NguoiQuanLi('Manage.csv')
        nguoi_quan_ly.menu()
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()