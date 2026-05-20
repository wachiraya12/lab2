import customtkinter as ctk
from app_config1 import LabBase
class Lab13(LabBase):
    def __init__(self):
        theory = "In robotics, sliders represent PWM signals or Servo angles. The UI must 'Process' this float data into human-readable units."
        hint = "A progress bar can be repurposed as a high-visibility gauge by changing its 'progress_color' dynamically."
        super() .__init__("Edge AI Sensor Dashboard", theory, hint)
        self.slider = ctk.CTkSlider(self, from_= 0, to=150, width=500, height=25, command=self.update_telemetry)
        self.slider.pack (pady=60)
        self.slider.set (20)
        self.gauge = ctk.CTkProgressBar(self, width=600, height=40, corner_radius=5)
        self.gauge.pack(pady=10)
        self.metric = ctk.CTkLabel(self, text="20C", font=("Roboto", 80, "bold"))
        self.metric.pack()
    def update_telemetry(self, value):
        normalized = value / 150
        self.gauge.set (normalized)
        color = "#2FA572" if value < 60 else "#E67E22" if value < 100 else "#FF3333"
        self.gauge.configure(progress_color=color)
        self.metric.configure(text=f"{int(value)}℃", text_color=color)
if __name__ == "__main__":
    app = Lab13() 
    app.mainloop() 
        