# genai
## Problem statement:
Building a Question-Answering System for PDF Documents

Many organizations and individuals have valuable information stored in PDF documents, but retrieving specific information from these documents can be time-consuming and challenging. The goal is to develop a system that can:

Automatically extract and process text from multiple PDF documents.
Handle user queries by understanding and retrieving relevant information from the processed text.
Provide accurate and contextually appropriate answers to user queries in real-time.

## Solution
This project creates a Flask-based chatbot to answer questions from PDF documents. It uses PyPDFLoader to load PDFs and RecursiveCharacterTextSplitter to split text into chunks. Embeddings are generated using HuggingFace Embeddings and stored in FAISS for efficient retrieval. The CTransformers model (Llama-2) generates responses, and LangChain's RetrievalQA chain manages the QA process.

## Tech stack
Backend Framework: Flask

PDF Processing: 
DirectoryLoader
PyPDFLoader

Text Processing:
RecursiveCharacterTextSplitter

Embeddings and Vector Store:
HuggingFace Embeddings
FAISS

Language Model:
CTransformers (Llama-2 model)

Prompt Engineering:
PromptTemplate

Application Logic:
LangChain (RetrievalQA Chain)

Web Interface:
HTML (index.html)

## Run Application

### Step 1-: download the model from Hugging face
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML

store the model in the model folder 
### store pdf in data folder 

### Step 2-: Clone the Repository
```bash
git clone https://github.com/NeHa77A/genai.git
```

### Step 3-: Create conda environment
```bash
conda create -p ./venv python=3.10 -y
```

### Step 4-: Activate Conda environment
```bash
conda activate venv/
```

### Step 5-: Install requirements
```bash
pip install -r requirements.txt
```

### Step 6-: run
```bash
python main.py
```
![](https://raw.githubusercontent.com/NeHa77A/genai/main/output.png)
