from memo_card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result
)
from PyQt5.QtWidgets import QWidget
from random import shuffle # Будемо перемішувати відповіді в картці питання

card_width, card_height = 600, 500 # Початкові розміри вікна " картка "
text_wrong = 'Неправильно'
text_correct = 'Правильно'

# В цій версії напишемо в коді одне питання і відповіді до нього 
 # Відповідні змінні як би поля майбутнього об'єкта " form " ( тобто анкета )
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'

# Тепер нам потрібно показати ці дані , 
 # Причому відповіді розподілити випадково між радіокнопку , і пам'ятати кнопку з правильною відповіддю . 
 # Для цього створимо набір посилань на радиокнопки і перемішаємо його
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]

def show_data():
    ''' показує на екрані потрібну інформацію '''
    # Об'єднаємо в функцію схожі дії
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    ''' перевірка , чи правильний відповідь обраний 
     якщо відповідь була обрана , то напис " вірно / невірно " набуває потрібне значення 
     і показується панель відповідей '''
    correct = answer.isChecked() # В цьому радіобаттоні лежить наша відповідь
    if correct:
        # Відповідь вірна , запишемо
        lb_Result.setText(text_correct) # Напис " вірно " або " невірно "
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            # Відповідь невірна, запишемо і відобразимо в статистиці
            lb_Result.setText(text_wrong)# Напис " вірно " або " невірно "
            show_result()

def click_OK(self):
    # Поки що перевіряємо питання , якщо ми в режимі питання , інакше нічого
    if btn_OK.text() != 'Наступний':
        check_result()

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(check_result)

win_card.show()
app.exec_()