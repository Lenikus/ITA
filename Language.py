from TextProcess import text_processing, normalize_list, normalize_item
from List import is_list_in_list, list_replace
from LoadData import load_questions_answers, load_synonyms, load_stopwords, load_lexems


class Language(object):
    language_name = ''
    stopwords = []
    synonyms = []
    lexems = []
    questions_answers = []
    dataset = {}
    vectorizer_t = 0
    clf_t = 0

    def __init__(self, language_name = 'cpp'):
        self.language_name = language_name
        self.stopwords = load_stopwords(self.language_name)
        self.make_lexems()
        self.make_synonyms()

    def make_lexems(self):
        self.lexems = load_lexems(self.language_name)
        self.lexems = normalize_list(self.lexems)


    def make_synonyms(self): #normaleze pairs q-a
        self.synonyms = load_synonyms(self.language_name)
        # synonym_normalize
        for pair in self.synonyms:
            pair = normalize_list(pair)

    def make_pairs_with_synonyms(self):
        for pair in self.questions_answers:
            q = ' ' + pair[0] + ' '
            a = pair[1]
            flag = True
            for cur_syn_list in self.synonyms:
                for syn in cur_syn_list:
                    syn_in_q = q.find(syn)
                    if syn_in_q != -1 and q[syn_in_q - 1] == ' ' and q[syn_in_q + len(syn)] == ' ':
                        for i in cur_syn_list:
                            if i != syn:
                                qcopy = q
                                qcopy = qcopy.replace(syn, i)
                                q_synonym_a_pair = [(qcopy.rstrip()).lstrip(), a]
                                if q_synonym_a_pair not in self.questions_answers:
                                    self.questions_answers.append(q_synonym_a_pair)
                        break

    def make_questions_answers(self):
        self.questions_answers.clear()
        questions_answers = load_questions_answers(self.language_name)
        for pair in questions_answers:
            question, answer = pair
            question = text_processing(question, self)
            self.questions_answers.append([question, answer])
        self.make_pairs_with_synonyms()

    def make_dataset(self):
        for q, a in self.questions_answers:
            words = q.split(' ')
            for lexem in self.lexems:
                cur_lexem_list = lexem.split()
                pos = is_list_in_list(cur_lexem_list, words)
                if pos != -1:
                    list_replace(words, pos, cur_lexem_list, [lexem])
            for word in words:
                if word not in self.dataset:
                    self.dataset[word] = []
                self.dataset[word].append([q, a])

