"""104 - Word Frequency Analyzer"""
from collections import Counter
from pathlib import Path
import re

def extract_words(text):
    return re.findall(r"[A-Za-z0-9']+", text.lower())

def analyze_text(text):
    words = extract_words(text)
    counter = Counter(words)
    return {
        "total_words": len(words),
        "unique_words": len(counter),
        "most_common": counter.most_common(10)
    }

def analyze_file(filename):
    return analyze_text(Path(filename).read_text(encoding="utf-8"))

def main():
    text = """
    Python is easy to learn. Python is powerful and Python is popular.
    Learning Python helps developers build useful applications.
    """
    result = analyze_text(text)
    print("Total words:", result["total_words"])
    print("Unique words:", result["unique_words"])
    print("Most common:", result["most_common"])

if __name__ == "__main__":
    main()
