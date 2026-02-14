import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertForSequenceClassification
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# =====================
# Initialize App
# =====================
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# =====================
# Load Model (Only Once)
# =====================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

tokenizer = BertTokenizer.from_pretrained("imdb_bert_model")
model = BertForSequenceClassification.from_pretrained("imdb_bert_model")

model.to(device)
model.eval()

print("Model loaded successfully.")


# =====================
# Home Route
# =====================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# =====================
# Prediction Route
# =====================
@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, review: str = Form(...)):

    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        prediction_id = torch.argmax(probs, dim=1).item()

    confidence = probs[0][prediction_id].item()

    label = "Positive 😊" if prediction_id == 1 else "Negative 😠"
    color_class = "positive" if prediction_id == 1 else "negative"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": label,
            "confidence": f"{confidence:.4f}",
            "color_class": color_class
        }
    )


# =====================
# Run with python main.py
# =====================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
