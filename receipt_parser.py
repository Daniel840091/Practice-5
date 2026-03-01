import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract product names

products = re.findall(r"\d+\.\s*\n(.+)", text)


# 2. Extract item prices (строки после x)

prices_raw = re.findall(r"x\s*([\d\s]+,\d{2})", text)


prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices_raw]


# 3. Calculate total

calculated_total = sum(prices)


# 4. Extract TOTAL from receipt

total_match = re.search(r"ИТОГО:\s*\n?([\d\s]+,\d{2})", text)
receipt_total = total_match.group(1).replace(" ", "").replace(",", ".") if total_match else "Not found"


# 5. Extract payment method

payment = re.search(r"Банковская карта|Наличные", text)
payment_method = payment.group() if payment else "Not found"


# 6. Extract date and time

datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", text)
datetime_value = datetime_match.group() if datetime_match else "Not found"


# 7. Structured Output

data = {
    "products": products,
    "prices": prices,
    "calculated_total": calculated_total,
    "receipt_total": receipt_total,
    "payment_method": payment_method,
    "datetime": datetime_value
}

print(json.dumps(data, indent=4, ensure_ascii=False))