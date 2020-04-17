from collections import namedtuple

from bs4 import BeautifulSoup

from src.common.errors import ParsingError

base_lesson = namedtuple('Base', ['date', 'verb', 'lessons'])
lesson = namedtuple('Lesson', ['number', 'start', 'stop', 'description'])


def serialize(data):
    return [
        {
            'date': base.date, 'verbose': base.verb, 'lessons': [
                {
                    'number': single.number, 'from': single.start,
                    'to': single.stop, 'description': single.description
                }
                for single in base.lessons
            ]
        }
        for base in data
    ]


def collect(containers):
    result = []
    for container in containers:
        lessons = []
        date = container.h4.text.split()
        for each_tr in container.find_all('tr'):
            row = each_tr.find_all('td')
            if row[-1].get_text(strip=True):
                description = row[2].text.replace('\xa0', ' ')
                lesson_time = row[1].text[:5], row[1].text[5:]
                lessons.append(lesson(row[0].text, *lesson_time, description))
        result.append(base_lesson(*date, lessons))
    return serialize(result)


def parse(content):
    try:
        soup = BeautifulSoup(content, 'lxml').find_all('div', class_='container')
        containers = soup[1].find_all('div', class_='col-md-6')
        if not containers:
            return []
        return collect(containers)
    except LookupError:
        raise ParsingError("Schedule parsing error. Try to fix the X-Schedule-Url header.") from None
