import pandas as pd

class NguoiNhapHang:
    def __init__(self, csv_file):
        # Đọc file CSV
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)

        # Xử lý khoảng trắng và chữ hoa/thường cho cột 'Item'
        self.df['Item'] = self.df['Item'].str.strip().str.lower()

    # Hàm nhập mặt hàng
    def nhap_hang(self):
        # Nhập tên mặt hàng từ người dùng
        item_name = input("Nhập tên mặt hàng: ").strip().lower()

        # Kiểm tra sự tồn tại của mặt hàng
        if item_name in self.df['Item'].values:
            print(f"Mặt hàng '{item_name}' đã tồn tại.")
            
            # Nhập số lượng mới từ người dùng
            new_quantity = int(input(f"Nhập số lượng muốn thêm cho mặt hàng '{item_name}': "))
            
            # Cập nhật số lượng cho cột 'Additional import quantity'
            row_index = self.df[self.df['Item'] == item_name].index[0]
            self.df.at[row_index, 'Quantity imported'] += new_quantity
            
            # Lưu lại file CSV sau khi cập nhật
            self.df.to_csv(self.csv_file, index=False)
            print(f"Số lượng của mặt hàng '{item_name}' đã được cập nhật.")
        else:
            print(f"Mặt hàng '{item_name}' chưa tồn tại.")
            
            # Nếu chưa tồn tại, nhập thông tin cho sản phẩm mới
            self.them_san_pham_moi(item_name)

    # Hàm thêm sản phẩm mới
    def them_san_pham_moi(self, item_name):
        quantity = int(input("Nhập số lượng của sản phẩm mới: "))
        price_buy = int(input("Nhập giá mua: "))
        price_sell = int(input("Nhập giá bán: "))

        # Tạo chỉ số (index) mới
        new_index = self.df['Index'].max() + 1

        # Thêm sản phẩm mới vào DataFrame
        new_row = {
            'Index': new_index,
            'Item': item_name,
            'Quantity': quantity,
            'Sales quantity': 0,
            'Quantity imported': 0,
            'Price sell': price_sell,
            'Price buy': price_buy,
            'Quantity limit': 30
        }

        self.df = self.df._append(new_row, ignore_index=True)

        # Ghi lại DataFrame vào file CSV
        self.df.to_csv(self.csv_file, index=False)
        print(f"Sản phẩm mới '{item_name}' đã được thêm vào.")

# Tạo đối tượng người nhập hàng và thao tác
# nguoi_nhap_hang = NguoiNhapHang('Manage.csv')
# nguoi_nhap_hang.nhap_hang()

