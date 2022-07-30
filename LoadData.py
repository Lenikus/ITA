def load_synonyms(language_name):
    filename = language_name + '/synonyms.txt'
    f = open(filename, 'r')
    synonyms = []
    first = f.readline()
    while first:
        cur_list = []
        cur_list.append(first.rstrip())
        cur_item = f.readline()
        while cur_item != '\n' and cur_item:
            cur_list.append(cur_item.rstrip())
            cur_item = f.readline()
        synonyms.append(cur_list)
        first = f.readline()
    f.close()
    return synonyms


def load_lexems(language_name):
    filename = language_name + '/lexems.txt'
    return load_list(filename)


def load_questions_answers(language_name):
    filename = language_name + '/questions_answers.txt'
    return load_pair(filename)


def load_stopwords(language_name):
    filename = language_name + '/stopwords.txt'
    return load_list(filename)


def load_pair(filename):
    f = open(filename, 'r')
    pairs = []
    first = f.readline()  # 1-я строка (всего одна)
    while first:
        second = ""
        cur_line = f.readline()  # 2-я и последующие строки до пустой строки
        while cur_line != '\n' and cur_line:
            second += cur_line
            cur_line = f.readline()
        pairs.append([first.rstrip(), second.rstrip()])
        first = f.readline()
    f.close()
    return pairs


def load_list(filename):
    f = open(filename, 'r')
    item = f.readline().rstrip()
    items = []
    while item:
        items.append(item)
        item = f.readline().rstrip()
    f.close()
    return items
