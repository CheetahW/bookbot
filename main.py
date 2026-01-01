import sys
from stats import get_number_of_words, get_stats_of_text, get_sorted_list

def get_book_text(path_to_file): 
    with open(path_to_file) as f: 
        return f.read()

def main(): 
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_number_of_words(text)
    stats = get_stats_of_text(text)
    sorted_list = get_sorted_list(stats)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list: 
        if entry["name"].isalpha(): 
            print(f"{entry["name"]}: {entry["num"]}")
    print("============= END ===============")
main()