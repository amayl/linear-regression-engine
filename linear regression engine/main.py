import customtkinter as ctk
from dynamic_table import DynamicTable

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Linear Regression Engine")
        self.geometry("800x600")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Title
        title_label = ctk.CTkLabel(
            self,
            text="Linear Regression Engine",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            width=750,  # Set desired width
            height=500  # Set desired height
        )
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        # Configure scrollable frame grid
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Create dynamic table inside scrollable frame
        self.table = DynamicTable(
            self.scrollable_frame,  # Parent is now the scrollable frame
            headers=["X Values", "Y Values"],
            initial_rows=5
        )
        self.table.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

if __name__ == "__main__":
    # Set appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()