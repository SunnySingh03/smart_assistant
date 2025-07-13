from transformers import pipeline
import torch
import re
import textwrap

# Detect device
device = 0 if torch.cuda.is_available() else -1
print("✅ Using", "GPU" if device == 0 else "CPU")

# Load models
summarizer = pipeline("summarization", model="Falconsai/text_summarization", device=device)
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2", device=device)

# Summarize
def summarize(text, max_chunk=500):
    chunks = textwrap.wrap(text, max_chunk)
    summary = ""
    for chunk in chunks:
        try:
            result = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
            summary += result[0]['summary_text'] + "\n"
        except Exception as e:
            print("Summarization error:", e)
    return summary.strip()

# Answer Question from best paragraph
def answer_question(context, question):
    try:
        paragraphs = re.split(r'\n\s*\n', context)
        best_answer = ""
        best_score = 0

        for para in paragraphs:
            if len(para.strip()) < 50:
                continue
            result = qa_model(question=question, context=para)
            answer = result.get("answer", "").strip()
            score = result.get("score", 0)

            if score > best_score and answer.lower() not in ["", ".", "unknown"]:
                best_answer = answer
                best_score = score

        if best_score > 0.4:
            return best_answer
        else:
            return "❌ No relevant answer found in the document."
    except Exception as e:
        print("QA error:", e)
        return "⚠️ Could not process the question properly."
