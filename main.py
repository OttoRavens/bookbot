import sys
from stats import count_characters, sort_character_counts

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    character_counts = count_characters(book_text)
    sorted_counts = sort_character_counts(character_counts)

    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
