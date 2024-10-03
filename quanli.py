import pandas as pd

class NguoiQuanLi:
    def __init__(self, csv_file):
        # Đọc file CSV khi khởi tạo đối tượng
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)

        # Xử lý khoảng trắng và chữ hoa/thường cho cột 'Item'
        self.df['Item'] = self.df['Item'].str.strip().str.lower()

    def menu(self):
        # Hiển thị danh sách lựa chọn cho người quản lý
        print("\nChọn một tùy chọn:")
        print("1. Đọc số lượng hàng nhập")
        print("2. Đọc số lượng hàng bán")
        print("3. Tính lợi nhuận/thua lỗ")
        print("4. Kiểm tra hàng bán > nhập")
        print("5. Kiểm tra hàng bán < nhập")

        choice = int(input("Nhập lựa chọn của bạn (1-5): "))

        if choice == 1:
            self.doc_so_luong_hang_nhap()
        elif choice == 2:
            self.doc_so_luong_hang_ban()
        elif choice == 3:
            self.tinh_loi_nhuan_thua_lo()
        elif choice == 4:
            self.kiem_tra_hang_ban_lon_hon_nhap()
        elif choice == 5:
            self.kiem_tra_hang_ban_nho_hon_nhap()
        else:
            print("Lựa chọn không hợp lệ.")

    # Lựa chọn 1: Đọc số lượng hàng nhập
    def doc_so_luong_hang_nhap(self):
        print("\nSố lượng hàng nhập:")
        print(self.df[['Item', 'Quantity', 'Quantity imported']])

    # Lựa chọn 2: Đọc số lượng hàng bán
    def doc_so_luong_hang_ban(self):
        print("\nSố lượng hàng bán:")
        print(self.df[['Item', 'Sales quantity']])

    # Lựa chọn 3: Tính lợi nhuận/thua lỗ
    def tinh_loi_nhuan_thua_lo(self):
        # Tính lợi nhuận cho từng mặt hàng
        self.df['Profit/Loss'] = (self.df['Price sell'] - self.df['Price buy']) * self.df['Sales quantity']
        print("\nLợi nhuận/thua lỗ cho từng mặt hàng:")
        print(self.df[['Item', 'Profit/Loss']])

    # Lựa chọn 4: Kiểm tra hàng bán > nhập
    def kiem_tra_hang_ban_lon_hon_nhap(self):
        print("\nMặt hàng có số lượng bán > số lượng nhập:")
        sold_more_than_imported = self.df[self.df['Sales quantity'] > self.df['Quantity']]
        if not sold_more_than_imported.empty:
            print(sold_more_than_imported[['Item', 'Sales quantity', 'Quantity']])
        else:
            print("Không có mặt hàng nào bán nhiều hơn số lượng nhập.")

    # Lựa chọn 5: Kiểm tra hàng bán < nhập
    def kiem_tra_hang_ban_nho_hon_nhap(self):
        print("\nMặt hàng có số lượng bán < số lượng nhập:")
        sold_less_than_imported = self.df[self.df['Sale quantity'] < self.df['Quantity']]
        if not sold_less_than_imported.empty:
            print(sold_less_than_imported[['Item', 'Sale quantity', 'Quantity']])
        else:
            print("Không có mặt hàng nào bán ít hơn số lượng nhập.")


# Tạo đối tượng quản lý và hiển thị menu
# quan_ly = NguoiQuanLi('data.csv')
# quan_ly.menu()
