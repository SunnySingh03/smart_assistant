import streamlit as st
import fitz  # PyMuPDF
from qa_engine import summarize, answer_question

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@st.cache_data
def get_summary(text):
    return summarize(text[:3000])  # summarize only part for speed

# Streamlit UI
st.title("📚 Smart Research Assistant (Offline + GPU)")

uploaded_file = st.file_uploader("📄 Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    raw_text = extract_text_from_pdf(uploaded_file)
    st.write("📏 Document Length:", len(raw_text))

    with st.spinner("⏳ Generating summary..."):
        summary = get_summary(raw_text)
    st.success("✅ Summary Ready!")

    st.subheader("📝 Summary")
    st.write(summary)

    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question about the document")

    if question:
        with st.spinner("🤖 Finding answer..."):
            answer = answer_question(raw_text[:5000], question)
        st.write("🧠 **Answer:**", answer)
