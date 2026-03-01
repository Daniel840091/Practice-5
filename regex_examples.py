import re

text = "My phone number is 87051234567 and my email is test@mail.com"

# re.search() – first match
match = re.search(r"\d+", text)
print("Search:", match.group())

# re.findall() – all matches
numbers = re.findall(r"\d+", text)
print("Findall:", numbers)

# re.split() – split string
words = re.split(r"\s", text)
print("Split:", words)

# re.sub() – replace
hidden = re.sub(r"\d", "*", text)
print("Sub:", hidden)

# re.match() – match at beginning
start = re.match(r"My", text)
print("Match:", start.group())