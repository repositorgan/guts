from model import summarize_text
from utils import load_text


if __name__ == "__main__":
text = load_text("sample_input.txt")
summary = summarize_text(text)
print("SUMMARY:\n", summary)
