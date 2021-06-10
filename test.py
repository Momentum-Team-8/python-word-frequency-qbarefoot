import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


with open ("praise_song_for_the_day.txt") as f:
    text = f.read().lower()
    words = text.split()
    print(words)

    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    print(stripped)

for element in STOP_WORDS:
        while element in text_no_punctuation:
            text_no_punctuation.remove(element)

    print(text_no_punctuation)