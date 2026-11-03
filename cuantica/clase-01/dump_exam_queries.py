import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open("rendered_gemini_edge.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Find the queries around "Dijo que lo último"
queries = soup.find_all(class_=lambda x: x and 'query-text' in x)

for i, q in enumerate(queries):
    txt = q.get_text(separator=' ', strip=True)
    if any(k in txt for k in ['Dijo que lo', 'diagonal', 'bases más menos', 'Solo te comento']):
        print(f"==================== QUERY {i} ====================")
        print(txt)
        # Find next sibling or parent's next elements containing model response
        # In Gemini web, let's look at the corresponding markdown response
