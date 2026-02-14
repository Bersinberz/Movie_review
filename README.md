<div align="center">

# IMDB Sentiment Analyzer
### BERT + FastAPI + PyTorch

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)

<br />

**A Deep Learning web application that predicts whether a movie review is  
<span style="color:green">Positive</span> or <span style="color:red">Negative</span>  
using a fine-tuned BERT transformer model.**

</div>

---

## 🚀 Project Overview

This project demonstrates an **end-to-end Machine Learning pipeline**, moving from raw data to a deployed web application.

- ⚡ **Transformer Fine-tuning:** Customized `bert-base-uncased` for sentiment classification.
- 🏎️ **GPU Acceleration:** Training optimized with CUDA on NVIDIA hardware.
- 🌐 **Modern Backend:** High-performance inference API using **FastAPI**.
- 🎨 **Dynamic Frontend:** Server-side rendering with **Jinja2 Templates**.

---

## 🧠 Model Information

We fine-tuned BERT on the **IMDB Large Movie Review Dataset**.

| Metric | Value | Details |
| :--- | :--- | :--- |
| **Base Model** | `bert-base-uncased` | Hugging Face Transformers |
| **Dataset Size** | 25,000 Samples | Balanced (Positive / Negative) |
| **Validation Accuracy** | **~91%** | High fidelity prediction |
| **Parameters** | 110M+ | Fine-tuned weights |
| **Loss Trajectory** | `0.26 → 0.07` | 3 Epochs / AdamW |

---

## 📁 Project Structure

```bash
Movie_review/
├── 📄 main.py              # FastAPI Application Entry Point
├── 📄 prepare_data.py      # Data Preprocessing Script
├── 📄 test.py              # Model Inference Testing
├── 📊 imdb_train.csv       # Processed Training Data
├── 📓 train_imdb.ipynb     # Training Notebook
├── 📓 verify.ipynb         # Verification Notebook
│
├── 📂 templates/
│   └── 🎨 index.html       # Web Interface (Jinja2)
│
├── 📂 imdb_bert_model/     # Saved Fine-tuned Model
└── 🚫 .gitignore           # Git Ignore Rules
```

---

# ⚙️ Setup Instructions

Follow these steps to run the application locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bersinberz/Movie_review.git
cd Movie_review
```

---

## 2️⃣ Environment Setup

### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 🍎 Mac / 🐧 Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

### 🚀 GPU Version (Recommended)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers fastapi uvicorn jinja2 pandas scikit-learn
```

### 💻 CPU Version

```bash
pip install torch transformers fastapi uvicorn jinja2 pandas scikit-learn
```

---

# ▶️ Running the App

### Via Command Line

```bash
python main.py
```

The server will start at:

```
http://127.0.0.1:8000
```

---

### Via VS Code

1. Open the `Movie_review` folder.
2. Open Terminal (`Ctrl + ~`)
3. Activate environment:
   ```
   venv\Scripts\activate
   ```
4. Run:
   ```
   python main.py
   ```

---

## 🧪 Real-World Example

### Input:

```
The cinematography was breathtaking, but the plot felt rushed towards the end. Still, a solid watch!
```

### Model Output:

```json
{
  "Sentiment": "Positive 😊",
  "Confidence": 0.97
}
```

---

# 🔥 Roadmap

- [ ] Add REST JSON API endpoint (`/api/predict`)
- [ ] Probability visualization chart (Chart.js)
- [ ] Dockerize the application
- [ ] Deploy on Render / AWS
- [ ] Push model to Hugging Face Hub

---

<div align="center">

## 👨‍💻 Author

**Bersin**

Built with ❤️ using PyTorch & FastAPI

</div>
