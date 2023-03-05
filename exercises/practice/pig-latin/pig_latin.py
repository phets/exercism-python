import re

RE = re.compile('^(x+(?!r)|y+(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')

def translate(text: str) -> str:
    return ' '.join(map(translate_word, text.split(' ')))


def translate_word(word: str) -> str:
    return RE.sub(lambda m: '{1}{0}ay'.format(*m.groups()), word)

