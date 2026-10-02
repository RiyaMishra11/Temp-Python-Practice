"""96 - URL Shortener"""
import secrets
import string

class URLShortener:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}

    def shorten(self, url):
        if url in self.long_to_short:
            return self.long_to_short[url]

        alphabet = string.ascii_letters + string.digits
        while True:
            code = "".join(secrets.choice(alphabet) for _ in range(6))
            if code not in self.short_to_long:
                break

        self.short_to_long[code] = url
        self.long_to_short[url] = code
        return code

    def expand(self, code):
        return self.short_to_long.get(code)

def main():
    shortener = URLShortener()
    url = "https://example.com/python-project"
    code = shortener.shorten(url)

    print("Original:", url)
    print("Short code:", code)
    print("Expanded:", shortener.expand(code))

if __name__ == "__main__":
    main()
