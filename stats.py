def get_number_of_words(text): 
    word_list = text.split()
    return len(word_list)

def get_stats_of_text(text): 
    characters = list(text.lower())
    new_dict = {}
    for char in characters: 
        if char in new_dict: 
            new_dict[char] += 1
        else: 
            new_dict[char] = 1
    return new_dict
    
def sort_on(items): 
    return items["num"]

def get_sorted_list(stats): 
    new_list = []
    for entry in stats:
        new_list.append({"name": entry, "num": stats[entry]}) 
    new_list.sort(reverse=True, key=sort_on)
    return new_list
