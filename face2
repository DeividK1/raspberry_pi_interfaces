import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Основен прозорец
root = tb.Window(themename="darkly")  # Избери тема (напр. "darkly", "cosmo", "flatly")
root.title("Модерен интерфейс")
root.geometry("600x400")

# Заглавие
title = tb.Label(root, text="Моето модерно приложение", font=("Helvetica", 20, "bold"))
title.pack(pady=20)

# Падащо меню
dropdown_var = tb.StringVar(value="Избери опция")
dropdown_menu = tb.Combobox(root, textvariable=dropdown_var, state="readonly", bootstyle="info")
dropdown_menu["values"] = ["Опция 1", "Опция 2", "Опция 3"]
dropdown_menu.pack(pady=10)

# Търсачка
search_frame = tb.Frame(root)
search_frame.pack(pady=20)

search_label = tb.Label(search_frame, text="Търси:", font=("Helvetica", 12))
search_label.pack(side="left", padx=5)

search_entry = tb.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)

def search_action():
    title.config(text=f"Резултат за: {search_entry.get()}")

search_button = tb.Button(search_frame, text="Търси", bootstyle="primary", command=search_action)
search_button.pack(side="left", padx=5)

# Секция с бутони
button_frame = tb.Frame(root)
button_frame.pack(pady=20)

def button_clicked(button_name):
    title.config(text=f"Натиснат бутон: {button_name}")

button1 = tb.Button(button_frame, text="Бутон 1", bootstyle="success", command=lambda: button_clicked("Бутон 1"))
button1.pack(side="left", padx=10)

button2 = tb.Button(button_frame, text="Бутон 2", bootstyle="info", command=lambda: button_clicked("Бутон 2"))
button2.pack(side="left", padx=10)

button3 = tb.Button(button_frame, text="Бутон 3", bootstyle="warning", command=lambda: button_clicked("Бутон 3"))
button3.pack(side="left", padx=10)

# Прогрес бар (добавя модерно усещане)
progress = tb.Progressbar(root, bootstyle="success", length=400, mode="indeterminate")
progress.pack(pady=20)
progress.start()

# Footer
footer = tb.Label(root, text="Създадено с ttkbootstrap", font=("Helvetica", 10))
footer.pack(side="bottom", pady=10)

# Стартиране на приложението
root.mainloop()
