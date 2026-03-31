<div align="center">

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Clapper%20Board.png" alt="Clapper Board" width="80" height="80" />

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=40&pause=1000&color=4F46E5&center=true&vCenter=true&width=800&lines=IMDB+Sentiment+Analyzer;Deep+Learning+Web+Application;Fine-Tuned+BERT+Transformer;Powered+by+FastAPI+%26+PyTorch" alt="Typing SVG" />

**An end-to-end Machine Learning web application that analyzes movie reviews and predicts sentiment.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch Badge" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace Badge" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge" />
  <img src="https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2 Badge" />
</p>

[Explore The Code](#project-structure) · [Report Bug](https://github.com/Bersinberz/Movie_review/issues) · [Request Feature](https://github.com/Bersinberz/Movie_review/issues)

</div>

---

## 🌟 Overview

The **IMDB Sentiment Analyzer** is an end-to-end Machine Learning pipeline that takes raw textual movie reviews and classifies their sentiment as <span style="color:green; font-weight:bold;">Positive 😊</span> or <span style="color:red; font-weight:bold;">Negative 😠</span>. 

It demonstrates the full lifecycle of an ML project, from fine-tuning a generic `bert-base-uncased` transformer on the IMDB dataset, to deploying a high-performance inference server using **FastAPI** with a server-side rendered **Jinja2** frontend.

## ✨ Key Features

- 🧠 **Transformer Architecture:** Customized and fine-tuned BERT models for industry-standard NLP text classification.
- ⚡ **GPU-Accelerated Processing:** Optimized model training and rapid inference leveraging CUDA on NVIDIA hardware.
- 🚀 **High-Performance API:** Asynchronous Python backend utilizing **FastAPI** for low-latency responses.
- 🎨 **Dynamic Interface:** Light-weight, server-side rendered UI utilizing **Jinja2** templates.

<br>

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" alt="Magnifying Glass" width="40" height="40" />
</div>

## 📊 Model Specifications

We successfully fine-tuned the base BERT model on the **IMDB Large Movie Review Dataset**:

| Metric | Details | Value |
| :--- | :--- | :--- |
| **Foundation Model** | Hugging Face Transformers | `bert-base-uncased` |
| **Dataset Configuration** | Balanced Train/Test Split | 25,000 Samples |
| **Validation Accuracy** | High-fidelity predictions | **~91%** |
| **Architecture Scale** | Total Trainable Params | 110M+ Parameters |
| **Training Performance** | Optimization via AdamW (3 Epochs) | Loss `0.26 → 0.07` |

---

## 📁 Repository Anatomy

```bash
Movie_review/
├── 📄 main.py              # 🚀 FastAPI Application Entry Point
├── 📄 prepare_data.py      # 🧹 Data Loading and Preprocessing Script
├── 📄 test.py              # 🧪 Model Inference & Evaluation Script
├── 📊 imdb_train.csv       # 📝 Processed Training Data Formats
├── 📓 train_imdb.ipynb     # 🧠 Core Model Fine-Tuning Notebook
├── 📓 verify.ipynb         # ✅ Model Validation & Metrics Notebook
│
├── 📂 templates/           # 🎨 Frontend Rendering Engine
│   └── 📄 index.html       # Web Interface (Jinja2)
│
├── 📂 imdb_bert_model/     # 📦 Saved Fine-tuned Transformer Checkpoints
└── 🚫 .gitignore           # Git ignore definitions
```

---

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" alt="Gear" width="50" height="50" />
</div>

## ⚙️ Quick Start Installation

Follow these instructions to set up the sentiment analyzer on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bersinberz/Movie_review.git
cd Movie_review
```

### 2️⃣ Initialize Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ System Dependencies

**Using GPU Acceleration Engine (Recommended for Inference):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers fastapi uvicorn jinja2 pandas scikit-learn
```

**Using Standard CPU Processing:**
```bash
pip install torch transformers fastapi uvicorn jinja2 pandas scikit-learn
```

---

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Play%20Button.png" alt="Play Button" width="50" height="50" />
</div>

## ▶️ Execution Guide

Launch the high-performance application server directly through your command line or ide.

```bash
python main.py
```

The application will initialize the neural network and stream to:
> **http://127.0.0.1:8000**

### Testing a Real-World Scenario

**Incoming Request:**
```text
The cinematography was absolutely breathtaking, but the plot felt significantly rushed towards the end. Still, a solid watch!
```

**Model Output Resolution:**
```json
{
  "Sentiment": "Positive 😊",
  "Confidence": 0.9723
}
```

---

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" alt="Handshake" width="50" height="50" />
</div>

## 🤝 Contribution Guidelines

Contributions, issues, and feature requests are always welcome! Feel free to check the [issues page](https://github.com/Bersinberz/Movie_review/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<p align="center">
  Developed by <b>Bersinberz</b>
</p>
