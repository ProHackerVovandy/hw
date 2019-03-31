import random

Otvet = ['Мой магический шар говорит: ','Духи шепчут мне ответ на твой вопрос. Но я не могу его расслышать, положи еще 1000руб в шляпу на лечение слуха. Спасибо. О, о, кажется что-то расслышала. Они сказали: ','Карты глаголят: ']

def read_book(filename):
    text = ''
    with open(filename, encoding='utf-8') as book:
        text = book.readlines()
    with open(filename, encoding='utf-8') as book:
        lines = book.read()
    text = lines.splitlines()
    return text


def listen_question():
    question = ''
    print('Задай свой вопрос путник...')
    while True:
        question = input()
        if(question[len(question)-1] != '?'):
            print('Извини, я что-то не расслышала твой вопрос, повтори...')
        else:
            print('Хммм... Дайка спросить у духов!')
            return question


def answer(text, question):
    if(len(question.split()) <= len(text)):
        letter = text[len(question.split())-1].split()
        for i in letter:
            if(len(i) >= 2):
                answer = i
                break
    else:
        answer = 'начало'        
    return answer


def print_answer(answer):
    """Печатает ответ, обрамляя его красивой фразой
    
    Эта функция ничего не возвращает
    """
    print(Otvet[random.randint(0, 2)],'"',answer,'"')

def main():
    text = read_book('book.txt')
    question = listen_question()
    ans = answer(text, question)
    print_answer(ans)


if __name__ == '__main__':
    main()
