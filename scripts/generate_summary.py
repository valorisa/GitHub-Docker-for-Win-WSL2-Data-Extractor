from transformers import pipeline
import json

# Charger les données depuis le fichier
with open('../data/fixed_formatted_result.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialiser le modèle de résumé
summarizer = pipeline("summarization")

# Concaténer toutes les descriptions
all_bodies = " ".join(issue["body"] for issue in data if issue["body"])

# Générer un résumé
summary = summarizer(all_bodies, max_length=50, min_length=25, do_sample=False)
print("Résumé des descriptions :")
print(summary[0]['summary_text'])
