# question - Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops

s = input("Input String: ")
letters = 0
digits = 0
special_symbols = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special_symbols += 1
print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of special symbols:", special_symbols)



# question -  Counting Letters, Digits, and Special Symbols in a String Using List Comprehension

s = input("Input String: ")
letters = [ch for ch in s if ch.isalpha()]
digits = [ch for ch in s if ch.isdigit()]
special_symbols = [ch for ch in s if not ch.isalnum()]
print("Number of letters:", len(letters))
print("Number of digits:", len(digits))
print("Number of special symbols:", len(special_symbols))



# question - To Use Regex To Search Digits

import re
s = input("Enter a string: ")
digits = re.findall(r'\d', s)
if digits:
    print("Digits found in the string:", digits)
else:
    print("No digits found in the string.")



# To Check Email Address

import re
def check_password(password):
    pattern = r'^[A-Za-z][A-Za-z0-9@#$%^&*]{7,}$'
    if (re.match(pattern, password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[@#$%^&*]', password)):
        return True
    return False
password = input("Enter your password: ")
if check_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")



# News Data Processing

import re
news_paragraph = "Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi. Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X. These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code, he posted on X, in a clear indication that govt intends to initiate action. Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed experts, as per the X post."
def check_modi(news):
    return "Modi" in news
def count_words(news):
    return len(news.split())
def count_the(news):
    return len(re.findall(r'\bthe\b', news, re.IGNORECASE))
def check_digits(news):
    return any(ch.isdigit() for ch in news)
def remove_articles(news):
    words = news.split()
    words = [word for word in words if word.lower() not in ["a", "an", "the"]]
    return " ".join(words)
def remove_vowels(news):
    return "".join([ch for ch in news if ch.lower() not in "aeiou"])
print("Presence of 'Modi':", check_modi(news_paragraph))
print("Number of words:", count_words(news_paragraph))
print("Number of occurrences of 'the':", count_the(news_paragraph))
print("Presence of digits:", check_digits(news_paragraph))
compact_news = remove_articles(news_paragraph)
print("Compact news data without articles:", compact_news)
vowel_free_news = remove_vowels(compact_news)
print("Compact news data without vowels:", vowel_free_news)