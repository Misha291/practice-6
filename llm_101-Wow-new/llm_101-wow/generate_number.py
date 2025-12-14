import random
import sys
import csv

def get_topic_by_id(record_id, csv_file='topics.csv'):
    """Возвращает тему по id из CSV."""
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['id']) == record_id:
                return row['topic']
    return None

def prepend_to_readme(number, topic, filename='README.md'):
    """Добавляет число и тему в начало README.md."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = ""
    header = f"Ваше уникальное случайное число - {number}\nТема: {topic}\n\n"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header + content)

if __name__ == "__main__":
    min_val = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    max_val = int(sys.argv[2]) if len(sys.argv) > 2 else 101

    random_number = random.randint(min_val, max_val)
    topic = get_topic_by_id(random_number, 'topics.csv') or 'Тема не найдена'

    prepend_to_readme(random_number, topic)
    print(f"✅ Сгенерировано число: {random_number}, Тема: {topic}")
