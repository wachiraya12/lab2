import customtkinter as ctk
def apply_pro_style(window, title):
    """
    Configures the window to be 75% of the screen size and centers it.
    Applies the modern dark theme and standard tech-blue accent.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    width = int(screen_w * 0.75)
    height = int(screen_h * 0.75)
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.title(f"STEM AI | {title}")
class LabBase(ctk.CTk):
    """A base class to ensure Theory and Hints are always displayed on screen. """
    def __init__(self, title, theory, hint):
        super().__init__()
        apply_pro_style(self, title)
        self.header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        self.header.pack(fill="x", padx=30, pady=(20, 10))
        ctk.CTkLabel(self.header, text="THEORY", font=("Orbitron", 14, "bold"), text_color="#3b8ede").pack(anchor="w", padx=20, pady=(10, 0))
        self.theory_box = ctk.CTkLabel(self.header, text=theory, wraplength=1000, justify="left", font=("Inter", 13))
        self.theory_box.pack(anchor="w", padx=20, pady=(5, 10))
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.pack(side="bottom", fill="x", padx=30, pady=20)
        self.hint_lbl = ctk.CTkLabel(self.footer, text=f"HINT: {hint}", font=("Inter", 12, "italic"), text_color="#aaaaaa")
        self.hint_lbl.pack(side="left")