from stats import get_book_length, get_count_of_characters
def get_book_text():
    path_to_file = "books/frankenstein.txt"
    file_content = ""
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content
    

def main():
    try:
        book = get_book_text()
        book_length = get_book_length(book)
        character_dictionary = get_count_of_characters(book)
        print(f"{book_length} words found in the document")
        print(character_dictionary)
        
    except Exception as error:
        print(error)
    
    
main()