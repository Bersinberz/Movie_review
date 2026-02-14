# 🎬 IMDB Sentiment Analyzer (BERT + FastAPI)

A Deep Learning web application that predicts whether a movie review is **Positive** or **Negative** using a fine-tuned BERT transformer model.

This project demonstrates:
- Transformer fine-tuning with PyTorch
- GPU training using CUDA
- Model inference with FastAPI
- HTML templating using Jinja2
- End-to-end ML deployment

---

## 🚀 Tech Stack

- Python
- PyTorch (CUDA enabled)
- Hugging Face Transformers
- FastAPI
- Jinja2
- HTML + CSS
- NVIDIA GPU (optional but recommended)

---

## 🧠 Model Information

- Base Model: `bert-base-uncased`
- Fine-tuned on: IMDB Large Movie Review Dataset
- Training Samples: 25,000
- Validation Accuracy: ~91%
- Parameters: 110M+

---

## 📁 Project Structure

```
project/
│
├── main.py
├── prepare_data.py
├── test.py
├── imdb_train.csv
├── train_imdb.ipynb
├── verify.ipynb
│
├── templates/
│     └── index.html
│
├── imdb_bert_model/   (trained model)
├── aclImdb/           (raw dataset)
└── .gitignore
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

---

## 2️⃣ Create Virtual Environment

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

### CPU Version:
```bash
pip install torch transformers fastapi uvicorn jinja2 pandas scikit-learn
```

### GPU Version (Recommended):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Then install remaining:
```bash
pip install transformers fastapi uvicorn jinja2 pandas scikit-learn
```

---

# ▶️ Run The Web Application

Inside the project folder:

```bash
python main.py
```

Then open your browser:

```
http://127.0.0.1:8000
```

---

# 💻 Run Inside VS Code

1. Open VS Code
2. Click **File → Open Folder**
3. Select the project folder
4. Open Terminal in VS Code:
   ```
   Ctrl + `
   ```
5. Activate virtual environment:
   ```
   venv\Scripts\activate
   ```
6. Run:
   ```
   python main.py
   ```
7. Open browser:
   ```
   http://127.0.0.1:8000
   ```

---

# 🎯 How It Works

1. User enters a movie review.
2. FastAPI receives the form submission.
3. The fine-tuned BERT model processes the text.
4. Sentiment prediction is generated.
5. Result + confidence score is rendered in HTML.

---

# 🧪 Example

Input:
```
This movie was absolutely amazing!
```

Output:
```
Positive 😊
Confidence: 0.97
```

---

# 📊 Model Training

Training was performed using:
- PyTorch DataLoader
- AdamW Optimizer
- Cross-Entropy Loss
- 3 Epochs
- GPU acceleration (RTX 3070 Ti)

Training loss decreased from:
```
0.26 → 0.14 → 0.07
```

---

# 🔥 Future Improvements

- Add REST JSON API endpoint
- Add probability bar chart visualization
- Add Docker support
- Deploy to cloud (Render / AWS)
- Convert frontend to React
- Push model to Hugging Face Hub

---

## 👨‍💻 Author

Built using Transformers and GPU acceleration for real-world NLP deployment.
