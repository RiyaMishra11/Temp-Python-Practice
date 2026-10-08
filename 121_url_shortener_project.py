# 121 URL Shortener Mini Project
import hashlib
import string
import random

def valid(url):
    return url.startswith(("http://","https://"))
print("1.",valid("https://example.com"))

def random_code(n=6):
    chars=string.ascii_letters+string.digits
    return "".join(random.choice(chars) for _ in range(n))
print("2.",random_code())

def hash_code(url):
    return hashlib.sha256(url.encode()).hexdigest()[:8]
print("3.",hash_code("https://example.com"))

url_map={}
code_map={}

def shorten(url):
    if not valid(url): raise ValueError("Invalid URL")
    code=hash_code(url)
    url_map[code]=url
    code_map[url]=code
    return code
code=shorten("https://example.com")
print("5.",code)

def expand(code):
    return url_map.get(code)
print("6.",expand(code))

def shorten_unique(url):
    if url in code_map: return code_map[url]
    return shorten(url)
print("7.",shorten_unique("https://example.com"))

for url in ["https://python.org","https://github.com","https://example.com/docs"]:
    shorten_unique(url)
print("8.",url_map)

def delete(code):
    url=url_map.pop(code,None)
    if url:
        code_map.pop(url,None)
        return True
    return False
print("9.",delete(code))

def stats():
    return {"total":len(url_map),"codes":list(url_map)}
print("10.",stats())

class URLShortener:
    def __init__(self):
        self.urls={}
        self.codes={}
    def shorten(self,url):
        if not valid(url): raise ValueError("Invalid URL")
        if url in self.codes: return self.codes[url]
        code=hash_code(url)
        while code in self.urls and self.urls[code]!=url:
            code=random_code()
        self.urls[code]=url
        self.codes[url]=code
        return code
    def expand(self,code):
        return self.urls.get(code)
    def count(self):
        return len(self.urls)

s=URLShortener()
c=s.shorten("https://www.python.org/")
print("11.",c,s.expand(c),s.count())
