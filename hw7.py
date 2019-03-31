def words_filter(words, startswith='', min_length =-1, endswith='', contains=''):
    '''Фильтрует слова в соответствии с фильтрами

    words: list
    	Список слов
    startswith: str
    	Строка, с которой должно начинаться слово
    endswith: str
    	Строка, на которую должно заканчиваться слово
    min_length: int
    	Минимальная длина слова
    contains:
    	Строка, которую обязательно должна быть в слове

    Функция возвращает список отфильтрованных слов
    '''
    if min_length != -1:
        return 0, 'Я не умею работать с min_length :( ', []
    elif endswith != '':
        return 0, 'Я не умею работать с endswith :( ', []
    
    answer = []
    if contains != '' and startswith == '':
        for i in words:
            if i.find(contains) >= 0:
                answer.append(i)
        return 1, '', answer

    elif contains == '' and startswith != '':
        for i in words:
            if i[0:(len(startswith))] == startswith:
                answer.append(i)
        return 1, '', answer

    elif contains != '' and startswith != '':
        for i in words:
            if i[0:(len(startswith))] == startswith and i.find(contains) >= 0:
                answer.append(i)
        return 1, '', answer

def main():
    words = ['маша','машина','михандрий','крутой','маленькая','девочка','чьорт']
    print(words_filter(words, contains='а', startswith='м'))
    print(words_filter(words, contains='а', endswith='ма'))
if __name__ == "__main__":
    main()