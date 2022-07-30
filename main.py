from Bot import teach, bot_answer_utf8
from Language import Language
# from TextProcess import make_default_stopwords
# from SaveUserData import save_my_dataset, save_word_dataset
# from TextProcess import text_processing

language_name = 'cpp'
lang = Language(language_name)
teach(lang)
# save_word_dataset(user)
while True:
   print("Введите вопрос или quit для завершения")
   question = input()
   if question == 'quit':
       break
   answer = bot_answer_utf8(question, lang)
   # answer = text_processing(question, lang)
   print(answer)
