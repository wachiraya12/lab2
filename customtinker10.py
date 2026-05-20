import customtkinter as ctk
class Lab10(ctk.CTk):
    def __init__(self):
        super() .__init__()
        self.geometry("600x500")
        self.title("Lab 10: Multi-Axis Robotics Controller")
        ctk.set_appearance_mode("dark")
        self.info_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.info_frame.pack(fill="x", padx=20, pady=10)
        self.theory_lbl = ctk.CTkLabel(self. info_frame, text="THEORY: Tab views isolate operational domains (e.g., X vs Y axis).", text_color="cyan")
        self.theory_lbl.pack()
        self.hint_lbl = ctk.CTkLabel(self.info_frame, text="HINT: Bind slider commands to dynamically update telemetry displays.", text_color="gray")
        self.hint_lbl.pack()
        self.tab_view = ctk.CTkTabview(self) 
        self.tab_view.pack(padx=20, pady=10, fill="both", expand=True)
        self.tab_x = self.tab_view.add("X-Axis Motor")
        self.tab_y = self.tab_view.add("Y-Axis Motor")
        self.tab_view.set("X-Axis Motor")
        self.setup_motor_tab(self.tab_x, "X")
        self.setup_motor_tab(self.tab_y, "Y")
        self.e_stop_btn = ctk.CTkButton(self, text="EMERGENCY STOP (E-STOP)", command=self.e_stop,
                                        fg_color="#cc0000", hover_color="#ff0000", font=("Roboto", 16, "bold"))
        self.e_stop_btn.pack(pady=20, fill="x", padx=20)
    def setup_motor_tab(self, tab_parent, axis_name):
        switch = ctk.CTkSwitch(tab_parent, text=f"Enable {axis_name} Driver", text_color="green")
        switch.pack (pady=15)
        val_lbl = ctk.CTkLabel(tab_parent, text="Velocity: 0 RPM", font=("Consolas", 20))
        val_lbl.pack(pady=10)
        def slider_event(value, lbl=val_lbl):
            lbl.configure(text=f"Velocity:{int(value)} RPM")
            slider = ctk.CTkSlider(tab_parent, from_= 0, to=3000, command=slider_event)
            slider.set(0)
            slider.pack(pady=10, padx=40, fill="x")
            dir_seg = ctk.CTkSegmentedButton(tab_parent, values=["Forward (CW)", "Reverse (CCW)"])
            dir_seg.set("Forward (CW)")
            dir_seg.pack(pady=15)
    def e_stop(self):
        """Emergency stop sequence: locks the interface"""
        self.tab_view.configure(state="disabled")
        self.e_stop_btn.configure(text="SYSTEM LOCKED - RESET REQUIRED", state="disabled")
if __name__ == "__main__":
    app = Lab10() 
    app.mainloop()  
        
    
