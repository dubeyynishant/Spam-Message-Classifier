# 🚫 Spam Message Classifier


## 📌 Project Overview

The **Spam Message Classifier** is a Machine Learning–based web application that classifies messages as **Spam** or **Ham (Not Spam)**.
This project uses **Python**, **Scikit-learn**, and **Streamlit** to deploy a trained ML model with an interactive and user-friendly interface.

It supports both **single message prediction** and **bulk message prediction**, making it suitable for real-world use cases and academic projects.

---

## 📸 Application Preview

![Spam Classifier App](https://github.com/dubeyynishant/Spam-Message-Classifier/tree/main/Spam%20Detection.png)

---

## ✨ Features

* ✅ Predict spam or ham for a single message
* ✅ Bulk message prediction using CSV or TXT files
* ✅ Simple and clean Streamlit UI
* ✅ Fast predictions using a trained ML model
* ✅ Beginner-friendly and interview-ready project

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas**
* **Joblib**

---

## 📁 Project Structure

```
Spam-Message-Classifier/
│
├── Spam_project.py        # Single message prediction
├── Spam_project2.py       # Full app (Single + Bulk prediction)
├── spam_clf.pkl           # Trained ML model
├── test_data_spam.txt     # Sample data for bulk testing
├── flag.jpg               # Image used in sidebar
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 How to Run the Project Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Application

```bash
streamlit run Spam_project2.py
```

---

## 🌐 Live Deployment (Streamlit Cloud)

You can deploy this project easily using **Streamlit Cloud**.

**Steps:**

1. Push the code to GitHub
2. Go to 👉 [https://share.streamlit.io](https://share.streamlit.io)
3. Select repository: `dubeyynishant/Spam-Message-Classifier`
4. Main file: `Spam_project2.py`
5. Click **Deploy**

---

## 🧪 Sample Test Data

The repository includes a sample file: **`test_data_spam.txt`**

Example messages:

```
you won a free trip of world tour
give your account details to get the offer
hello sir how are you?
congratulation you got selected in final round of job process
```

---

## 🧠 How the Project Works

1. A Machine Learning model is trained on labeled spam and ham messages.
2. The trained model is saved using **Joblib**.
3. Streamlit loads the model.
4. User enters a message or uploads a file.
5. The model predicts whether the message is **Spam** or **Ham**.

---

## 🎯 Use Cases

* SMS spam detection
* Learning ML model deployment
* College mini/major project
* Streamlit + ML practice

---

## 🔮 Future Enhancements

* Add prediction accuracy display
* Support Excel file uploads
* Improve UI styling
* Retrain model with larger dataset

---

## 👨‍💻 Author

**Nishant Dubey**
GitHub: [https://github.com/dubeyynishant](https://github.com/dubeyynishant)

---

## ⭐ Support

If you like this project, please ⭐ star the repository and share your feedback!

