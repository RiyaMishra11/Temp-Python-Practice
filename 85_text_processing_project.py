# 85 Text Processing Mini Project
import re
from collections import Counter
TEXT="""Python is powerful.
Python is easy to learn.
Learning Python improves problem solving.
Good programs use clear names."""
# 1 Normalize
print("1"," ".join(TEXT.lower().split()))
# 2 Words
words=re.findall(r"\b[a-z]+\b",TEXT.lower()); print("2",len(words))
# 3 Unique
print("3",sorted(set(words)))
# 4 Frequency
freq=Counter(words); print("4",freq.most_common(5))
# 5 Longest
print("5",max(words,key=len))
# 6 Starts with p
print("6",sorted({w for w in words if w.startswith("p")}))
# 7 Sentences
sent=[x.strip() for x in re.split(r"[.!?]+",TEXT) if x.strip()]; print("7",len(sent))
# 8 Capitalized
print("8",re.findall(r"\b[A-Z][a-z]+\b",TEXT))
# 9 Whitespace cleanup
messy="Python   is\n awesome\t."; print("9",re.sub(r"\s+"," ",messy).strip())
# 10 Keyword search
def search(text,key): return [s.strip() for s in re.split(r"[.!?]+",text) if key.lower() in s.lower()]
print("10",search(TEXT,"python"))
# 11 Full analyzer
def analyze(text):
 w=re.findall(r"\b[a-z]+\b",text.lower())
 return {"characters":len(text),"words":len(w),"unique":len(set(w)),"sentences":len([s for s in re.split(r"[.!?]+",text) if s.strip()]),"avg_word_len":round(sum(map(len,w))/len(w),2),"top":Counter(w).most_common(5)}
print("11",analyze(TEXT))
