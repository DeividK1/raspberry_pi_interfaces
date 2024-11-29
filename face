import tkinter as tk
from tkinter import ttk

# Основен прозорец
root = tk.Tk()
root.title("Raspberry Pi Приложение")
root.geometry("800x480")  # Типичен размер за сензорен дисплей
root.resizable(False, False)  # Фиксиран размер за производителност

# Основен цвят и стилове
bg_color = "#f0f0f0"
root.configure(bg=bg_color)

# Стилове за елементи
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("TLabel", background=bg_color, font=("Arial", 16))
style.configure("TFrame", background=bg_color)
style.configure("TNotebook", padding=10)
style.configure("TNotebook.Tab", font=("Arial", 14), padding=[10, 5])

# Tabs - Раздели
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Начало")
notebook.add(tab2, text="Настройки")
notebook.add(tab3, text="Информация")
notebook.pack(fill="both", expand=True)

# Tab 1: Начало
header = ttk.Label(tab1, text="Управление на Програмата", font=("Arial", 20))
header.pack(pady=20)

# Бутонна секция
button_frame = ttk.Frame(tab1)
button_frame.pack(pady=20)

def start_action():
    status_label.config(text="Статус: Програмата е стартирана")

def stop_action():
    status_label.config(text="Статус: Програмата е спряна")

start_button = ttk.Button(button_frame, text="Стартирай", command=start_action)
start_button.grid(row=0, column=0, padx=20, pady=10)

stop_button = ttk.Button(button_frame, text="Спри", command=stop_action)
stop_button.grid(row=0, column=1, padx=20, pady=10)

status_label = ttk.Label(tab1, text="Статус: Неактивно", font=("Arial", 14))
status_label.pack(pady=10)

# Tab 2: Настройки
settings_header = ttk.Label(tab2, text="Настройки на Програмата", font=("Arial", 20))
settings_header.pack(pady=20)

resolution_label = ttk.Label(tab2, text="Резолюция на Екрана:")
resolution_label.pack(anchor="w", padx=20, pady=5)

resolution_combo = ttk.Combobox(tab2, values=["800x480", "1024x600", "1920x1080"], state="readonly")
resolution_combo.set("800x480")
resolution_combo.pack(anchor="w", padx=20, pady=5)

apply_button = ttk.Button(tab2, text="Приложи", command=lambda: print("Настройките са приложени"))
apply_button.pack(pady=20)

# Tab 3: Информация
info_header = ttk.Label(tab3, text="Информация за Програмата", font=("Arial", 20))
info_header.pack(pady=20)

info_text = tk.Text(tab3, height=10, width=60, wrap="word", bg="#ffffff", fg="#333333", font=("Arial", 12))
info_text.insert("1.0", "Това е програма за управление на проект, използвайки Raspberry Pi 5.\n\nРазработена с Python и Tkinter.")
info_text.config(state="disabled")  # Само за четене
info_text.pack(pady=10)

# Footer
footer = ttk.Label(root, text="Създадено за Raspberry Pi 5", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

# Стартиране на приложението
root.mainloop()
