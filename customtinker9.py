"""
PURPOSE: Create a secure Biomedical Data Entry application with input validation.
THEORY: Clinical UIs require strict data validation before processing to avoid DB corruption.
HINT: Use CTkScrollableFrame for forms that might exceed the display height of smaller monitors.
"""
import customtkinter as ctk # Import the modern toolkit

class Lab9(ctk.CTk):
    def __init__(self):
        super().__init__() # Initialize the main window
        
        # --- WINDOW CONFIGURATION ---
        self.geometry("600x700") # Set explicit window geometry
        self.title("Lab 9: Clinical Trial Data Entry") # Set professional title
        ctk.set_appearance_mode("light") # Medical software often uses light themes
        
        # --- THEORY & HINT PANEL ---
        self.info_frame = ctk.CTkFrame(self, fg_color="#e0e0e0") # Create info container
        self.info_frame.pack(fill="x", padx=20, pady=10) # Position at top
        self.theory_lbl = ctk.CTkLabel(self.info_frame, text="THEORY: Validate numeric inputs using try/except blocks.", text_color="blue")
        self.theory_lbl.pack() # Display theory
        self.hint_lbl = ctk.CTkLabel(self.info_frame, text="HINT: CTkScrollableFrame handles tall content effortlessly.", text_color="gray")
        self.hint_lbl.pack() # Display hint

        # --- SCROLLABLE FORM CONTAINER ---
        self.form_frame = ctk.CTkScrollableFrame(self, width=500, height=450)
        self.form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # 1. Patient ID
        ctk.CTkLabel(self.form_frame, text="Patient Subject ID:").pack(anchor="w", padx=10, pady=(10,0))
        self.id_entry = ctk.CTkEntry(self.form_frame, placeholder_text="e.g. SUB-1042")
        self.id_entry.pack(fill="x", padx=10, pady=5)

        # 2. Blood Type (Segmented Button)
        ctk.CTkLabel(self.form_frame, text="Blood Group:").pack(anchor="w", padx=10, pady=(10,0))
        self.blood_seg = ctk.CTkSegmentedButton(self.form_frame, values=["A", "B", "AB", "O"])
        self.blood_seg.pack(fill="x", padx=10, pady=5)
        self.blood_seg.set("A") # Set default value

        # 3. Vitals: Heart Rate
        ctk.CTkLabel(self.form_frame, text="Resting Heart Rate (BPM):").pack(anchor="w", padx=10, pady=(10,0))
        self.hr_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Normal range 60-100")
        self.hr_entry.pack(fill="x", padx=10, pady=5)

        # 4. Status Dropdown
        ctk.CTkLabel(self.form_frame, text="Trial Status:").pack(anchor="w", padx=10, pady=(10,0))
        self.status_menu = ctk.CTkOptionMenu(self.form_frame, values=["Screening", "Enrolled", "Completed", "Withdrawn"])
        self.status_menu.pack(fill="x", padx=10, pady=5)

        # --- OUTPUT/VALIDATION SECTION ---
        self.submit_btn = ctk.CTkButton(self, text="VALIDATE & SAVE", command=self.validate_data, fg_color="green")
        self.submit_btn.pack(pady=10) # Create and pack action button
        
        self.log_box = ctk.CTkTextbox(self, height=100, state="disabled")
        self.log_box.pack(fill="x", padx=20, pady=(0,20)) # Textbox for system logs

    def validate_data(self):
        # Gather inputs
        p_id = self.id_entry.get()
        hr_str = self.hr_entry.get()
        blood = self.blood_seg.get()
        
        self.log_box.configure(state="normal") # Enable textbox to write
        self.log_box.delete("1.0", "end") # Clear previous logs
        
        if not p_id or not hr_str: # Check for blank fields
            self.log_box.insert("end", "[ERROR] Fields cannot be empty.\n")
        else:
            try:
                hr_val = int(hr_str) # Attempt to parse integer
                if 40 <= hr_val <= 200: # Medical constraint check
                    success_msg = f"[SUCCESS] Saved Patient {p_id} | Type: {blood} | HR: {hr_val}\n"
                    self.log_box.insert("end", success_msg)
                    self.id_entry.delete(0, 'end') # Clear form on success
                    self.hr_entry.delete(0, 'end')
                else:
                    self.log_box.insert("end", f"[WARNING] HR {hr_val} BPM is outside biological limits!\n")
            except ValueError:
                self.log_box.insert("end", "[ERROR] Heart rate must be a valid integer.\n")
                
        self.log_box.configure(state="disabled") # Disable textbox to prevent user edits

if __name__ == "__main__":
    app = Lab9() # Create instance
    app.mainloop() # Run the application