"""
PURPOSE: Build a real-time 'System Boot' sequence using asynchronous recursion.
THEORY: GUI mainloops are single-threaded. To show progress without freezing, we use .after().
HINT: Values in progress bars must be normalized between 0.0 and 1.0.
"""
import customtkinter as ctk
from app_config1 import LabBase # Import the pro configuration

class Lab01(LabBase):
    def __init__(self):
        # Theory and Hint content displayed on screen
        theory = "To prevent 'Not Responding' errors during heavy AI processing, we use the .after() method to schedule updates without locking the UI thread."
        hint = "Use 'determinate' mode for known durations and 'indeterminate' for unknown loading times."
        super().__init__("Neural Link Loader", theory, hint)

        # 1. INPUT: Trigger Button
        self.btn = ctk.CTkButton(self, text="INITIALIZE CORE", font=("Roboto", 16), height=50, command=self.process_start)
        self.btn.pack(pady=40)

        # 2. PROCESS: Real-time Colorful Progress Bar
        self.progress = ctk.CTkProgressBar(self, width=600, height=15, progress_color="#A32CC4", fg_color="#333333")
        self.progress.set(0) # Start at zero
        self.progress.pack(pady=20)

        # 3. OUTPUT: Status Display
        self.status = ctk.CTkLabel(self, text="SYSTEM READY", font=("Consolas", 24, "bold"), text_color="#555555")
        self.status.pack(pady=20)

    def process_start(self):
        self.btn.configure(state="disabled") # Disable input to prevent spamming
        self.run_cycle(0) # Start the iterative process

    def run_cycle(self, val):
        if val <= 1.0: # Process Logic: Check if complete
            self.progress.set(val) # Update the colorful bar
            self.status.configure(text=f"LOADING NEURAL WEIGHTS: {int(val*100)}%", text_color="#A32CC4") # Real-time text
            self.after(20, lambda: self.run_cycle(val + 0.01)) # Recurse after 20ms
        else:
            self.status.configure(text="SYSTEM ONLINE", text_color="#2FA572") # Final output success
            self.btn.configure(state="normal") # Re-enable input

if __name__ == "__main__":
    app = Lab01()
    app.mainloop()