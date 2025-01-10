def main():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        #print(file_contents)

    def count(file_contents):

        words = file_contents.split()  

        a = len(words)  

        print(a)
        #return a
    

main()