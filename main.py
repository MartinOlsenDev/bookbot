import stats as s
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...""")

    num_words = s.word_counter(filepath)
    print(f"""----------- Word Count ----------
Found {num_words} total words""")

    frequency_dict = s.character_frequency(filepath)
    lst_d = s.to_list_of_dict(frequency_dict)
    print("--------- Character Count -------")
    for item in filter(lambda x: x["char"].isalpha(), lst_d):
        printable_char = item["char"]
        printable_freq = item["num"]
        print(f"{printable_char}: {printable_freq}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
