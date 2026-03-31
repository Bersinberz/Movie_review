<div align="center">

<!-- Animated Typing Header -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=40&pause=1000&color=3B82F6&center=true&vCenter=true&width=800&lines=IMDB+Sentiment+Analyzer;Deep+Learning+Web+Application;Fine-Tuned+BERT+Transformer;Powered+by+FastAPI+%26+PyTorch" alt="Typing SVG" />

<p align="center">
  <strong>An end-to-end Machine Learning web application that analyzes movie reviews and predicts sentiment.</strong>
</p>

<p align="center">
  <a href="#-stack"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" /></a>
  <a href="#-stack"><img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch Badge" /></a>
  <a href="#-stack"><img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace Badge" /></a>
  <a href="#-stack"><img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge" /></a>
  <a href="#-stack"><img src="https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2 Badge" /></a>
</p>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="3px">

</div>

## ✨ Key Features

- 🧠 **Transformer Architecture** — Customized and fine-tuned BERT models for industry-standard NLP text classification.
- ⚡ **GPU-Accelerated Processing** — Optimized model training and rapid inference leveraging CUDA on NVIDIA hardware.
- 🚀 **High-Performance API** — Asynchronous Python backend utilizing FastAPI for low-latency responses.
- 🎨 **Dynamic Interface** — Light-weight, server-side rendered UI utilizing Jinja2 templates.

<br>

## 🛠️ Stack

The project utilizes an end-to-end Machine Learning pipeline merged with a modern web backend.

**Core ML & Training 🧠**
> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white" /> <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" />

**Backend & Inference ⚙️**
> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/Uvicorn-499848?style=flat&logo=uvicorn&logoColor=white" /> <img src="https://img.shields.io/badge/Jinja2-B41717?style=flat&logo=jinja&logoColor=white" />

<br>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="3px">

## 🚀 Development

### 📋 Prerequisites
Ensure you have the following installed on your local environment before proceeding:
- Python 3.8+
- Active internet connection for downloading Hugging Face models
- (Optional) NVIDIA GPU with CUDA for accelerated inference

### 💻 Setup

<details>
<summary><b>Environment Configuration ⚙️</b> (Click to Expand)</summary>

1. First, clone the repository and navigate into it:
```bash
git clone https://github.com/Bersinberz/Movie_review.git
cd Movie_review
```

2. Initialize a virtual environment:

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
</details>

<details>
<summary><b>Dependencies Installation 📦</b> (Click to Expand)</summary>

Install the required packages based on your hardware capabilities:

**Using GPU Acceleration Engine (Recommended):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers fastapi uvicorn jinja2 pandas scikit-learn
```

**Using Standard CPU Processing:**
```bash
pip install torch transformers fastapi uvicorn jinja2 pandas scikit-learn
```
</details>

<br>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="3px">

## ▶️ Running the Application

### 1️⃣ Launch the Server

Launch the high-performance application server directly through your command line:

```bash
python main.py
```

> 💡 **Tip:** The application will initialize the neural network and stream to [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

### 2️⃣ Analyze a Review

Open the browser, paste a movie review into the UI, or send an API request:

**Model Output Example:**
```json
{
  "Sentiment": "Positive 😊",
  "Confidence": 0.9723
}
```

<br>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="3px">

## 🗂️ Project Structure

Using Mermaid standard graphs, observe our full project overview separating logic models perfectly per target layer:

```mermaid
graph TD;
    Root((Movie Review Root))-->MainApp[main.py];
    Root-->DataScripts[Data Scripts];
    Root-->Notebooks[Jupyter Notebooks];
    Root-->Frontend[templates/];
    Root-->ModelCheckpoints[imdb_bert_model/];
    
    DataScripts-->PrepData[prepare_data.py];
    DataScripts-->TestInfer[test.py];
    DataScripts-->Dataset[imdb_train.csv];
    
    Notebooks-->TrainModel[train_imdb.ipynb];
    Notebooks-->VerifyModel[verify.ipynb];
    
    Frontend-->IndexHTML[index.html];
```

<br>

<div align="center">
  <sub>Built with ❤️ by Bersinberz. © 2026</sub>
</div>
