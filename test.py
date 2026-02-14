import torch
from transformers import BertTokenizer, BertForSequenceClassification
import torch.nn.functional as F


def load_trained_model(model_path="imdb_bert_model"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)
    
    model.to(device)
    model.eval()
    
    return tokenizer, model, device


def interactive_predict():
    tokenizer, model, device = load_trained_model()
    
    print("🎬 IMDB Sentiment Analyzer")
    print("Type 'exit' to stop.\n")
    
    while True:
        text = input("Enter movie review: ")
        
        if text.lower() == "exit":
            print("Exiting...")
            break
        
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)
            prediction = torch.argmax(probs, dim=1).item()

        confidence = probs[0][prediction].item()
        label = "Positive 😊" if prediction == 1 else "Negative 😠"

        print(f"Prediction: {label}")
        print(f"Confidence: {confidence:.4f}\n")


# Run it
interactive_predict()
