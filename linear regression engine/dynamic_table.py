from tkinter import END
import customtkinter as ctk
from typing import List, Any


class DynamicTable(ctk.CTkFrame):
    def __init__(self, parent, headers: List[str], initial_rows: int = 5, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.headers = headers
        self.num_cols = len(headers)
        self.entries: List[List[ctk.CTkEntry]] = []
        
        # Configure grid
        for i in range(self.num_cols + 1):  # +1 for row numbers
            self.grid_columnconfigure(i, weight=1)
        
        self.setup_headers()
        self.add_rows(initial_rows)
        self.setup_controls()
    
    def setup_headers(self):
        """Create header row"""
        # Empty cell for row numbers column
        header_frame = ctk.CTkFrame(self)
        header_frame.grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        
        row_label = ctk.CTkLabel(header_frame, text="#", font=ctk.CTkFont(weight="bold"))
        row_label.pack(pady=5)
        
        # Column headers
        for j, header in enumerate(self.headers):
            header_frame = ctk.CTkFrame(self)
            header_frame.grid(row=0, column=j+1, padx=2, pady=2, sticky="ew")
            
            header_label = ctk.CTkLabel(
                header_frame, 
                text=header, 
                font=ctk.CTkFont(weight="bold")
            )
            header_label.pack(pady=5)
    
    def add_rows(self, count: int):
        """Add specified number of rows to the table"""
        start_row = len(self.entries) + 1  # +1 for header
        
        for i in range(count):
            row_index = start_row + i
            row_entries = []
            
            # Row number label
            row_num_frame = ctk.CTkFrame(self)
            row_num_frame.grid(row=row_index, column=0, padx=2, pady=2, sticky="ew")
            
            row_num_label = ctk.CTkLabel(
                row_num_frame, 
                text=str(len(self.entries) + i + 1),
                font=ctk.CTkFont(weight="bold")
            )
            row_num_label.pack(pady=5)
            
            # Data entry cells
            for j in range(self.num_cols):
                entry = ctk.CTkEntry(
                    self,
                    width=100,
                    placeholder_text=f"Enter {self.headers[j].lower()}"
                )
                entry.grid(row=row_index, column=j+1, padx=2, pady=2, sticky="ew")
                row_entries.append(entry)
            
            self.entries.append(row_entries)
        
        self.update_row_numbers()
    
    def remove_last_row(self):
        """Remove the last row from the table"""
        if len(self.entries) > 1:  # Keep at least one row
            # Remove entries from last row
            for entry in self.entries[-1]:
                entry.destroy()
            
            # Remove row number label
            last_row_index = len(self.entries)  # +1 for header, -1 for 0-indexing = 0
            for widget in self.grid_slaves(row=last_row_index):
                if widget.grid_info()['column'] == 0:
                    widget.destroy()
            
            self.entries.pop()
            self.update_row_numbers()
    
    def update_row_numbers(self):
        """Update row number labels"""
        for i, widget in enumerate(self.grid_slaves()):
            info = widget.grid_info()
            if info and info['column'] == 0 and info['row'] > 0:  # Skip header
                # Find the label inside the frame and update it
                for child in widget.winfo_children():
                    if isinstance(child, ctk.CTkLabel):
                        child.configure(text=str(info['row']))
                        break
    
    def setup_controls(self):
        """Create control buttons for adding/removing rows"""
        controls_frame = ctk.CTkFrame(self)
        controls_frame.grid(
            row=len(self.entries) + 1, 
            column=0, 
            columnspan=self.num_cols + 1, 
            padx=2, 
            pady=10, 
            sticky="ew"
        )
        
        add_btn = ctk.CTkButton(
            controls_frame,
            text="Add Row",
            command=lambda: self.add_row_and_update_controls(),
            width=100
        )
        add_btn.pack(side="left", padx=5, pady=5)
        
        remove_btn = ctk.CTkButton(
            controls_frame,
            text="Remove Row",
            command=lambda: self.remove_row_and_update_controls(),
            width=100
        )
        remove_btn.pack(side="left", padx=5, pady=5)
        
        clear_btn = ctk.CTkButton(
            controls_frame,
            text="Clear All",
            command=self.clear_all_data,
            width=100
        )
        clear_btn.pack(side="left", padx=5, pady=5)
        
        get_data_btn = ctk.CTkButton(
            controls_frame,
            text="Get Data",
            command=self.get_data,
            width=100
        )
        get_data_btn.pack(side="right", padx=5, pady=5)
    
    def add_row_and_update_controls(self):
        """Add a row and update control positions"""
        # Remove current controls
        for widget in self.grid_slaves():
            if widget.grid_info() and widget.grid_info()['row'] == len(self.entries) + 1:
                widget.destroy()
        
        self.add_rows(1)
        self.setup_controls()
    
    def remove_row_and_update_controls(self):
        """Remove a row and update control positions"""
        if len(self.entries) > 1:
            # Remove current controls
            for widget in self.grid_slaves():
                if widget.grid_info() and widget.grid_info()['row'] == len(self.entries) + 1:
                    widget.destroy()
            
            self.remove_last_row()
            self.setup_controls()
    
    def clear_all_data(self):
        """Clear all data from entries"""
        for row in self.entries:
            for entry in row:
                entry.delete(0, END)
    
    def get_data(self):
        """Get X and Y values as separate arrays"""
        x_values = []
        y_values = []
        
        for row in self.entries:
            # Get X value (first column)
            x_val: int = int(row[0].get().strip())
            # Get Y value (second column) 
            y_val: int = int(row[1].get().strip())
            
            # Only add if both have values
            if x_val and y_val:
                x_values.append(x_val)
                y_values.append(y_val)
    
        print(f"X values: {x_values}")
        print(f"Y values: {y_values}")
    
    
    def set_data(self, data: List[List[str]]):
        """Set data in the table"""
        # Clear existing data
        self.clear_all_data()
        
        # Add more rows if needed
        needed_rows = len(data)
        current_rows = len(self.entries)
        
        if needed_rows > current_rows:
            self.add_rows(needed_rows - current_rows)
        
        # Fill data
        for i, row_data in enumerate(data):
            if i < len(self.entries):
                for j, value in enumerate(row_data):
                    if j < len(self.entries[i]):
                        self.entries[i][j].delete(0, END)
                        self.entries[i][j].insert(0, int(value))