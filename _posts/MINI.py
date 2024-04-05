import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# 데이터베이스 연결 설정
def create_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # MySQL 사용자 이름
            passwd='your_password',  # MySQL 비밀번호
            database='InventorySystem'
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# 로그인 검증 함수
def verify_login(username, password):
    # 실제 어플리케이션에서는 여기서 데이터베이스를 조회해야 합니다.
    # 예시를 위해 하드코딩된 값을 사용합니다.
    if username == "admin" and password == "admin":
        return True
    else:
        return False

# 로그인 성공 시 호출될 함수
def login_success():
    login_window.destroy()
    create_main_window()

# 로그인 함수
def login():
    username = username_entry.get()
    password = password_entry.get()
    if verify_login(username, password):
        messagebox.showinfo("로그인 성공", "로그인에 성공하였습니다.")
        login_success()
    else:
        messagebox.showerror("로그인 실패", "사용자 이름 또는 비밀번호가 잘못되었습니다.")

# 메인 윈도우 생성 함수
def create_main_window():
    root = tk.Tk()
    root.title("재고 관리 시스템")

    # 여기에 메인 윈도우 구성 요소를 추가합니다.
    # (생략)

    root.mainloop()

# 로그인 윈도우 생성
login_window = tk.Tk()
login_window.title("로그인")

tk.Label(login_window, text="사용자 이름:").grid(row=0, column=0)
tk.Label(login_window, text="비밀번호:").grid(row=1, column=0)

username_entry = tk.Entry(login_window)
password_entry = tk.Entry(login_window, show="*")

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

tk.Button(login_window, text="로그인", command=login).grid(row=2, column=0, columnspan=2)

login_window.mainloop()
이게 데이터베이스 코드고

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import tkinter.simpledialog as simpledialog

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('재고 관리 시스템')
        self.db_connection = self.connect_to_db()
        
        self.setup_ui()
        self.create_menu()
    def create_menu(self):
        # 메뉴바 생성
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # 재고 메뉴
        stock_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="재고 관리", menu=stock_menu)
        stock_menu.add_command(label="재고 입고", command=self.stock_in)
        stock_menu.add_command(label="재고 출고", command=self.stock_out)
        stock_menu.add_separator()

    def stock_in(self):
        # 재고 입고 정보 입력받기
        product_id = simpledialog.askinteger("재고 입고", "제품번호:")
        quantity = simpledialog.askinteger("재고 입고", "입고량 입력:")
        if product_id is None or quantity is None:
            return  # 사용자가 취소하거나 입력하지 않은 경우

        # 데이터베이스에 재고 입고 반영
        if self.db_connection:
            cursor = self.db_connection.cursor()
            update_query = """
            UPDATE Product 
            SET Quantity = Quantity + %s
            WHERE ProductId = %s
            """
            try:
                cursor.execute(update_query, (quantity, product_id))
                self.db_connection.commit()
                messagebox.showinfo("Success", "재고가 성공적으로 입고되었습니다.")
            except Error as e:
                messagebox.showerror("Error", str(e))
            finally:
                cursor.close()

        self.load_products_from_db()  # 제품 목록 갱신

        
    def stock_out(self):
        # 재고 출고 정보 입력받기
        product_id = simpledialog.askinteger("재고 출고", "제품 ID 입력:")
        quantity = simpledialog.askinteger("재고 출고", "출고량 입력:")
        if product_id is None or quantity is None:
            return  # 사용자가 취소하거나 입력하지 않은 경우

        # 데이터베이스에 재고 출고 반영
        if self.db_connection:
            cursor = self.db_connection.cursor()
            update_query = """
            UPDATE Product 
            SET Quantity = Quantity - %s
            WHERE ProductId = %s
            """
            try:
                cursor.execute(update_query, (quantity, product_id))
                self.db_connection.commit()
                messagebox.showinfo("Success", "재고가 성공적으로 출고되었습니다.")
            except Error as e:
                messagebox.showerror("Error", str(e))
            finally:
                cursor.close()

        self.load_products_from_db()  # 제품 목록 갱신
 
    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',  # 실제 호스트 주소로 변경
                user='root',       # 실제 사용자 이름으로 변경
                password='3607',   # 실제 비밀번호로 변경
                database='schoolsuppliesdb'  # 실제 데이터베이스 이름으로 변경
            )
            return connection
        except Error as e:
            messagebox.showerror("Database Connection Error", str(e))
            return None

    def setup_ui(self):
        # 제품 목록 프레임
        self.frame_products = tk.Frame(self.root)
        self.frame_products.pack(fill=tk.BOTH, expand=True)

        columns = ('Product ID', 'Product Name', 'Product Code', 'Category', 'Supplier Price', 'Retail Price', 'Initial Stock', 'Quantity')
        self.tree_products = ttk.Treeview(self.frame_products, columns=columns, show='headings')
        for col in columns:
            self.tree_products.heading(col, text=col)
            self.tree_products.column(col, anchor=tk.CENTER)
        self.tree_products.pack(fill=tk.BOTH, expand=True)

        # 제품 추가 프레임
        self.frame_add_product = tk.Frame(self.root)
        self.frame_add_product.pack(fill=tk.X, pady=10)

        self.inputs = {}
        labels = ['Product Name', 'Product Code', 'Category', 'Supplier Price', 'Retail Price', 'Initial Stock', 'Quantity']
        for i, label in enumerate(labels):
            tk.Label(self.frame_add_product, text=label).grid(row=i, column=0, sticky=tk.W)
            entry = tk.Entry(self.frame_add_product)
            entry.grid(row=i, column=1, sticky=tk.EW)
            self.inputs[label] = entry

        self.frame_add_product.grid_columnconfigure(1, weight=1)

        self.btn_add_product = tk.Button(self.frame_add_product, text='Add Product', command=self.add_product_to_db)
        self.btn_add_product.grid(row=len(labels), column=0, columnspan=2, sticky=tk.EW)

        self.load_products_from_db()

    def load_products_from_db(self):
        for i in self.tree_products.get_children():
            self.tree_products.delete(i)

        if self.db_connection:
            cursor = self.db_connection.cursor()
            query = "SELECT ProductId, ProductName, ProductCode, Category, SupplierPrice, RetailPrice, InitialStock, Quantity FROM Product"
            cursor.execute(query)
            for row in cursor.fetchall():
                self.tree_products.insert('', tk.END, values=row)
            cursor.close()

    def add_product_to_db(self):
        if self.db_connection:
            data = [self.inputs[label].get() for label in self.inputs]
            query = "INSERT INTO Product (ProductName, ProductCode, Category, SupplierPrice, RetailPrice, InitialStock, Quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor = self.db_connection.cursor()
            try:
                cursor.execute(query, data)
                self.db_connection.commit()
                messagebox.showinfo("Success", "Product successfully added")
            except Error as e:
                messagebox.showerror("Error", str(e))
            finally:
                cursor.close()
                for entry in self.inputs.values():
                    entry.delete(0, tk.END)
                self.tree_products.delete(*self.tree_products.get_children())
                self.load_products_from_db()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()


