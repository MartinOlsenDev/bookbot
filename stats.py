import functools as ft

def file_to_text(func):
    def wrapper(filepath):
        return func(get_book_text(filepath))
    return wrapper

@ft.lru_cache(maxsize=16)
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

@file_to_text
def word_counter(path):
    return len(path.split())

@file_to_text
def character_frequency(path):
    output = dict()
    for c in path.lower():
        output[c] = 1 + output.get(c, 0)
    return output

def to_list_of_dict(char_frequency):
    output_lst = [
        {"char": k, "num": v}
        for k,v in char_frequency.items()
    ]
    output_lst.sort(reverse=True, key=lambda x: x["num"])
    return output_lst
    
