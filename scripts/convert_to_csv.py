import json
import csv

# Charger les données depuis le fichier
with open('../data/fixed_formatted_result.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Écrire les données dans un fichier CSV
with open('../output/issues.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'body', 'comments_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for issue in data:
        writer.writerow({
            "title": issue["title"],
            "body": issue["body"],
            "comments_url": issue["comments_url"]
        })

print("Fichier CSV généré dans ../output/issues.csv")
