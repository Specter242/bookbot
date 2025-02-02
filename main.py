def main():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        #print(file_contents)

    def count_words(file_contents):

        words = file_contents.split()  

        a = len(words)  

        #print(a)
        return a

    def count_characters(file_contents):

        lowered = file_contents.lower()

        letters = {}

        for letter in lowered:
    
            if letter in letters:

                letters[letter] = (letters[letter] + 1)

            else:

                letters[letter] = 1

        #print(letters)
        return letters

    def sort(letters):
        
        sorted_letters = {}

        sorted_letters = {key: letters[key] for key in sorted(letters)}
        
        return sorted_letters
        #print(sorted_letters)

    def report(count_words, sorted_letters):

        print("--- Begin report of books/frankenstein.txt ---")

        print(f"{count_words} words found in the document")

        print()

        for letter in sorted_letters:

            if letter.isalpha():

                print(f"The {letter} character was found {sorted_letters[letter]} times")

        print("--- End report ---")

        

    #count_words(file_contents)
    
    counted_words = count_words(file_contents)

    letters = count_characters(file_contents)

    sorted_letters = sort(letters)

    report(counted_words, sorted_letters)

main()