# Installation Guide for the Project

This guide provides step-by-step instructions to set up the Python environment and install the required libraries for this project.

---

## **1. Verify Python Installation**

Before proceeding, ensure that Python 3.x is installed on your system. You can check this by running:

```bash
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions. Make sure to select the option to add Python to your system's PATH during installation.

---

## **2. Create a Virtual Environment (Optional but Recommended)**

Using a virtual environment helps isolate the project's dependencies. To create and activate a virtual environment:

### On Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Once activated, you will see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

---

## **3. Install Required Libraries**

The project uses the following Python libraries:

- `requests`: For interacting with the GitHub API.
- `pandas`: For data manipulation and analysis.
- `transformers`: For generating automatic summaries using advanced language models.

To install these libraries, follow these steps:

### Step 1: Create a `requirements.txt` File
Create a file named `requirements.txt` in the root directory of your project and add the following content:

```plaintext
requests==2.31.0
pandas==2.1.4
transformers==4.36.2
```

### Step 2: Install the Libraries
Run the following command to install all the required libraries:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all the specified libraries and their dependencies.

---

## **4. Verify Installation**

After installation, you can verify that the libraries were installed correctly by listing all installed packages:

```bash
pip list
```

You should see the installed libraries (`requests`, `pandas`, `transformers`) in the output.

---

## **5. Run the Scripts**

Once the libraries are installed, you can execute the Python scripts located in the `scripts/` directory. For example:

```bash
python scripts/generate_markdown_table.py
python scripts/convert_to_csv.py
python scripts/analyze_word_frequencies.py
python scripts/generate_summary.py
```

These scripts will process the data and generate outputs in the `output/` directory.

---

## **6. Deactivate the Virtual Environment**

When you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

---

## **7. Troubleshooting Common Issues**

### **Issue 1: Missing Module Error**
If you encounter an error like `ModuleNotFoundError: No module named 'xxx'`, ensure that all libraries are installed by running:

```bash
pip install -r requirements.txt
```

### **Issue 2: Permission Errors**
If you face permission issues during installation, try adding the `--user` flag:

```bash
pip install -r requirements.txt --user
```

### **Issue 3: Incompatible Python Version**
Ensure you are using Python 3.7 or higher. Some libraries, such as `transformers`, require a recent version of Python.

---

## **8. Explanation of Libraries**

Here’s a brief overview of the libraries used in this project:

1. **`requests`**:  
   - Used to send HTTP requests to the GitHub API for extracting issue data.

2. **`pandas`**:  
   - Used for handling structured data, such as converting JSON data into CSV format.

3. **`transformers`**:  
   - Provides pre-trained language models for tasks like summarization, enabling automatic generation of summaries from issue descriptions.

---

With these steps, you should be able to successfully install and use the required Python libraries for this project. If you encounter any issues or have further questions, feel free to ask!
