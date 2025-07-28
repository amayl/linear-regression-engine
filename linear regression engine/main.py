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
        
        # Create dynamic table
        self.table = DynamicTable(
            self,
            headers=["X Values", "Y Values"],
            initial_rows=5
        )
        self.table.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")



if __name__ == "__main__":
    # Set appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()