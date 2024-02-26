# Lexical Analyzer for MS Small Basic

This Python-based lexical analyzer is designed to analyze source code written in MS Small Basic. It utilizes a clear LL(1) grammar to tokenize and identify lexical errors in the Small Basic code.

## Features

- **Tokenization:** The analyzer tokenizes input source code into meaningful tokens such as keywords, identifiers, literals, and symbols.
- **LL(1) Grammar:** Utilizes a LL(1) grammar to parse the input code efficiently and accurately.
- **Error Handling:** Detects and reports lexical errors in the input code, providing helpful messages for debugging and correction.
- **Python Implementation:** Implemented in Python, making it cross-platform and easy to integrate into existing workflows.

## Usage

1. **Install Python:** Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

2. **Clone Repository:** Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/yourusername/lexical-analyzer.git
    ```

3. **Install Jupyter Notebook:** If you haven't already, install Jupyter Notebook using pip:

    ```
    pip install notebook
    ```

4. **Run the Jupyter Notebook:** Navigate to the cloned directory and run the Jupyter Notebook server:

    ```
    jupyter notebook
    ```

5. **Open and Run the Notebook:** Open the `lexical.ipynb` notebook and execute the code cells to test the lexical analyzer with your Small Basic source code. Alternatively, you can use manual input via stdin.
