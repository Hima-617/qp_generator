# 📝 Question Paper Generator (Streamlit)

A Streamlit-based Question Paper Generator that creates **question papers and answer keys** for:

- **Grades 1–12** (sample questions)
- **B.Tech** subjects (Python Programming, Data Structures, DBMS)

This tool lets you choose the exact number of MCQs, Short Answers, and Long Answers.  
It shows live previews and allows downloading the outputs in **TXT** or **PDF** format (PDF generated without reportlab).

---

## 📁 Project Structure

qp_generator/
│── app.py # Main Streamlit application
│── ui.py # UI components and sidebar controls
│── generator.py # Logic for selecting and creating QP & Answer Key
│── question_bank.py # Complete question bank for Grades 1–12 and B.Tech
│── utils.py # Text formatting + custom minimal PDF generator
│── requirements.txt # Streamlit dependency
│── README.md # Documentation

---

## ▶️ Run the App
streamlit run app.py

---

## 📸 Screenshots

<img width="1366" height="768" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/d323528d-76ea-4603-bb17-c248a754338e" />

---

## 📦 Requirements

- Python 3.x  
- Streamlit (auto-installed via requirements.txt)

---

## 📝 License

This project is licensed under the **MIT License**.

---

## ❤️ Contributing

Pull requests are welcome!  
If you'd like a feature added, open an issue — suggestions are appreciated.

---
