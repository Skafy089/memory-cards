
#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,
 QVBoxLayout,
QGroupBox, QRadioButton, QPushButton, QHBoxLayout, QButtonGroup)
from random import shuffle, randint

class Question():
    #Вопрос, 3 непр, 1 прав ответ
    def __init__(self,question, right_answer, wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

question_list=[]
question_list.append(Question ('Какого цвета нет на флаге РФ','Черный', 'Красный', 'белый', 'Синий'))
question_list.append(Question('Какой страны нету?', 'Москва', 'Россия', 'CША','Турция'))
question_list.append(Question('Что не фрукт?', 'Арбуз', 'Яблоко', 'Киви', 'Груша'))
question_list.append(Question('Что не овощь?', 'Банан', 'Огурец', 'Помидор', 'Капуста'))
question_list.append(Question ('Какой буквы нет в Русском алфавите?', 'للُّغَ', 'в', 'й', 'ы'))
question_list.append(Question ('Какой буквы нет в Английском алфавите?', 'ъ', 'd', 'e', 'r'))
question_list.append(Question ('Какой цифры не существует?', '20', '1', '6', '9'))
question_list.append(Question ('Какой планеты не существует в солнечяной системе?', 'Росс 128 b', 'Земля', 'Солнце', 'Юпитер'))
question_list.append(Question ('Что не ягода?', 'Манго', 'Виноград', 'Арбуз', 'Смородина'))
question_list.append(Question ('Какое животное не относится к рыбам', 'Хммяк', 'Окунь', 'Лосось', 'Барбусы'))


app = QApplication([])


window = QWidget()
window.setWindowTitle('Memory Card')

#Interface
question1 = QLabel('Какой национальности не существует')
btn_ok = QPushButton('Ответить')

radioButtonBox = QGroupBox('Варианты ответа:')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымынцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox('Результаты')
lb_Result = QLabel ('Правильно ли или нет?')
lb_Correct = QLabel('Смурфы')

layout_res= QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)

layout_answer1 = QHBoxLayout()
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(rbtn_1)
layout_answer2.addWidget(rbtn_2)

layout_answer3.addWidget(rbtn_3)
layout_answer3.addWidget(rbtn_4)

layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)

radioButtonBox.setLayout(layout_answer1)


layout_line1 = QHBoxLayout() #Вопрос
layout_line2 = QHBoxLayout() #Варианты ответа
layout_line3 = QHBoxLayout() #Кнопка

layout_line1.addWidget(question1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(radioButtonBox)
layout_line1.addStretch(1)
layout_line3.addWidget(btn_ok , stretch=2)
layout_line1.addStretch(1)



loyout_card = QVBoxLayout() #Слой окна
loyout_card.addLayout(layout_line1, stretch=2) #Поменять на addLayout
loyout_card.addLayout(layout_line2, stretch=8)
loyout_card.addStretch(1)

loyout_card.addLayout(layout_line3, stretch=1)
loyout_card.addStretch(1)
loyout_card.setSpacing(5)

answer=[rbtn_2, rbtn_1,rbtn_3,rbtn_4] #Положили ответы в список

def show_answer():
    radioButtonBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)

def ask(question, right_answer, wrong1,wrong2,wrong3):
    answer[0].setText(right_answer)
    answer[1].setText(wrong1)
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    question.setText(question)
    lb_Correct.setText(right_answer)
    show_answer()

def ask(q : Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question1.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_answer()

    

def show_result(): #Показать ответы
    radioButtonBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        window.score+=1
        print('Статистика\nВсего вопросов:', window.total,'\nКоличество правельных:', window.score)
        print('Рейтинг:',window.score/window.total*100,'%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг:',window.score/window.total*100,'%')


def next_quastion(): #Фун-я отображает след вопрос
    window.total+=1
    print('\n\n--------Статистика\nВсего вопросов:', window.total,'\nКоличество правельных:', window.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_quastion()

btn_ok.clicked.connect(click_OK)
window.total =0
window.score =0
next_quastion()
window.setLayout(loyout_card)
window.show()
app.exec()