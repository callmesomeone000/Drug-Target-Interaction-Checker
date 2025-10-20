# 💊 Drug-Target Interaction Checker

**Description:**  
Drug-Target Interaction Checker is a Python tool that lets users explore which proteins interact with specific drugs. Enter a drug name, and it instantly shows all known protein targets from a CSV database. Interactive, simple, and perfect for learning drug-protein relationships.

---

## ✨ Features
- 🔍 Search for drug-protein interactions
- 🗂️ Uses a CSV database for drug-target mapping
- 🖥️ Interactive GUI with Tkinter
- ⚡ Fast and easy to use
- 📚 Great for students and beginners in bioinformatics

---

## 🛠️ Requirements
- Python 3.x
- Tkinter (usually comes with Python)
- CSV file with `Drug,Protein` columns

<img width="622" height="400" alt="image" src="https://github.com/user-attachments/assets/69c782b7-d45f-4cd8-8e36-04dae9dedd1f" />

<img width="403" height="844" alt="image" src="https://github.com/user-attachments/assets/bed95387-9649-4ebf-8c4b-dea513d5c7b1" />


---

## 📝 Usage
1. Save your drug-target CSV (example `drug_target.csv`) in the same folder as the script.
2. Run the script:
```
python drug_target_checker.py
```
3. Enter the drug name in the input box and click Check Target Proteins.
4. View interacting proteins instantly.

👨‍💻 How It Works
- Loads drug-target data from a CSV into a Python dictionary
- User inputs a drug name
- Script looks up proteins interacting with the drug
- Displays results neatly in the GUI

⚡ Future Improvements
- Auto-complete suggestions for drug names
- Add web-based version using Streamlit
- Expand database with more drugs and proteins
