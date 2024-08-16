def main():
    # get book contents
    book_path = "books/frankenstein.txt"
    book_contents = get_book(book_path)

    # get report contents
    word_count = get_word_count(book_contents)
    character_dict = get_char_count(book_contents)
    character_sorted_list = get_sorted_char_dict_list(character_dict)

    # begin report
    print(f"Begin report of {book_path}")
    print(f"{word_count} words found")
    print()
    
    # print only alphabet characters and their counts
    for c in character_sorted_list:
        if c['char'].isalpha():
            print(f"The '{c['char']}' character appears {c['num']} times")
    
    # end report
    print()
    print("End of report")


def sort_on(d):
    # Sort key for get_sorted_char_dict_list
    return d["num"]

def get_sorted_char_dict_list(char_dict):
    # Returns sorted list of dictonaries showing counts of each unique letter from most to least. e.g. [{'char':'a', 'num':10}]
    sorted_list = []
    for c in char_dict:
        sorted_list.append({'char':c,'num':char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book(path):
    # Returns all text contained in file located at 'path'
    with open(path) as f:
        return f.read()

def get_word_count(book):
    # Returns count of words in 'book' separated by whitespace
    words = book.split()
    return len(words)
    
def get_char_count(book):
    # Returns dictionary of all unique characters in 'book' and how many times they appeared
    lowercase_text = book.lower()
    characters = {}
    for c in lowercase_text:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

main()