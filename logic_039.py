from datetime import date
import random

def to_uppercase(text):
    return text.upper()

def get_today_date():
    return date.today().isoformat()

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def get_random_number():
    return random.randint(1, 100)

def full_name():
    return "Emilia ikpa"
