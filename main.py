def count_words(s):
    wordcount = len(s.split())
    return wordcount

def count_each_character(s):
    s = s.lower()
    count = {}
    for c in s:
        if not c in count:
            count[c] = 0
        count[c] += 1
    return count


def main():
    bookpath = './books/frankenstein.txt' 
    print("--- Begin report of books/frankenstein.txt ---")
    with open(bookpath) as f:
        file_contents = f.read()
        count = count_words(file_contents)
        print(f"{count} words found in the document\n")
        charcount = count_each_character(file_contents)
        tuples = filter(lambda kv: kv[0].isalpha(), charcount.items())
        sortedalpha = (sorted(tuples, key=lambda kv: kv[1], reverse=True))
        for kv in sortedalpha:
            print(f"The '{kv[0]}' character was found {kv[1]} times")
    print("--- End report ---")


main()
