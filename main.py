import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox

from untitled import form

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
path = str(current_directory).split('\\')
path[0] += '\\'
root_directory = os.path.dirname(path[0])


class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.directoryPath.setText(current_directory)
        self.directoryPath.textChanged.connect(self.handle_text_change)
        self.browse_folder(self.directoryPath.text())
        self.directoryPath.returnPressed.connect(lambda: self.browse_folder(self.directoryPath.text()))

        self.exitButton.clicked.connect(self.program_close)

        self.directoryTree.setHeaderLabels([f'Корневая папка \n{root_directory}'])
        self.directoryTree.itemDoubleClicked.connect(self.get_path_tree_widget_item)
        self.populate_tree_widget(root_directory, self.directoryTree.invisibleRootItem())

        self.directory.itemDoubleClicked.connect(self.open_directory)

        self.upButton.clicked.connect(lambda: self.up_directory(self.directoryPath.text()))

    def browse_folder(self, path):
        self.directory.clear()
        if os.path.exists(path):
            items = os.listdir(path)
            folders = []
            files = []
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    folders.append(item)
                elif os.path.isfile(full_path):
                    files.append(item)
            for folder in sorted(folders):
                icon = QIcon('untitled/img/folder.png')
                self.directory.addItem(QtWidgets.QListWidgetItem(icon, folder))
            for file in sorted(files):
                icon = QIcon('untitled/img/file.png')
                self.directory.addItem(QtWidgets.QListWidgetItem(icon, file))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Указанный путь не найден.")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()

    def handle_text_change(self, text):
        return str(text)

    def program_close(self):
        sys.exit()

    def populate_tree_widget(self, directory, parent_item):
        try:
            items = os.listdir(directory)
            for item in items:
                item_path = os.path.join(directory, item)
                try:
                    if os.path.isdir(item_path):
                        tree_item = QTreeWidgetItem(parent_item, [item])
                        self.populate_tree_widget(item_path, tree_item)
                except OSError as e:
                    print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def open_directory(self, item):
        path = os.path.join(self.directoryPath.text(), item.text())
        if os.path.isdir(path):
            self.directoryPath.setText(path)
            self.browse_folder(path)
        else:
            self.open_file(path)

    def open_file(self, path):
        os.startfile(path)

    def up_directory(self, path):
        path_list = str(path).split('\\')
        if len(path_list) > 1:
            path_list.pop()
            path_list = '\\'.join(path_list)
            if path_list[-1] == ":":
                path_list += "\\"
            self.directoryPath.setText(path_list)
            self.browse_folder(path_list)

    def get_path_tree_widget_item(self, item):
        texts = []
        while item is not None:
            texts.insert(0, item.text(0))
            item = item.parent()
            print(texts)
        path = "\\".join(texts)
        print(path)
        path = root_directory + path
        print(path)

        self.directoryPath.setText(path)
        self.browse_folder(path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()