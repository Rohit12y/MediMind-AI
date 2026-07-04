#🩺 MediMind-AI

An AI-powered medical chatbot that answers healthcare-related questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG). The application provides intelligent responses based on medical documents through a simple and interactive web interface.

---

## ✨ Features

- 💬 AI-powered medical chatbot
- 📄 PDF-based knowledge retrieval
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using vector embeddings
- ⚡ Fast and accurate responses
- 🌐 Simple Flask web interface

---

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Pinecone
- Google Gemini API
- Hugging Face Embeddings
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
MediMind-AI/
│
├── Data/                 # Medical PDF files
├── static/               # CSS, JavaScript, Images
├── templates/            # HTML templates
├── app.py                # Flask application
├── store_index.py        # Creates vector database
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rohit12y/MediMind-AI.git

cd MediMind-AI
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv medibot
medibot\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv medibot
source medibot/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 5. Create the vector database

```bash
python store_index.py
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Demo

Add screenshots or a GIF here.

```
assets/demo.gif
```

---

## 📌 Future Improvements

- Voice input
- Medical image analysis
- Chat history
- User authentication
- Multi-language support
- Doctor appointment integration

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes only.

It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rohit Yadav**

GitHub: https://github.com/Rohit12y
Email: yadavrohit7212@gmail.com

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
