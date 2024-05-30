import sys
import requests

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QListWidgetItem, QListWidget, QLineEdit, QLabel, QTextEdit
from lab2_ui import Ui_Form

class LabaTwo(QWidget):
    def __init__(self):
        request_string = "https://belarusbank.by/api/kursExchange"
        response = requests.get(request_string)
        super(LabaTwo, self).__init__()
        self.response_json = response.json()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn_click)
        self.ui.listWidget.itemClicked.connect(self.item_click)

    def btn_click(self):
        if self.ui.listWidget.count() > 0:
            self.ui.listWidget.clear()
        for el in self.response_json:
            if self.ui.lineEdit.text() == el["name"]:
                self.ui.listWidget.addItem(QListWidgetItem(el["filials_text"]))

    def item_click(self, item):
        for el in self.response_json:
            if item.text() == el["filials_text"]:
                self.ui.labelAdr.setText(f"<b>Адрес:</b> {el['street_type']} {el['street']}, {el['home_number']}")
                self.ui.labelAdr.adjustSize()
                time_list = []
                for time in el['info_worktime'].split("|")[:-1]:
                    if time[-5].isdigit():
                        if len(time) > 18:
                            time_list.append(
                                f"{time[:2]}: {time[3:5]}:{time[6:8]} - {time[9:11]}:{time[12:14]} (пер. {time[15:17]}:{time[18:20]} - {time[21:23]}:{time[24:26]})")
                        else:
                            time_list.append(f"{time[:2]}: {time[3:5]}:{time[6:8]} - {time[9:11]}:{time[12:14]}")

                time_list = "<br/>".join(time_list)
                self.ui.labelTW.setText(f"<b>Время работы</b><br/>{time_list}")
                self.ui.labelTW.adjustSize()

                self.ui.textEdit.clear()
                self.ui.textEdit.setReadOnly(True)
                currency_list = ["USD", "EUR", "RUB", "GBP", "CAD", "PLN", "SEK", "CHF", "JPY", "CNY", "CZK", "NOK"]
                for currency in currency_list:
                    self.ui.textEdit.append(
                        f"<b>{currency}</b><br/>Покупка: {el[f'{currency}_in']}<br/>Продажа: {el[f'{currency}_out']}<br/><br/>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabaTwo()
    window.show()

    sys.exit(app.exec())