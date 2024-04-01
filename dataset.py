import pandas as pd
import random
import string
import datetime

def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

genuine_phrases = read_list_from_file('./sample data/genuine_phrases.txt')
spam_phrases = read_list_from_file('./sample data/spam_phrases.txt')
bad_words = read_list_from_file('./sample data/bad_words.txt')
suffixes = read_list_from_file('./sample data/suffixes.txt')
titles = read_list_from_file('./sample data/titles.txt')
names = read_list_from_file('./sample data/names.txt')

first_names = names[:10]
last_names = names[10:]

def generate_comment_id(length=16):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_author_name():
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_timestamp():
    start_date = datetime.datetime(2013, 11, 1)
    end_date = datetime.datetime(2013, 12, 31)
    time_diff = end_date - start_date
    random_days = random.randint(0, time_diff.days)
    random_seconds = random.randint(0, 86400)
    return (start_date + datetime.timedelta(days=random_days, seconds=random_seconds)).strftime('%Y-%m-%dT%H:%M:%S')

def generate_content(class_value):
    if class_value == 0:
        return random.choice(genuine_phrases) + ' ' + generate_random_suffix()
    else:
        spam_phrase = random.choice(spam_phrases)
        content = f"{spam_phrase}"
        if random.random() < 0.5:
            link = f'{generate_shortened_url()}'
            additional_text = random.choice(["Check it out now!", "Limited stock available!", "Offer expires soon!"])
            content += f" {link} {additional_text}"
        if random.random() < 0.3:
            content += f" {random.choice(bad_words)}"
        return content + ' ' + generate_random_suffix()


def generate_random_suffix():
    return random.choice(suffixes)

def generate_shortened_url():
    url_services = [
        "https://bit.ly/",
        "https://tinyurl.com/",
        "https://is.gd/"
    ]
    return random.choice(url_services) + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

def generate_youtube_title():
    return random.choice(titles)

def generate_class():
    return random.randint(0, 1)

def generate_dataset(num_samples):
    data = []
    for _ in range(num_samples):
        comment_id = generate_comment_id()
        author = generate_author_name()
        timestamp = generate_timestamp()
        youtube_title = generate_youtube_title()
        class_value = generate_class()
        content = generate_content(class_value)
        data.append([comment_id, author, timestamp, youtube_title, content, class_value])
    return pd.DataFrame(data, columns=['COMMENT_ID', 'AUTHOR', 'DATE', 'YOUTUBE_TITLE', 'CONTENT', 'CLASS'])

if __name__ == '__main__':
    num_samples = 1000
    dataset = generate_dataset(num_samples)
    dataset.to_csv('random.csv', index=False)
    print(f"Dataset generated with {num_samples} samples.")
