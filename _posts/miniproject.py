import tkinter as tk
from tkinter import ttk

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('재고 관리 시스템')

        # 제품 목록 프레임
        self.frame_products = tk.Frame(self.root)
        self.frame_products.pack(fill=tk.BOTH, expand=True)

        self.tree_products = ttk.Treeview(self.frame_products, columns=('Product ID', 'Product Name', 'Quantity'), show='headings')
        self.tree_products.heading('Product ID', text='제품 ID')
        self.tree_products.heading('Product Name', text='제품명')
        self.tree_products.heading('Quantity', text='수량')
        self.tree_products.pack(fill=tk.BOTH, expand=True)

        # 제품 추가 프레임
        self.frame_add_product = tk.Frame(self.root)
        self.frame_add_product.pack(fill=tk.X)

        tk.Label(self.frame_add_product, text='제품명:').pack(side=tk.LEFT, padx=(10, 2))
        self.entry_product_name = tk.Entry(self.frame_add_product)
        self.entry_product_name.pack(side=tk.LEFT, padx=(0, 10))

        tk.Label(self.frame_add_product, text='수량:').pack(side=tk.LEFT)
        self.entry_quantity = tk.Entry(self.frame_add_product)
        self.entry_quantity.pack(side=tk.LEFT, padx=(0, 10))

        self.btn_add_product = tk.Button(self.frame_add_product, text='제품 추가', command=self.add_product)
        self.btn_add_product.pack(side=tk.LEFT)

        # 샘플 데이터 추가
        self.insert_sample_data()

    def add_product(self):
        product_name = self.entry_product_name.get()
        quantity = self.entry_quantity.get()
        if product_name and quantity:
            product_id = len(self.tree_products.get_children()) + 1
            self.tree_products.insert('', tk.END, values=(product_id, product_name, quantity))
            self.entry_product_name.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)

    def insert_sample_data(self):
        # 샘플 데이터
        products = [
            (1, '연필', 100),
            (2, '볼펜', 200),
            (3, '지우개', 150),
        ]
        for product in products:
            self.tree_products.insert('', tk.END, values=product)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('재고 관리 시스템')

        # 데이터베이스 연결 및 테이블 생성
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()
        self.create_table()

        # GUI 구성
        # 생략된 부분은 이전 예제와 동일하므로, 주요 변경/추가된 부분만 나타냅니다.
        self.btn_add_product = tk.Button(self.frame_add_product, text='제품 추가', command=self.add_product_to_db)
        self.btn_add_product.pack(side=tk.LEFT)

        self.load_products_from_db()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS products
                     (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')
        self.conn.commit()

    def add_product_to_db(self):
        product_name = self.entry_product_name.get()
        quantity = self.entry_quantity.get()
        if product_name and quantity:
            self.c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, quantity))
            self.conn.commit()
            self.load_products_from_db()
            self.entry_product_name.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)

    def load_products_from_db(self):
        self.tree_products.delete(*self.tree_products.get_children())
        for row in self.c.execute('SELECT id, name, quantity FROM products'):
            self.tree_products.insert('', tk.END, values=row)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
