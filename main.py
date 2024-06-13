def main():
    book_path = "/home/ruairi/workspace/github.com/ruairi212/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = count_characters(text)
    print(char_dict)
    char_sorted = sort_to_list(char_dict)
    print(f"---Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    for item in char_sorted:
        if  item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"End report of {book_path}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    string_lower = text.lower()
    dic = dict()
    for i in string_lower:
        if i in dic.keys():
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    return(dic)



def sort_to_list(num_each):
    list = []
    for ch in num_each:
        list.append({"char": ch,"num": num_each[ch]})
    sorted_list = sorted(list, key=lambda ch : ch['num'])
    return sorted_list

main()