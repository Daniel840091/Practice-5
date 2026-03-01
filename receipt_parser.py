import re
import json

# Read file
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Extract prices (example: 1250.50 or 1250)
prices = re.findall(r"\d+\.\d+|\d+", text)

# Convert to float and calculate total
prices_float = [float(p) for p in prices]
total = sum(prices_float)

# Extract product names (line before price)
products = re.findall(r"([A-Za-zА-Яа-я\s]+)\s+\d+\.\d+|\d+", text)

# Extract date (example: 12/03/2025 or 2025-03-12)
date = re.search(r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}", text)
date = date.group() if date else "Not found"

# Extract time (example: 14:35)
time = re.search(r"\d{2}:\d{2}", text)
time = time.group() if time else "Not found"

# Extract payment method (CASH / CARD)
payment = re.search(r"CASH|CARD|Cash|Card", text)
payment = payment.group() if payment else "Not found"

# Structured output
data = {
    "products": products,
    "prices": prices_float,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment
}

print(json.dumps(data, indent=4, ensure_ascii=False))