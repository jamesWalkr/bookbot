def get_num_words(book_text):
    num_of_words = book_text.split()

    return f"Found {len(num_of_words)} total words"


def get_num_of_chars_appearance(book_text):
    result_dict = {}
    for letter in book_text.lower():
        if letter in result_dict:
            result_dict[letter] = result_dict[letter] + 1
        else:
            result_dict[letter] = 1

    return result_dict


def sort_dict_by_values(result_dict):
    list_of_dicts = []

    def sort_on(dict):
        return dict["count"]

    for i in result_dict:
        new_dict = {"letter": i, "count": result_dict[i]}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
