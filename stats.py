def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_char(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] +=1
    return char_dict

def sort_char(dict):
    char_list = []
    for char, value in dict.items():
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = value
        char_list.append(temp_dict)
    def sorted_on(dict):
        return dict["num"]
    char_list.sort(reverse= True, key=sorted_on)
    return char_list




