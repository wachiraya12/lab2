import customtkinter as ctk
from app_config1 import LabBase
class Lab12(LabBase):
    def __init__(self):
        theory = "Validation logic acts as a filter between raw user input and system security. Real-time feedback reduces user error rates."
        hint = "Binding '<KeyRelease>' ensures the 'Process' function runs immediately after the finger leaves the key."
        super() .__init__("Biometric Security Gateway", theory, hint)
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter Authorization Token ... ", width=450, height=60, font=("Roboto", 18), corner_radius=10)
        self.entry.pack(pady=50)
        self.entry.bind("<KeyRelease>", self.real_time_process)
        self.display = ctk.CTkLabel(self, text="WAITING FOR TOKEN", font=("Orbitron", 32, "bold"), text_color="#444444")
        self.display.pack (pady=20)
    def real_time_process (self, event):
        token = self. entry.get()
        if len(token) == 0:
            self.display.configure(text="WAITING FOR TOKEN", text_color="#444444")
        elif "admin" in token. lower() and len(token) > 8:
            self.display.configure(text="ACCESS GRANTED", text_color="#2FA572")
        else:
            self.display.configure(text="INVALID CREDENTIALS", text_color="#FF3333")
if __name__ == "__main__":
    app = Lab12() 
    app.mainloop() 