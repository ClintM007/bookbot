def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_tally = {}
    for character in text.lower():
        if character in character_tally:
            character_tally[character] += 1
        else:
            character_tally[character] = 1
    return character_tally

def sort_on(item):
    key, value = item
    return value

