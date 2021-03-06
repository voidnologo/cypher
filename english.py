from dictionaries import system_dictionary

ENGLISH_WORDS = system_dictionary()


def is_english_word(word):
    return word.upper() in ENGLISH_WORDS


def probably_english(message, required_percentage=40):
    word_list = message.split()
    match = 0
    for word in word_list:
        if is_english_word(word.strip()):
            match += 1
    match_percent = float(match) / len(word_list)
    return match_percent * 100 >= required_percentage
