

def open_file_separate_by_line(filename):
    list_of_words = []

    with open(filename) as open_file:
        for line in open_file:
            line = line.rstrip()

            list_of_words += line.split(" ")

    return list_of_words

def add_to_dictionary(filename):
    list_of_words = open_file_separate_by_line(filename)

    word_count_dict = {}

    for word in list_of_words:
        if word in word_count_dict:
           word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    # for key, value in word_count_dict.iteritems():
    #     print key, value

    for key in word_count_dict:
        print key, word_count_dict[key]

add_to_dictionary("twain.txt")
