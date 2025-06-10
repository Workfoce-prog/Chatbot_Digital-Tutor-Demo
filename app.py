import streamlit as st
import random
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.set_page_config(page_title="Digital Tutor Demo", page_icon="🎓")

st.title("🎓 Digital Tutor (Demo - No API Key Required)")

subjects = [
    "Algebra", "Geometry", "Trigonometry", "Polynomials", "Radicals",
    "Quadratic Functions", "Exponential & Logarithmic Functions",
    "Parabolas", "Statistics", "Data Science"
]

# Placeholder chatbot logic
def demo_tutor_response(question, subject):
    demo_responses = [
        f"In {subject}, a common concept is solving equations. Here's an example: 2x + 3 = 7 → x = 2.",
        f"{subject} often involves step-by-step reasoning. Let's break this down...",
        f"To answer your question about {subject}, think about the key principles: balance, structure, and formulas."
    ]
    return random.choice(demo_responses)

def generate_pdf(questions, answers):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, 740, "Grade 6–12 Worksheet (Demo)")
    c.setFont("Helvetica", 12)
    y = 700
    for q, a in zip(questions, answers):
        c.drawString(72, y, q)
        y -= 20
        c.drawString(92, y, f"Answer: {a}")
        y -= 30
    c.save()
    buffer.seek(0)
    return buffer

tab1, tab2 = st.tabs(["🎓 Tutor", "📝 Worksheet Generator"])

with tab1:
    st.header("Ask the Digital Tutor")
    student_name = st.text_input("Student Name (for demo purposes)")
    subject = st.selectbox("Select a Subject", subjects)
    question = st.text_input("Enter a question:")
    if student_name and question:
        response = demo_tutor_response(question, subject)
        st.markdown("### 📘 Demo Response:")
        st.write(response)

with tab2:
    st.header("Generate Practice Worksheets (Demo)")
    subject = st.selectbox("Worksheet Subject", subjects, key="worksheet_subject")
    num_q = st.slider("Number of Questions", 1, 5, 3)
    difficulty = st.radio("Select Difficulty", ["Easy", "Medium", "Hard"], horizontal=True)
    if st.button("Generate Worksheet PDF"):
        questions = [f"{i+1}. Sample {difficulty} question in {subject}" for i in range(num_q)]
        answers = [f"Sample Answer {i+1}" for i in range(num_q)]
        pdf = generate_pdf(questions, answers)
        st.download_button("📄 Download PDF", pdf, file_name="worksheet_demo.pdf")
