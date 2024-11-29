import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class RaspberryPiApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Основни настройки на прозореца
        self.title("Raspberry Pi 5 Приложение")
        self.geometry("800x480")  # Типичен размер за сензорен дисплей
        self.resizable(False, False)
        self.configure(bg="#2E3440")  # Тъмен фон за модерна визия

        # Стилове за елементи
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14), padding=10)
        style.configure("TLabel", background="#2E3440", foreground="#ECEFF4", font=("Arial", 16))
        style.configure("TFrame", background="#2E3440")
        style.configure("TNotebook", background="#2E3440")
        style.configure("TNotebook.Tab", font=("Arial", 14), padding=[10, 5])

        # Раздели
        notebook = ttk.Notebook(self)
        tab_dashboard = ttk.Frame(notebook, style="TFrame")
        tab_settings = ttk.Frame(notebook, style="TFrame")
        tab_stats = ttk.Frame(notebook, style="TFrame")

        notebook.add(tab_dashboard, text="Табло")
        notebook.add(tab_settings, text="Настройки")
        notebook.add(tab_stats, text="Статистика")
        notebook.pack(fill="both", expand=True)

        # Tab 1: Табло
        self.create_dashboard(tab_dashboard)

        # Tab 2: Настройки
        self.create_settings(tab_settings)

        # Tab 3: Статистика
        self.create_stats(tab_stats)

        # Footer
        footer = ttk.Label(self, text="Създадено за Raspberry Pi 5", font=("Arial", 10), background="#2E3440", foreground="#ECEFF4")
        footer.pack(side="bottom", pady=5)

    def create_dashboard(self, parent):
        """Създава интерфейса на таблото."""
        header = ttk.Label(parent, text="Добре дошли в Програмата", style="TLabel")
        header.pack(pady=20)

        button_frame = ttk.Frame(parent, style="TFrame")
        button_frame.pack(pady=20)

        # Бутони за управление
        start_button = ttk.Button(button_frame, text="Стартирай", command=self.start_action)
        start_button.grid(row=0, column=0, padx=10, pady=10)

        stop_button = ttk.Button(button_frame, text="Спри", command=self.stop_action)
        stop_button.grid(row=0, column=1, padx=10, pady=10)

        # Статусен етикет
        self.status_label = ttk.Label(parent, text="Статус: Неактивно", style="TLabel")
        self.status_label.pack(pady=10)

    def create_settings(self, parent):
        """Създава интерфейса за настройките."""
        settings_header = ttk.Label(parent, text="Настройки на Програмата", style="TLabel")
        settings_header.pack(pady=20)

        resolution_label = ttk.Label(parent, text="Резолюция на екрана:", style="TLabel")
        resolution_label.pack(anchor="w", padx=20, pady=5)

        self.resolution_combo = ttk.Combobox(parent, values=["800x480", "1024x600", "1920x1080"], state="readonly")
        self.resolution_combo.set("800x480")
        self.resolution_combo.pack(anchor="w", padx=20, pady=5)

        apply_button = ttk.Button(parent, text="Приложи", command=self.apply_settings)
        apply_button.pack(pady=20)

    def create_stats(self, parent):
        """Създава интерфейса за статистика."""
        stats_header = ttk.Label(parent, text="Статистика", style="TLabel")
        stats_header.pack(pady=20)

        progress_label = ttk.Label(parent, text="Прогрес:", style="TLabel")
        progress_label.pack(pady=10)

        self.progress = ttk.Progressbar(parent, length=400, mode="determinate", maximum=100, value=50)
        self.progress.pack(pady=10)

    def start_action(self):
        """Действие за старт."""
        self.status_label.config(text="Статус: Програмата е стартирана")
        messagebox.showinfo("Информация", "Програмата е стартирана успешно!")

    def stop_action(self):
        """Действие за стоп."""
        self.status_label.config(text="Статус: Програмата е спряна")
        messagebox.showinfo("Информация", "Програмата е спряна успешно!")

    def apply_settings(self):
        """Прилагане на настройките."""
        resolution = self.resolution_combo.get()
        messagebox.showinfo("Настройки", f"Резолюцията е зададена на {resolution}")


# Стартиране на приложението
if __name__ == "__main__":
    app = RaspberryPiApp()
    app.mainloop()

