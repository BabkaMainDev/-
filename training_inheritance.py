from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt

prilozhenie = QApplication([])
prilozhenie.setApplicationName('Кокурс Крейзи Пипл')

# Glavnoe okno
glavnoe_okno = QWidget()
glavnoe_okno.resize(475, 300)

# Оsnovnoya layout
main_layout = QVBoxLayout(glavnoe_okno)

# Vopros
vopros = QLabel('V kakom godu mi poluchili zolotaya knopka????')
main_layout.addWidget(vopros, alignment=Qt.AlignCenter)

# Otveti & dobavlenie widgetov
radio_group = QButtonGroup()  # Sosdaem group radiobutton

Knopka_1 = QRadioButton('988')
Knopka_2 = QRadioButton('1914')
Knopka_3 = QRadioButton('1933')
Knopka_4 = QRadioButton('1939')
Knopka_5 = QRadioButton('1991')
Knopka_6 = QRadioButton('2005')
Knopka_7 = QRadioButton('2011')
Knopka_8 = QRadioButton('2015')
radio_group.addButton(Knopka_1)
radio_group.addButton(Knopka_2)
radio_group.addButton(Knopka_3)
radio_group.addButton(Knopka_4)
radio_group.addButton(Knopka_5)
radio_group.addButton(Knopka_6)
radio_group.addButton(Knopka_7)
radio_group.addButton(Knopka_8)

# Roztashuvanya knopok
h_layout1 = QHBoxLayout()
h_layout1.addWidget(Knopka_1, alignment=Qt.AlignLeft)
h_layout1.addWidget(Knopka_2, alignment=Qt.AlignRight)

h_layout2 = QHBoxLayout()
h_layout2.addWidget(Knopka_3, alignment=Qt.AlignLeft)
h_layout2.addWidget(Knopka_4, alignment=Qt.AlignRight)

h_layout3 = QHBoxLayout()
h_layout3.addWidget(Knopka_5, alignment=Qt.AlignLeft)
h_layout3.addWidget(Knopka_6, alignment=Qt.AlignRight)

h_layout4 = QHBoxLayout()
h_layout4.addWidget(Knopka_7, alignment=Qt.AlignLeft)
h_layout4.addWidget(Knopka_8, alignment=Qt.AlignRight)

# Dobavlenie gorizontal roztashuvan do osnovnogo vertikal
main_layout.addLayout(h_layout1)
main_layout.addLayout(h_layout2)
main_layout.addLayout(h_layout3)
main_layout.addLayout(h_layout4)

def otveti_reaction():
    if Knopka_1.isChecked():
        vopros.setText('Ochen Daleko ot vernogo otveta, verniy 2015, ti nichego ne vigral')
    elif Knopka_2.isChecked():
        vopros.setText('Daleko ot vernogo otveta, verniy 2015, ti nichego ne vigral')
    elif Knopka_3.isChecked():
        vopros.setText('Dlizhe k vernogo otveta, verniy 2015, ti vigral knigu istorii')
    elif Knopka_4.isChecked():
        vopros.setText('God vtoroy mirovoy, verniy 2015, ti vigral luley ot deda')
    elif Knopka_5.isChecked():
        vopros.setText('God razvala CCCP, verniy 2015, ti vigral knigu istorii')
    elif Knopka_6.isChecked():
        vopros.setText('Blizko no ne verno, verniy otvet 2015, ti vigral karyinu')
    elif Knopka_7.isChecked():
        vopros.setText('Ochen blizko no ne verno, verniy otvet 2015, ti vigral karyinu')
    elif Knopka_8.isChecked():
        vopros.setText('Pravilno, ti vigral milion dolarov i 250000 ton trotila!')
    for button in radio_group.buttons():
        button.setEnabled(False)

Knopka_1.clicked.connect(otveti_reaction)
Knopka_2.clicked.connect(otveti_reaction)
Knopka_3.clicked.connect(otveti_reaction)
Knopka_4.clicked.connect(otveti_reaction)
Knopka_5.clicked.connect(otveti_reaction)
Knopka_6.clicked.connect(otveti_reaction)
Knopka_7.clicked.connect(otveti_reaction)
Knopka_8.clicked.connect(otveti_reaction)

glavnoe_okno.setLayout(main_layout)
glavnoe_okno.show()
prilozhenie.exec()











'''class Widget:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def print_info(self):
        print(f"Tекст: {self.text}")
        print(f"Розташування: ({self.x}, {self.y})")

class Button(Widget):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.is_clicked = False

    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")

# Створення екземпляра класу Button
button = Button("Реєтрація", 100, 100)

# Друк загальної інформації про кнопку
button.print_info()

# Запит у користувача
response = input("Хочете зареєструватися? (так / ні): ").strip().lower()

if response == "так":
    button.click()
elif response == "ні":
    print("А шкода!")
else:
    print("НАПИШИ ТАК АБО НІ!!!!!!!")'''
