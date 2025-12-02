import stats as s

TXT_FILEPATH = "./books/frankenstein.txt"
      
def main():
    num_words = s.word_counter(TXT_FILEPATH)
    print(f"Found {num_words} total words")
    frequency_dict = s.character_frequency(TXT_FILEPATH)
    print(frequency_dict)
    lst_d = s.to_list_of_dict(frequency_dict)
    for item in filter(lambda x: x["char"].isalpha(), lst_d):
        printable_char = item["char"]
        printable_freq = item["num"]
        print(f"{printable_char}: {printable_freq}")

if __name__ == "__main__":
    main()
