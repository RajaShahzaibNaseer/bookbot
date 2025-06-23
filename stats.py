
#for getting word count
def get_word_count(file_contents):
    word_count = len(file_contents.split())
    print(f"{word_count} words found in the document")


#for getting character count
def get_character_count(content):
    character_counter = {}
    content_list = list(content.lower().split())
    for word in content_list:
        for char in word:
            if char in character_counter.keys():
                character_counter[char] += 1
            else:
                character_counter[char] = 1
    print(character_counter)


#for making sorted list
def sorted_list_maker(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"char" : key , "num" : dictionary[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


#for getting value to sort on
def sort_on(items):
    return items["num"]