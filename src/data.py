import random

WORDS = [
    ("Resilient", "Able to recover quickly from difficulties"),
    ("Meticulous", "Showing great attention to detail"),
    ("Pragmatic", "Dealing with things realistically"),
]

TIPS = [
    "Use list comprehensions for cleaner Python code.",
    "Break problems into small functions.",
    "Use virtual environments for projects.",
]

NEWS = [
    "AI is transforming software development.",
    "Cybersecurity demand is increasing globally.",
    "Open-source contributions are growing fast.",
]


def get_word():
    return random.choice(WORDS)


def get_tip():
    return random.choice(TIPS)


def get_news():
    return random.choice(NEWS)
