# 🚗 Parking Management System – Entry Ticket

This is a simple **Parking Entry Ticket Generator** built with **Flask (Python)** and **HTML/CSS**.  
It generates a **unique entry code** for vehicles entering the parking lot. The ticket can be **printed** directly from the browser and will be required at the time of exit.

---

## 📸 Preview
<img width="1898" height="872" alt="Screenshot 2025-08-22 063334" src="https://github.com/user-attachments/assets/4c02b720-8e00-41c1-8b8d-b33b2fd45e74" />


---

## ✨ Features
-  Generate a **unique entry code** for each vehicle  
-  Print only the **ticket section** (no buttons/UI clutter)  
-  Ticket appears at the **top-center** of the print page  
-  Clean, responsive design with modern UI  
-  Back-to-home button for quick navigation  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS  
- **Database (optional):** MySQL / SQLite (if integrated for storing entries)  

---

## 📂 Project Structure
```
parking-management/
│── static/ # CSS, JS, Images (if any)
│── templates/ # HTML templates
│ └── entry_confirmed.html
│── app.py # Flask backend
└── requirements.txt # Dependencies
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/parking-management.git
cd parking-management
```
### 2️⃣ Create a Virtual Environment (Optional but recommended)
```
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Linux/Mac

```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```
python app.py
```
#### Now open your browser and visit 👉
```
http://127.0.0.1:5000/
```

---

## 🖨️ Printing the Ticket

Click the Print button

Only the ticket box will be printed (centered at the top of the page, 150px width)

---

## 📌 Future Improvements
 - Store ticket data in a database (MySQL/SQLite)

 - Implement Exit system with code verification

 - Add Admin dashboard for managing parking slots


---


## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo, open an issue, or submit a pull request.


---


## 👨‍💻 Author
### Arpan Dey
- adey011003@gmail.com
- https://monumental-melba-466609.netlify.app/
