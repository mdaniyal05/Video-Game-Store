from datetime import datetime
from data import get_word, get_tip, get_news


def generate_learning():
    word, meaning = get_word()
    tip = get_tip()
    news = get_news()

    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""
Date: {today}

Word of the Day:
{word} - {meaning}

Programming Tip:
{tip}

News:
{news}

------------------------
"""
    return content


def save_to_file(content):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(content)


def main():
    content = generate_learning()
    print(content)
    save_to_file(content)


if __name__ == "__main__":
    main()
