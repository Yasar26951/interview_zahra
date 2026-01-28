# Zahra – AI Interview Preparation Assistant 🤖🎯

Zahra is an AI-powered interview preparation assistant designed to help students answer interview questions **clearly, professionally, and confidently**.  
The system is built using a **fine-tuned Large Language Model (LLM)** with **QLoRA**, orchestrated through **LangGraph** for structured conversational flow.

---

## 🚀 Features

- 💬 Provides clear and professional answers to interview questions  
- 🧠 Fine-tuned LLM using **QLoRA** for efficient training on limited compute  
- 🔁 Structured conversation handling using **LangGraph**  
- 🎯 Focused on interview concepts, HR questions, and behavioral answers  
- ⚡ Optimized inference using Hugging Face pipelines  

---

## 🏗️ Architecture Overview

- **Base Model:** Qwen2.5-3B-Instruct  
- **Fine-tuning:** QLoRA (PEFT)  
- **Prompting Style:** Instruction–Context–Response format  
- **Orchestration:** LangGraph (state-based execution)  
- **Inference:** Hugging Face `pipeline` + LangChain wrapper  

---

## 📁 Project Structure
```
Zahra_interview/
│
├── backend/
│ ├── agent.py # LangGraph logic and response generation
│ ├── app.py # Backend entry point (API / server logic)
│
├── frontend/
│ ├── index.html # Chat UI
│ ├── script.js # Frontend interaction logic
│ └── style.css # Styling
│
└── README.md
```

---

## 🧠 Prompt Template Used

The model was fine-tuned and invoked using the following structured format:

Instruction:
You are a helpful interview assistant called Zahra.
Help the student answer interview questions professionally and clearly.

Context:
<User Question>
Response:
<Model Answer> ```
This ensures consistent, role-aligned, and concise responses.

⚙️ Setup Instructions
1️⃣ Clone the Repository
``` bash
git clone https://github.com/Yasar26951/interview_zahra.git
cd Zahra_interview
```
2️⃣ Create Virtual Environment
``` bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
3️⃣ Install Dependencies
``` bash
pip install -r requirement.txt
```
▶️ Running the Application
Backend
```bash
python backend/app.py
```
Frontend
Open frontend/index.html in a browser.


