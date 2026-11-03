import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("all_gemini_responses_clean.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

parts = text.split("#################### RESPUESTA ")
# Let's inspect responses 14, 15, 16, 17, 18, 19
for num in [14, 15, 16, 17, 18]:
    if num < len(parts):
        print(f"************************************************************")
        print(f"                     RESPUESTA {num}                        ")
        print(f"************************************************************")
        print(parts[num][:3000])
