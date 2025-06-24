from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        report_maker(file_contents, path_to_file)


def report_maker(file_contents, path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    get_word_count(file_contents)
    print("--------- Character Count -------")
    sorted_list = get_character_count(file_contents)
    for dictionary in sorted_list:
        if str.isalpha(dictionary["char"]):
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) > 1:
        get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    main()
