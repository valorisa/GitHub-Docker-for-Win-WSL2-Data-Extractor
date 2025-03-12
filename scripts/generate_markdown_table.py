import json

# Charger les données depuis le fichier
with open('../data/fixed_formatted_result.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Générer un tableau Markdown
markdown_table = "| Title | Body (Truncated) | Comments URL |\n|-------|------------------|--------------|\n"
for issue in data:
    title = issue.get("title", "No Title").replace("\n", " ")  # Remplacer les sauts de ligne dans le titre
    body = issue.get("body", "No Description").replace("\n", " ")[:100] + "..."  # Limiter la description à 100 caractères
    comments_url = issue.get("comments_url", "No URL")
    markdown_table += f"| {title} | {body} | {comments_url} |\n"

# Écrire le tableau Markdown dans un fichier
with open('../output/issues.md', 'w', encoding='utf-8') as file:
    file.write(markdown_table)

print("Tableau Markdown généré dans ../output/issues.md")
