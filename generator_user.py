from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES, ANIMALS, COLORS, COUNTRIES, LANGUAGES, NAMES, STAR_WARS
from random import randint, choice

class User:
    def __init__(self):
        self._name = get_random_name(combo=[ADJECTIVES, NAMES], separator="_")
        self._group = f'М23-ИВТ-{randint(1, 4)}'

    def set_name(self, name):
        self._name = name

    def set_group(self, group):
        self._group = group

    def name(self):
        return self._name

    def group(self):
        return self._group

    def __repr__(self):
        return f'[name: {self._name},  group: {self._group}]'

class Teacher:
    def __init__(self):
        self._name = get_random_name(combo=[ADJECTIVES, NAMES], separator="_")
        self._status = choice(['доцент', 'доктор'])
        self._education = f'{randint(1, 100)}_Подробное описание образования'

    def set_name(self, name):
        self._name = name

    def set_status(self, status):
        self._status = status

    def set_education(self, education):
        self._education = education

    def name(self):
        return self._name

    def status(self):
        return self._status

    def education(self):
        return self._education

    def __repr__(self):
        return f'[name: {self._name},  status: {self._status}, education: {self._education}]'


class Subject:
    def __init__(self):
        self._title = get_random_name(combo=[ANIMALS], separator="-")
        self._description = f'{randint(1, 100)}_Подробное описание знаний, умений и навыков'

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def title(self):
        return self._title

    def description(self):
        return self._description

    def __repr__(self):
        return f'[title: {self._title},  description: {self._description}]'

class Section:
    def __init__(self):
        self._title = f'section {get_random_name(combo=[STAR_WARS])}'

    def set_title(self, title):
        self._title = title

    def title(self):
        return self._title

    def __repr__(self):
        return f'[title: {self._title}]'

class Subsection:
    def __init__(self):
        self._title = f'subsection {get_random_name(combo=[STAR_WARS])}'

    def set_title(self, title):
        self._title = title

    def title(self):
        return self._title

    def __repr__(self):
        return f'[title: {self._title}]'

class Step:
    def __init__(self):
        self._title = f'step {get_random_name(combo=[STAR_WARS])}'
        self._text = f'Теория или описание задания'
        self._answers = []

    def set_title(self, title):
        self._title = title

    def set_text(self, text):
        self._text = text

    def set_answers(self, answers):
        self._answers = answers

    def title(self):
        return self._title

    def text(self):
        return self._text

    def answers(self):
        return self._answers

    def __repr__(self):
        return f'[title: {self._title}, text: {self._text}, answers: {self._answers}]'


for _ in range(5):
    print(Step())