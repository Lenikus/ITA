def save_my_dataset(user):
    filename = user.language + '/my_data_set.txt'
    f = open(filename, 'w')
    for pair in user.my_dataset:
        f.write(pair[0])
        f.write('\n')
        f.write(pair[1])
        f.write('\n\n')


def save_word_dataset(user):
    filename = user.language + '/word_dataset.txt'
    f = open(filename, 'w')
    for pair in user.word_dataset:
        f.write(pair)
        f.write('\n[\n')
        for i in user.word_dataset[pair]:
            for j in i:
                f.write(j)
                f.write('\n')
        f.write(']\n')


# def load_word_dataset(user):
#     filename = user.language + '/word_dataset.txt'
#     f = open(filename, 'r')
#     q = f.readline().rstrip()
#     user.word_dataset = []
#     while q:
#         if q not in user.word_dataset:
#             user.word_dataset[[q]] = []
#             a = f.read() #[
#             while a != ']':
#                 a = f.read()
#                 user.word_dataset[q].append([q, a])
#         q = f.read().rstrip()

