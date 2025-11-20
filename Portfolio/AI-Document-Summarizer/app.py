# We want to produce a text file summary. 

# Import functions from module and reading input files.
from model import summarize_text
from utils import load_text

# Run code when file is executed directly only. Exclude when imported as a script or module.
if __name__ == "__main__":

# Load raw text file to produce string of text file content.
text = load_text("sample_input.txt")

# Pass result through function to reduce volume.
summary = summarize_text(text)

# Deliver consolidation to the console.
print("SUMMARY:\n", summary)
