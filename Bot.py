import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import codecs
from TextProcess import text_processing

goodProbability = 0.4


def teach(lang):
    # для пример и правила нужен анализ биграмм??
    # или словарь лексем - терминов??
    lang.make_questions_answers()
    lang.make_dataset()
    x = []
    y = []
    for i in lang.questions_answers:
        x.append(i[0])
        y.append(i[1])
    for i in lang.dataset:
        x.append(i)
        y.append(list(lang.dataset[i])[0][1])
    lang.vectorizer_t = TfidfVectorizer()
    x_vect = lang.vectorizer_t.fit_transform(x)
    lang.clf_t = RandomForestClassifier(n_estimators=300).fit(x_vect, y)


def get_fail_phrase():
    phrases = ['Ничего не найдено. Попробуйте переформулировать вопрос', 'Ничего нет. Задайте вопрос по-другому']
    return random.choice(phrases)


def generate_answer(txt, lang):
    txt_vec = lang.vectorizer_t.transform([txt])
    rez = lang.clf_t.predict(txt_vec)[0]
    index = list(lang.clf_t.classes_).index(rez)
    probability = lang.clf_t.predict_proba(txt_vec)[0][index]
    if probability > goodProbability:
        return rez


def bot_answer(question, lang):
    answer = generate_answer(question, lang)
    if answer:
        return answer
    answer = get_fail_phrase()
    return answer


def bot_answer_utf8(question, lang):
    answer_for_user = bot_answer(text_processing(question, lang), lang)
    return codecs.escape_decode(answer_for_user)[0].decode('utf-8')
