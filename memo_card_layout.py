''' Окно для карточки вопроса '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo_app import app 

# виджеты, которые надо будет разместить:
btn_Menu = QPushButton('Меню') # кнопка повернення в головне меню
btn_Sleep = QPushButton('Відпочити') # кнопка приховує вікно і повертає його після закінчення таймеру
box_Minutes = QSpinBox() # введення кількості хвилин відпочинку
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст питання

# Панель з варіантами відповіді:
RadioGroupBox = QGroupBox("Варіанти відповіді") # група на экрані для перемикачів з відповідями
RadioGroup = QButtonGroup() # а це для групування перемикачів, щоб керувати їх поведінкою

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Панель с результатом:
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') # тут поміщаємо напис "правильно" або "неправильно"
lb_Correct = QLabel('') # тут буде написаний текст правильної відповіді

#  Розміщення віджетів:

# Розміщуємо варіанти відповіді в два стовпці всередині групи:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальні будуть всередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді в перший стовпчик
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді в другий стовпчик
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку

RadioGroupBox.setLayout(layout_ans1) # готова "панель" з вариантами відповідей    
# розміщуємо результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# розміщуємо всі віджети у вікні, вони розташовуються в четырьох рядках (горизонтальних лініях):
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо подовше
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин')) # нам не обов'язково створювати змінну для цього напису

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка повинна бути велика, розтягуємо
layout_line4.addStretch(1)

# Тепер створені 4 рядки (горизонтальні лінії) розмістимо один під одним:
layout_card = QVBoxLayout() #ГОЛОВНА вертикальна лінія
layout_card.addLayout(layout_line1, stretch=1) # на неї додаємо всі інші
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробіли між вмістом

# Результат работы этого модуля: виджеты помещены внутрь layout_card, который можно назначить окну.

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    # зкинути вибрану радіо-кнопку
    RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було зкинути вибір радіокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # зняли обмеження, тепер тільки одна радіокнопка може бути вибрана
