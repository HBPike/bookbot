def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin book report of {book_path} ---")
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)
        word_count(file_contents)
        print ("")
        character_count(file_contents)
    print("--- End report ---")


def character_count(input_string):
    character_dictionary = {}
    check_string = input_string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for character in check_string:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    for each in alphabet:
        print(f"The '{each}' character was found {character_dictionary[each]} times")
        

def word_count(input_string):
    words_to_count = input_string.split()
    number_of_words = len(words_to_count)
    print(number_of_words, "words found in the document")
    return number_of_words


main()