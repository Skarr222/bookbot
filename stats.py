from curses.ascii import isalpha


def get_book_length(book):
    book_splited = book.split()
    num_of_words = len(book_splited)
    return num_of_words

def get_count_of_characters (book):
    book_dictonary = {}
    book_splited = book.split()
    for word in book_splited:
        lower_case_word = word.lower()
        for char in lower_case_word:
            if char in book_dictonary:
                book_dictonary[char] +=1
            else:
                book_dictonary[char] = 1
        
    return book_dictonary    

def sort_dictionary(char_dic):
    sorted_dictionary = {}
    sorted_list = sorted(
        [{"character": char, "count": count} for char, count in char_dic.items() if char.isalpha()],
        key=lambda x: x["count"],
        reverse=True
    )
    return sorted_list