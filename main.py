import sys
from stats import get_num_words, count_characters, get_book_text, sort_dictionary

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = get_book_text(filepath)

    num_words = get_num_words(text)
    word_count = count_characters(text)
    
    sorted_list = sort_dictionary(word_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["character"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()

   