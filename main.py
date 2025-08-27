import sys



from stats import get_num_words
from stats import get_num_char
from stats import sort_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv)< 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    num_words= get_num_words(get_book_text(path_to_book))
    sorted_list= sort_char(get_num_char(get_book_text(path_to_book)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}..")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            char = dict["char"]
            value = dict["num"]
            print(f"{char}: {value}")
    print("============= END ===============")


main()
