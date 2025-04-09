def get_book_text(filepath):
    with open(filepath) as f:  
        return f.read()

def get_num_words(text):
   words = text.split()
   return len(words)


def count_characters(text):
    # create empty dictionary to story counts
    char_counts = {}
       
    # convert it to lowercase
    lower_text = text.lower()
       
    # for each character in text
    for char in lower_text:
         # update the count in our dictionary
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            

   

    # return comlpeted dictionary
    return char_counts


def sort_dictionary(dictionary):
    new_list = []

    for key, value in dictionary.items():
        new_list.append({"character": key, "count": value})
    
    def sort_on(dict):
        return dict["count"]
    
    new_list.sort(reverse=True, key=sort_on)

    return new_list