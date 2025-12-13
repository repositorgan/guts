from app.summarizer import summarize_text

if __name__ == "__main__":
    text = open("input.txt").read()
    result = summarize_text(text)
    print(result["summary"])
