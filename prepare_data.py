import os
import pandas as pd

def load_imdb_data(data_dir):
    texts = []
    labels = []

    for label_type in ['pos', 'neg']:
        dir_name = os.path.join(data_dir, label_type)
        for file in os.listdir(dir_name):
            with open(os.path.join(dir_name, file), encoding="utf-8") as f:
                texts.append(f.read())
                labels.append(1 if label_type == 'pos' else 0)

    return texts, labels

# Load train data
train_texts, train_labels = load_imdb_data("./aclImdb/train")

# Create DataFrame
df = pd.DataFrame({
    "text": train_texts,
    "label": train_labels
})

df.to_csv("imdb_train.csv", index=False)

print("Dataset saved successfully.")
