def main():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        #print(file_contents)

    def count_words(file_contents):

        words = file_contents.split()  

        a = len(words)  

        print(a)
        #return a

    def count_characters(file_contents):

        lowered = file_contents.lower()

        letters = {}

        for letter in lowered:
    
            if letter in letters:

                letters[letter] = (letters[letter] + 1)

            else:

                letters[letter] = 1

        print(letters)

    
    #count_words(file_contents)

    count_characters(file_contents)

main()