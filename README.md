# GitHub-Docker-for-Win-WSL2-Data-Extractor

This project aims to extract, analyze, and synthesize GitHub issues related to the [docker/for-win](https://github.com/docker/for-win) repository with the label `area/WSL2`, synthesize data from GitHub issues associated with the docker/for-win repository, focusing specifically on issues related to WSL2 (Windows Subsystem for Linux 2). This is an initiative to better understand recurring errors, problematic configurations and the needs of Docker Desktop users on Windows.

## Objectives
- Extract GitHub issues using the GitHub REST API.
- Analyze issue titles, descriptions, and comments.
- Generate reports in Markdown or CSV format.
- Identify trends and recurring problems.

## Project Structure
The project is organized as follows:

```plaintext
GitHub-Docker-for-Win-WSL2-Data-Extractor/
.
├── .git/                   # Git repository metadata  
│   ├── HEAD  
│   ├── branches/  
│   ├── config  
│   ├── description  
│   ├── hooks/  
│   ├── index  
│   ├── info/  
│   ├── logs/  
│   ├── objects/  
│   ├── packed-refs  
│   └── refs/  
├── .gitignore               # Specifies files and directories to be ignored by Git  
├── LICENSE                  # Project license  
├── README.md                # Main project documentation  
├── installation_guide.md     # Installation guide  
├── project_structure.txt     # Project structure details  
├── requirements.txt          # List of dependencies  
├── result.txt                # Raw result data  

## Data Directory
├── data/                     # Extracted raw data  
│   ├── fixed_formatted_result.txt  # Fixed formatted result  
│   ├── formatted_result.txt        # Formatted result  
│   └── result.txt                  # Raw result  

## Output Directory
├── output/                   # Generated results (Markdown, CSV, etc.)  
│   └── issues.md             # List of identified issues  

## Scripts Directory
├── scripts/                  # Python scripts for data processing and analysis  
│   ├── analyze_word_frequencies.py  # Word frequency analysis  
│   ├── convert_to_csv.py             # Converts extracted data to CSV  
│   ├── generate_markdown_table.py     # Creates Markdown tables  
│   ├── generate_summary.py            # Generates a summary  
│   └── markdown_table.py              # Markdown table utility  

## Summary
- 11 directories, 21 files
```

## Prerequisites
Python 3.12.x and
Python libraries: ```requests```, ```pandas```, ```transformers```.
A personal GitHub token for API authentication.

## Usage
Place the raw data in the ```data/``` folder.
Run the Python scripts from the ```scripts/``` folder.

```bash
python scripts/generate_markdown_table.py
python scripts/convert_to_csv.py
python scripts/analyze_word_frequencies.py
python scripts/generate_summary.py
```
Check the results in the ```output/``` folder.

## Available Scripts
```generate_markdown_table.py``` : Generates a Markdown table from JSON data.
```convert_to_csv.py``` : Converts JSON data into a CSV file.
```analyze_word_frequencies.py``` : Counts the most frequent words in titles.
```generate_summary.py``` : Generates an automatic summary of descriptions.

## Contributions
Contributions are welcome ! Feel free to submit pull requests or report issues.

## License
This project is distributed under the MIT License. See the LICENSE file for more details.
