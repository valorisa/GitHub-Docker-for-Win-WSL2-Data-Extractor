import json
from collections import Counter

# Charger les données depuis le fichier
with open('../data/fixed_formatted_result.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Compter les mots dans les titres
word_counts = Counter()
for issue in data:
    words = issue["title"].lower().split()
    word_counts.update(words)

print("Mots les plus fréquents dans les titres :")
print(word_counts.most_common(10))  # Afficher les 10 mots les plus fréquents
