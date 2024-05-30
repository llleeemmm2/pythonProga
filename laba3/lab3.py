import sys

from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel

from database import Ui_Form
from editWindow import Ui_Dialog

class LabaThree(QWidget):
    def __init__(self):
        super(LabaThree, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = QSqlDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.mainModel = QSqlQueryModel()
        query_string = """SELECT
                    f.id,
                    f.title AS [Название],
                    g.title AS [Жанр],
                    f.year AS [Год выпуска],
                    f.duration AS [Длительность]
                FROM films f 
                JOIN genres g on f.genre = g.id;"""
        self.mainModel.setQuery(query_string, self.db)

        self.ui.tableView.setModel(self.mainModel)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.doubleClicked.connect(self.doubleClick)

    def doubleClick(self, table):
        dialog = QDialog(self)
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        result = dialog.exec()

        if result == QDialog.Accepted:
            title = dialog_ui.titleEdit.text()
            year = dialog_ui.yearEdit.text()
            duration = dialog_ui.durationEdit.text()

            errors = {
                "Ошибка в названии фильма/сериала": not title,
                "Ошибка в годе фильма/сериала": not year.isdigit(),
                "Ошибка в длительности фильма/сериала": not duration.isdigit(),
            }

            for error_message, condition in errors.items():
                if condition:
                    print(error_message)
                    return

            genre = dialog_ui.genreBox.currentText()

            update_query = f"""UPDATE films
                        SET title = '{title}',
                        year = {int(year)},
                        genre = (SELECT id FROM genres WHERE title = '{genre}'),
                        duration = {int(duration)}
                    WHERE id = {int(table.sibling(table.row(), 0).data())};"""

            query = QSqlQuery(self.db)
            if query.exec_(update_query):
                query_string = """SELECT
                            f.id,
                            f.title AS [Название],
                            g.title AS [Жанр],
                            f.year AS [Год выпуска],
                            f.duration AS [Длительность]
                        FROM films f 
                        JOIN genres g on f.genre = g.id;"""
                self.mainModel.setQuery(query_string, self.db)
            else:
                print(query.lastError().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabaThree()
    window.show()

    sys.exit(app.exec())    # возможность закрыть окно приложения