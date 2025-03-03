def get_book_text():
    path_to_file = "books/frankenstein.txt"
    file_content = ""
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content
    
def main():
    book = get_book_text()
    print(book)
    
main()