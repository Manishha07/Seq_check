#8 August 2026
#Seq_check: A simple quality-control tool for FASTA sequences
import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from Bio import SeqIO
'''
It includes:

FASTA file upload
Sequence parsing with Biopython
Sequence count and total bases
Minimum, maximum, and average lengths
GC content calculation
Ambiguous N base count and percentage
Duplicate sequence detection
Sequence-length bar chart
QC report table
CSV download button
'''


st.set_page_config(
    page_title="SeqCheck",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 SeqCheck")
st.write(
    "A simple quality-control tool for FASTA sequences."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload a FASTA file",
    type=["fasta", "fa", "fna", "txt"],
)

if uploaded_file is None:
    st.info("Upload a FASTA file to begin.")
    st.stop()

fasta_text = uploaded_file.read().decode("utf-8")

records = list(
    SeqIO.parse(
        io.StringIO(fasta_text),
        "fasta",
    )
)

if not records:
    st.error("No sequences were found in the FASTA file.")
    st.stop()

lengths = [len(record.seq) for record in records]

sequence_count = len(records)
total_length = sum(lengths)
minimum_length = min(lengths)
maximum_length = max(lengths)
average_length = total_length / sequence_count

total_gc = 0

for record in records:
    sequence = str(record.seq).upper()
    total_gc += sequence.count("G")
    total_gc += sequence.count("C")

gc_content = (total_gc / total_length) * 100 if total_length else 0

ambiguous_bases = 0

for record in records:
    sequence = str(record.seq).upper()
    ambiguous_bases += sequence.count("N")

ambiguous_percentage = (
    (ambiguous_bases / total_length) * 100
    if total_length
    else 0
)

sequences = [
    str(record.seq).upper()
    for record in records
]

unique_sequences = set(sequences)
duplicate_count = len(sequences) - len(unique_sequences)

st.subheader("📊 Sequence Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Sequences", sequence_count)

with col2:
    st.metric("Total Bases", f"{total_length:,}")

with col3:
    st.metric("Average Length", f"{average_length:.1f} bp")

with col4:
    st.metric("GC Content", f"{gc_content:.1f}%")

st.divider()

st.subheader("🔍 Quality Checks")

col1, col2, col3 = st.columns(3)

with col1:
    if duplicate_count == 0:
        st.success("✅ No duplicate sequences")
    else:
        st.warning(
            f"⚠️ {duplicate_count} duplicate sequence(s) found"
        )

with col2:
    if ambiguous_bases == 0:
        st.success("✅ No ambiguous bases")
    else:
        st.warning(
            f"⚠️ {ambiguous_bases} ambiguous base(s) found "
            f"({ambiguous_percentage:.1f}% of all bases)"
        )

with col3:
    st.info(f"ℹ️ Shortest sequence: {minimum_length} bp")

st.divider()

st.subheader("📈 Sequence Length Distribution")

length_df = pd.DataFrame(
    {
        "Sequence": [record.id for record in records],
        "Length": lengths,
    }
)

st.bar_chart(length_df.set_index("Sequence"))

report = pd.DataFrame(
    {
        "Metric": [
            "Number of sequences",
            "Total bases",
            "Minimum length",
            "Maximum length",
            "Average length",
            "GC content (%)",
            "Ambiguous bases",
            "Ambiguous bases (%)",
            "Duplicate sequences",
        ],
        "Value": [
            sequence_count,
            total_length,
            minimum_length,
            maximum_length,
            round(average_length, 2),
            round(gc_content, 2),
            ambiguous_bases,
            round(ambiguous_percentage, 2),
            duplicate_count,
        ],
    }
)

st.divider()

st.subheader("📋 QC Report")

st.dataframe(
    report,
    use_container_width=True,
)

csv_data = report.to_csv(index=False)

st.download_button(
    label="⬇️ Download QC Report",
    data=csv_data,
    file_name="seqcheck_report.csv",
    mime="text/csv",
    type="primary",
)