# GitHub-Docker-for-Win-WSL2-Data-Extractor

This project aims to extract, analyze, and synthesize GitHub issues related to the [docker/for-win](https://github.com/docker/for-win) repository with the label `area/WSL2`.

## Objectives
- Extract GitHub issues using the GitHub REST API.
- Analyze issue titles, descriptions, and comments.
- Generate reports in Markdown or CSV format.
- Identify trends and recurring problems.

## Project Structure
The project is organized as follows:

```plaintext
GitHub-Docker-for-Win-WSL2-Data-Extractor/
├── data/               # Raw extracted data
│   ├── fixed_formatted_result.txt
│   ├── formatted_result.txt
│   └── result.txt
├── output/             # Generated results (Markdown, CSV, etc.)
│   └── issues.md
├── scripts/            # Python scripts for extraction and analysis
│   ├── generate_markdown_table.py
│   ├── convert_to_csv.py
│   ├── analyze_word_frequencies.py
│   └── generate_summary.py
├── README.md           # Project documentation
└── .gitignore          # List of files/folders to ignore


## Prerequisites
Python 3.x
Python libraries: requests, pandas, transformers
A personal GitHub token for API authentication.
## Usage
Place the raw data in the data/ folder.
Run the Python scripts from the scripts/ folder

```bash
python scripts/generate_markdown_table.py
python scripts/convert_to_csv.py
python scripts/analyze_word_frequencies.py
python scripts/generate_summary.py
```
Check the results in the output/ folder.

## Available Scripts
generate_markdown_table.py : Generates a Markdown table from JSON data.
convert_to_csv.py : Converts JSON data into a CSV file.
analyze_word_frequencies.py : Counts the most frequent words in titles.
generate_summary.py : Generates an automatic summary of descriptions.

## Contributions
Contributions are welcome! Feel free to submit pull requests or report issues.

## License
This project is distributed under the MIT License. See the LICENSE file for more details.
