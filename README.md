# 🤖 Smart Research Assistant (Offline + GPU Support)

An intelligent, GPU-accelerated research assistant that summarizes academic documents and answers questions from them — all offline! Built with 💡 PyTorch, 🤗 Transformers, and 🧠 NLP.

---

## 🚀 Features

- 🔍 **Automatic Text Summarization**
- 🤔 **Contextual Question Answering (QA)**
- ⚡ **GPU Acceleration Support**
- 📄 PDF File Upload and Extraction
- 🧠 Local LLM Inference (No API Required)
- ✅ Streamlit UI for ease of use

---

## 🎯 Use Case

This project is ideal for:
- Students reading research papers
- Researchers exploring large PDFs
- Offline environments with no internet access
- Developers experimenting with summarization & QA pipelines

---

## 🛠️ Tech Stack

| Layer        | Technology                         |
|--------------|------------------------------------|
| Frontend     | `Streamlit`                        |
| Backend      | `Transformers`, `PyTorch`          |
| PDF Parsing  | `PyMuPDF (fitz)`                   |
| Summarization| `Falconsai/text_summarization`     |
| QA Model     | `deepset/roberta-base-squad2`      |

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/smart_assistant.git
cd smart_assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
