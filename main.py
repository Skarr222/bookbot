from stats import get_book_length, get_count_of_characters, sort_dictionary
import sys 

def get_book_text(path_to_book):
    file_content = ""
    with open(path_to_book) as f:
        file_content = f.read()
    return file_content
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)     
    try:
        path_to_file = sys.argv[1]
        print(path_to_file)
        book = get_book_text(path_to_file)
        book_length = get_book_length(book)
        character_dictionary = get_count_of_characters(book)
        sorted_dictionary = sort_dictionary(character_dictionary)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {book_length} total words")
        print("--------- Character Count -------")
        for dictionary  in sorted_dictionary:
            character = dictionary["character"]
            count = dictionary["count"]
            print(f"{character}: {count}")
        print("============= END ===============")
    except Exception as error:
        print(error)
    
if __name__ == "__main__":
    main()