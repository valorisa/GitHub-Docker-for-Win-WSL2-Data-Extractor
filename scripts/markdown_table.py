import json

# Charger les données depuis le fichier
with open('fixed_formatted_result.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Générer un tableau Markdown
markdown_table = "| Title | Body | Comments URL |\n|-------|------|--------------|\n"
for issue in data:
    title = issue["title"].replace("\n", " ")  # Remplacer les sauts de ligne dans le titre
    body = issue["body"].replace("\n", " ")[:100] + "..."  # Lier la description à 100 caractères
    comments_url = issue["comments_url"]
    markdown_table += f"| {title} | {body} | {comments_url} |\n"

# Écrire le tableau Markdown dans un fichier
with open('issues.md', 'w', encoding='utf-8') as file:
    file.write(markdown_table)

print("Tableau Markdown généré dans issues.md")
