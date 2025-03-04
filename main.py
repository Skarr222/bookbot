from stats import get_book_length
def get_book_text():
    path_to_file = "books/frankenstein.txt"
    file_content = ""
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content
    

def main():
    book = get_book_text()
    
    num_of_words = get_book_length(book)
    print(f"{num_of_words} words found in the document")
    
    
main()