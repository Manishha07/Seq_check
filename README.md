🔬 SeqCheck

A lightweight bioinformatics tool for performing quick quality-control checks on FASTA sequence files.
SeqCheck is a beginner-friendly web application that helps students, researchers, and bioinformaticians perform an initial quality check of FASTA datasets.

The tool calculates basic sequence statistics, identifies common sequence issues, visualizes sequence-length distribution, and allows users to download the results as a CSV report.

📌 Overview

FASTA files are widely used to store DNA, RNA, and protein sequences. Before using a sequence dataset for downstream 
bioinformatics analysis, it is useful to check its basic properties and identify potential issues.
SeqCheck provides a simple interface for performing these initial checks without requiring users to manually calculate statistics or use command-line tools.

The application analyzes uploaded FASTA files and provides information about:

Number of sequences
Total sequence length
Minimum sequence length
Maximum sequence length
Average sequence length
GC content
Ambiguous bases
Duplicate sequences

✨ Features

📂 Upload FASTA files
🔢 Count the number of sequences
📏 Calculate total sequence length
📊 Calculate minimum, maximum, and average sequence length
🧬 Calculate GC content
⚠️ Detect ambiguous bases (N)
🔍 Identify duplicate sequences
📈 Visualize sequence-length distribution
📄 Generate a downloadable CSV QC report
🖥️ Screenshots
        Home Page
        QC Results

🛠️ Tech Stack

Python — Core application development
Biopython — FASTA parsing and sequence processing
Pandas — Data organization and CSV report generation
Matplotlib — Sequence-length visualization
Streamlit — Interactive web interface

📁 Project Structure

SeqCheck/
│
├── app.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── sample_data/
│   └── sample.fasta
│
└── screenshots/
    ├── home.png
    └── results.png

⚙️ Installation

1. Clone the repository
git clone https://github.com/Manishha07/SeqCheck.git

2. Navigate to the project directory
cd SeqCheck

3. Install the required packages
pip install -r requirements.txt

▶️ Run the Application

Start the Streamlit application with:
streamlit run app.py
The application will open in your web browser.

🧪 Example Workflow

Launch SeqCheck.
Upload a FASTA file.
View the number of sequences and basic sequence statistics.
Check GC content and ambiguous bases.
Identify duplicate sequences.
Explore the sequence-length distribution.
Download the QC results as a CSV file.

📄 Sample Data

A sample FASTA file is included in the sample_data folder.
It can be used to test the application without requiring an external dataset.
sample_data/sample.fasta

🔬 Example Output

SeqCheck provides a summary similar to:

Number of sequences     8
Total bases             200+
Minimum length          XX bp
Maximum length          XX bp
Average length          XX bp
GC content              XX.X %
Ambiguous bases         X
Duplicate sequences     X

The values will vary depending on the uploaded FASTA file.

🎯 Intended Use

SeqCheck is intended for:
Students learning bioinformatics
Beginners working with FASTA files
Researchers performing preliminary sequence checks
Quick inspection of sequence datasets before downstream analysis

SeqCheck is designed as a basic first-pass QC tool and is not intended to replace specialized sequence-quality or downstream bioinformatics pipelines.

🚀 Future Improvements

Sequence-type detection (DNA/RNA/Protein)
GC-content distribution
More detailed QC scoring
FASTQ support
Additional sequence-quality metrics
Improved visualizations
Detailed sequence-level QC reports

📚 Skills Demonstrated

This project demonstrates practical experience with:
Python programming
FASTA file processing
Biopython
Basic sequence analysis
Pandas
Data visualization
Streamlit
CSV report generation
Git and GitHub

👩‍💻 Author

Manisha R.
Integrated Master's StudentSystems and Computational Biology
Interested in:
Bioinformatics
Computational Biology
Artificial Intelligence
Scientific Software Development

📜 License

This project is licensed under the MIT License.
See the LICENSE file for more information.

⭐ Acknowledgements

This project makes use of the following open-source Python libraries:
Biopython
Streamlit
Pandas
Matplotlib