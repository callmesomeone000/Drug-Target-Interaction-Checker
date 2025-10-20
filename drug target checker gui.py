import tkinter as tk
from tkinter import messagebox
import csv

# ----------------- Load Data -----------------
def load_data(file_path):
    """Load drug-target interactions from CSV into a dictionary."""
    interactions = {}
    try:
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                drug = row['Drug'].strip().lower()
                protein = row['Protein'].strip()
                if drug in interactions:
                    interactions[drug].append(protein)
                else:
                    interactions[drug] = [protein]
    except FileNotFoundError:
        messagebox.showerror("Error", f"CSV file not found: {file_path}")
    return interactions

# ----------------- Check Function -----------------
def check_interaction():
    drug_name = drug_entry.get().strip().lower()
    if not drug_name:
        messagebox.showwarning("Warning", "Please enter a drug name!")
        return

    proteins = interactions.get(drug_name)
    if proteins:
        result_label.config(text=f"Proteins interacting with '{drug_name.title()}':\n- " + "\n- ".join(proteins))
    else:
        result_label.config(text=f"No interactions found for '{drug_name.title()}'.")

# ----------------- Main GUI -----------------
# Load CSV (example CSV path)
interactions = load_data("drug_target.csv")

root = tk.Tk()
root.title("💊 Drug-Target Interaction Checker")
root.geometry("500x300")
root.resizable(False, False)

# Heading
tk.Label(root, text="Drug-Target Interaction Checker", font=("Arial", 16, "bold")).pack(pady=10)

# Entry
tk.Label(root, text="Enter Drug Name:", font=("Arial", 12)).pack(pady=5)
drug_entry = tk.Entry(root, font=("Arial", 12))
drug_entry.pack(pady=5)

# Search Button
tk.Button(root, text="Check Target Proteins", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=check_interaction).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=450, justify="left")
result_label.pack(pady=10)

root.mainloop()
