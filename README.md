# Local AI Study Assistant

A terminal-based AI study assistant built using Python and Ollama that runs a locally hosted LLaMA language model.  
The application allows users to ask study-related questions directly from the command line and receive clear, contextual explanations — completely offline and without relying on cloud APIs.

This project demonstrates how to integrate local large language models into Python applications, design interactive CLI tools, and build AI-powered learning utilities using terminal-based workflows.

## Why This Project?
  
This project focuses on running and controlling a large language model locally, giving full control over data, performance, and interaction flow.

It highlights practical skills such as:
- Local LLM deployment
- Python-based AI integration
- Command-line application design
- Prompt handling and response parsing

## Technologies Used
- Python
- Ollama
- LLaMA (local model)
- Terminal / CLI
- Git & GitHub

## Intended Use

- Students learning Python or machine learning concepts
- Developers exploring local AI workflows
- Anyone interested in offline AI-powered study tools

# AI Study Helper

An AI-powered study assistant built using **Ollama Llama3**, designed to help users ask questions, get explanations, and generate study notes.

This project demonstrates **Python programming**, **LLM integration**, and **terminal-based application development**.

---

## Features

- Ask study-related questions in the terminal
- Get AI-generated explanations and summaries
- Easily extendable for new subjects or topics
- Designed for local LLM usage (Ollama + Llama3)

---
**Memory Management in the AI Assistant (1st upgradation)**

This project implements conversational memory to allow the local LLM to understand and respond to follow-up questions naturally. Instead of treating every user input as a new conversation, the assistant maintains a history of recent user questions and AI responses. To prevent unlimited memory growth—which can degrade performance and increase context confusion—a sliding window memory strategy is used. Only the most recent interactions are retained, ensuring relevant context is preserved while keeping the system efficient and stable. This approach mirrors how real-world LLM-based chat systems manage conversational context.


## Tech Stack

- Python 3.10+
- Ollama Llama3 (local model)
- Terminal / CLI interface
- Optional: `requirements.txt` for dependencies

---

## Project Structure

<img width="418" height="204" alt="Screenshot 2026-01-19 at 21 11 34" src="https://github.com/user-attachments/assets/fe1ba292-dc28-4010-bc9c-f29a1514e0f1" />


---

## ⚡ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/saikatgayen/AI_study_helper.git
cd AI_study_helper

2. **Setup Python virtual env** 
python -m venv venv
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows

3. **Install Python dependencies**
pip install -r requirements.txt

4. **Install Ollama and pull Llama3 model**
# Install Ollama: https://ollama.com/
ollama pull llama3

5. **Run the Study Helper**
python app.py

Notes

Models are not included in the repository due to size constraints. Users must download Llama3 locally.

Ensure Ollama is installed and running before starting the project.

Designed for terminal/CLI usage. GUI integration can be added later.
