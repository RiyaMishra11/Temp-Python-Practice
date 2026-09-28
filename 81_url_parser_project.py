# Python Practice 81: URL Parser Mini Project
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, urljoin

# 1. Parse URL
url = "https://example.com/products?id=10"
parsed = urlparse(url)
print("1. Scheme:", parsed.scheme)
print("   Host:", parsed.netloc)
print("   Path:", parsed.path)

# 2. Extract domain
def get_domain(url):
    return urlparse(url).netloc

print("2. Domain:", get_domain("https://www.python.org/docs/"))

# 3. Extract path
def get_path(url):
    return urlparse(url).path

print("3. Path:", get_path("https://example.com/shop/items"))

# 4. Parse query parameters
query = parse_qs("name=Aman&age=22&skill=python&skill=git")
print("4. Query:", query)

# 5. Get one parameter
def get_param(url, key):
    return parse_qs(urlparse(url).query).get(key, [None])[0]

print("5. ID:", get_param("https://example.com/product?id=101", "id"))

# 6. Build query string
params = {"name": "Aman", "course": "Python", "level": "beginner"}
query_string = urlencode(params)
print("6. Query:", query_string)

# 7. Build URL
built = urlunparse(("https", "example.com", "/search", "", query_string, ""))
print("7. URL:", built)

# 8. Join relative URL
base_url = "https://example.com/docs/"
print("8.", urljoin(base_url, "python.html"))

# 9. Remove tracking parameters
def clean_url(url):
    p = urlparse(url)
    params = parse_qs(p.query)
    allowed = {
        k: values[0] for k, values in params.items()
        if k not in {"utm_source", "utm_medium", "utm_campaign"}
    }
    return urlunparse((p.scheme, p.netloc, p.path, p.params,
                       urlencode(allowed), p.fragment))

tracking = "https://example.com/page?id=5&utm_source=google&utm_medium=cpc"
print("9. Clean:", clean_url(tracking))

# 10. Validate web URL
def is_web_url(url):
    p = urlparse(url)
    return p.scheme in {"http", "https"} and bool(p.netloc)

print("10.", is_web_url("https://example.com"))
print("    ", is_web_url("hello world"))

# 11. Complete URL analyzer
def analyze_url(url):
    p = urlparse(url)
    return {
        "scheme": p.scheme,
        "domain": p.netloc,
        "path": p.path,
        "query": parse_qs(p.query),
        "fragment": p.fragment,
        "is_web_url": is_web_url(url),
    }

sample = "https://example.com/search?q=python&page=2#results"
print("11. Analyzer:")
for key, value in analyze_url(sample).items():
    print(f"   {key}: {value}")
