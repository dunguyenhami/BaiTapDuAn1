import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Class chính cho ứng dụng
class LinearEquationSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải phương trình bậc nhất")
        self.root.geometry("300x250")  # Thiết lập kích thước cửa sổ

        # Font tùy chỉnh cho các thành phần
        self.font_style = font.Font(family="Arial", size=12)

        # Màu chữ
        self.text_color = "#000080"  # Màu xanh đậm cho chữ

        # Tạo LabelFrame để nhóm các trường nhập liệu
        input_frame = tk.LabelFrame(root, text="Nhập số liệu", padx=10, pady=10, font=self.font_style, fg=self.text_color)
        input_frame.pack(padx=10, pady=10)

        # Nhãn và trường nhập liệu cho a
        self.label_a = tk.Label(input_frame, text="Nhập a:", font=self.font_style, fg=self.text_color)
        self.label_a.grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(input_frame, font=self.font_style, fg=self.text_color)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        # Nhãn và trường nhập liệu cho b
        self.label_b = tk.Label(input_frame, text="Nhập b:", font=self.font_style, fg=self.text_color)
        self.label_b.grid(row=1, column=0, padx=5, pady=5)
        self.entry_b = tk.Entry(input_frame, font=self.font_style, fg=self.text_color)
        self.entry_b.grid(row=1, column=1, padx=5, pady=5)

        # Nút giải phương trình
        self.solve_button = tk.Button(root, text="Giải", command=self.solve_equation, font=self.font_style, bg="#FFCCFF", fg="black")
        self.solve_button.pack(pady=5)

        # Hiển thị kết quả
        self.result_label = tk.Label(root, text="Kết quả: ", font=self.font_style, fg=self.text_color)
        self.result_label.pack(pady=5)

        # Nút reset
        self.reset_button = tk.Button(root, text="Làm mới", command=self.reset_fields, font=self.font_style, bg="#0099FF", fg="black")
        self.reset_button.pack(pady=5)

    def solve_equation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())

            if a == 0:
                raise ValueError("Giá trị của a không thể bằng 0.")

            x = -b / a  # Giải phương trình ax + b = 0
            self.result_label.config(text=f"Kết quả: x = {x:.2f}")

        except ValueError as ve:
            messagebox.showerror("Lỗi nhập liệu", str(ve))
        except Exception as e:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho a và b.")

    def reset_fields(self):
        self.entry_a.delete(0, tk.END)  # Xóa trường a
        self.entry_b.delete(0, tk.END)  # Xóa trường b
        self.result_label.config(text="Kết quả: ")  # Đặt lại kết quả

# Tạo cửa sổ chính
if __name__ == "__main__":
    root = tk.Tk()
    app = LinearEquationSolver(root)  # Tạo đối tượng ứng dụng
    root.mainloop()
