import os
import pytest

from main import ExampleApp


@pytest.fixture
def app():
    # Создаем экземпляр приложения
    app = ExampleApp()
    yield app
    # Закрываем приложение после завершения теста
    app.close()


def test_browse_folder(app):
    # Проверяем, что функция browse_folder правильно обрабатывает существующий путь
    path = os.getcwd()
    app.browse_folder(path)
    assert app.directory.count() > 0  # Проверяем, что список не пустой


def test_up_directory(app):
    # Проверяем, что функция up_directory корректно переходит на уровень выше
    initial_path = app.directoryPath.text()
    app.up_directory(initial_path)
    assert app.directoryPath.text() == os.path.dirname(initial_path)


def test_open_directory(app):
    # Проверяем, что функция open_directory открывает директорию
    initial_path = os.getcwd()
    app.open_directory(initial_path)
    assert app.directoryPath.text() == initial_path


def test_open_file(app):
    # Проверяем, что функция open_file открывает файл
    path = os.path.join(os.getcwd(), "README.md")
    with open(path, "w") as file:
        file.write("Test")
    app.open_file(path)
    # Проверяем, что файл открыт в операционной системе


def test_program_close(app, qtbot):
    # Проверяем, что функция program_close закрывает приложение
    with qtbot.waitSignal(app.closed):
        app.program_close()