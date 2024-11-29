import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MinimalApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Основни настройки на прозореца
        self.title("Минимален интерфейс за Raspberry Pi")
        self.geometry("800x480")  # Типичен размер за сензорен дисплей
        self.resizable(False, False)

        # Главен фрейм с две секции
        self.main_frame = tk.Frame(self, bg="#1E1E2E")
        self.main_frame.pack(fill="both", expand=True)

        # Ляв панел - навигация
        self.nav_panel = tk.Frame(self.main_frame, bg="#2E3440", width=200)
        self.nav_panel.pack(side="left", fill="y")

        # Десен панел - съдържание
        self.content_panel = tk.Frame(self.main_frame, bg="#ECEFF4")
        self.content_panel.pack(side="right", fill="both", expand=True)

        # Създаване на навигация
        self.create_navigation()

        # Задаване на начален екран
        self.current_screen = None
        self.show_dashboard()

    def create_navigation(self):
        """Създава навигационни бутони."""
        title = tk.Label(
            self.nav_panel,
            text="Меню",
            font=("Arial", 18, "bold"),
            bg="#2E3440",
            fg="#ECEFF4",
            pady=20,
        )
        title.pack()

        dashboard_btn = tk.Button(
            self.nav_panel,
            text="Табло",
            font=("Arial", 14),
            bg="#3B4252",
            fg="#ECEFF4",
            activebackground="#5E81AC",
            activeforeground="#ECEFF4",
            command=self.show_dashboard,
            relief="flat",
            padx=10,
            pady=10,
        )
        dashboard_btn.pack(fill="x", pady=5)

        settings_btn = tk.Button(
            self.nav_panel,
            text="Настройки",
            font=("Arial", 14),
            bg="#3B4252",
            fg="#ECEFF4",
            activebackground="#5E81AC",
            activeforeground="#ECEFF4",
            command=self.show_settings,
            relief="flat",
            padx=10,
            pady=10,
        )
        settings_btn.pack(fill="x", pady=5)

        about_btn = tk.Button(
            self.nav_panel,
            text="Информация",
            font=("Arial", 14),
            bg="#3B4252",
            fg="#ECEFF4",
            activebackground="#5E81AC",
            activeforeground="#ECEFF4",
            command=self.show_about,
            relief="flat",
            padx=10,
            pady=10,
        )
        about_btn.pack(fill="x", pady=5)

    def show_dashboard(self):
        """Показва таблото."""
        self.clear_content()
        self.current_screen = "dashboard"

        title = tk.Label(
            self.content_panel,
            text="Табло",
            font=("Arial", 20, "bold"),
            bg="#ECEFF4",
            fg="#2E3440",
            pady=20,
        )
        title.pack()

        start_btn = tk.Button(
            self.content_panel,
            text="Стартирай Програмата",
            font=("Arial", 16),
            bg="#A3BE8C",
            fg="#ECEFF4",
            activebackground="#8FBCBB",
            activeforeground="#ECEFF4",
            command=lambda: messagebox.showinfo("Старт", "Програмата е стартирана!"),
            relief="flat",
            padx=10,
            pady=10,
        )
        start_btn.pack(pady=20)

        stop_btn = tk.Button(
            self.content_panel,
            text="Спри Програмата",
            font=("Arial", 16),
            bg="#BF616A",
            fg="#ECEFF4",
            activebackground="#D08770",
            activeforeground="#ECEFF4",
            command=lambda: messagebox.showinfo("Стоп", "Програмата е спряна!"),
            relief="flat",
            padx=10,
            pady=10,
        )
        stop_btn.pack(pady=20)

    def show_settings(self):
        """Показва настройките."""
        self.clear_content()
        self.current_screen = "settings"

        title = tk.Label(
            self.content_panel,
            text="Настройки",
            font=("Arial", 20, "bold"),
            bg="#ECEFF4",
            fg="#2E3440",
            pady=20,
        )
        title.pack()

        resolution_label = tk.Label(
            self.content_panel,
            text="Резолюция на екрана:",
            font=("Arial", 14),
            bg="#ECEFF4",
            fg="#2E3440",
        )
        resolution_label.pack(anchor="w", padx=20, pady=10)

        resolution_combo = ttk.Combobox(
            self.content_panel, values=["800x480", "1024x600", "1920x1080"], state="readonly", font=("Arial", 12)
        )
        resolution_combo.set("800x480")
        resolution_combo.pack(anchor="w", padx=20, pady=10)

        apply_btn = tk.Button(
            self.content_panel,
            text="Приложи",
            font=("Arial", 14),
            bg="#5E81AC",
            fg="#ECEFF4",
            activebackground="#81A1C1",
            activeforeground="#ECEFF4",
            command=lambda: messagebox.showinfo("Настройки", f"Избрана резолюция: {resolution_combo.get()}"),
            relief="flat",
            padx=10,
            pady=10,
        )
        apply_btn.pack(pady=20)

    def show_about(self):
        """Показва информация за програмата."""
        self.clear_content()
        self.current_screen = "about"

        title = tk.Label(
            self.content_panel,
            text="Информация",
            font=("Arial", 20, "bold"),
            bg="#ECEFF4",
            fg="#2E3440",
            pady=20,
        )
        title.pack()

        info_text = tk.Text(
            self.content_panel,
            height=10,
            width=50,
            wrap="word",
            bg="#ECEFF4",
            fg="#2E3440",
            font=("Arial", 14),
            bd=0,
        )
        info_text.insert("1.0", "Това е минималистичен интерфейс за Raspberry Pi проекти.")
        info_text.config(state="disabled")
        info_text.pack(pady=10)

    def clear_content(self):
        """Изчиства съдържанието на десния панел."""
        for widget in self.content_panel.winfo_children():
            widget.destroy()


# Стартиране на приложението
if __name__ == "__main__":
    app = MinimalApp()
    app.mainloop()

