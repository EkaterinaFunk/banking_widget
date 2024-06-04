import pytest

from src.decorators import log


def test_log_with_filename(capsys):
    @log(filename="test_log.txt")
    def test_func(x, y):
        return x + y

    test_func(1, 2)

    with open("test_log.txt", "r") as file:
        log_content = file.read()
    assert "test_func" in log_content
    assert "test_func ok" in log_content


def test_log_without_filename(capsys):
    @log()
    def test_func(x, y):
        return x + y

    test_func(1, 2)

    captured_output = capsys.readouterr()
    assert "test_func" in captured_output.out
    assert "test_func ok" in captured_output.out


def test_log_with_error(capsys):
    @log(filename="test_log.txt")
    def test_func(x, y):
        raise ValueError("Error!")

    with pytest.raises(ValueError):
        test_func(1, 2)

    with open("test_log.txt", "r") as file:
        log_content = file.read()
    assert "test_func error: ValueError" in log_content
    assert "Inputs: (1, 2), {}" in log_content
