import sys
from stats import get_num_words
from stats import get_num_of_chars_appearance
from stats import sort_dict_by_values

# print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
    return contents


def main():
    result = get_book_text(sys.argv[1])

    occurences = get_num_of_chars_appearance(result)

    word_count = get_num_words(result)

    characater_count = sort_dict_by_values(occurences)

    output_1 = f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
{word_count}
--------- Character Count -------"""

    print(output_1)

    for i in range(0, len(characater_count)):
        if characater_count[i]["letter"].isalpha():
            print(f"{characater_count[i]['letter']}: {
                  characater_count[i]['count']}")


main()
