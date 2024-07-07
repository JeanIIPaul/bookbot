import collections

def main():
    path = 'books/frankenstein.txt'

    print(f'--- Begin report of {path} ---')
    book = read_book(path)
    print(f'{word_count(book)} words found in the document')
    print()
    print()

    merge_book = remove_whitespace(book.lower())
    my_dict = count_frequency(merge_book)

    # sort dictionary in a descending order
    sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    for key, value in sorted_dict:
        if key.isalpha():
            print(f'The \'{key}\' character was found {value} times')
    print('--- End report ---')

def word_count(book):
    return len(book.split())

def read_book(path):
    with open(path) as f:
        return f.read()

def remove_whitespace(book):
    new_book = book.replace(" ", "")
    return new_book

def count_frequency(book):
    return collections.Counter(book)

main()