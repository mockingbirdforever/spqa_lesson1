from string_utils import StringUtils
import pytest

utils = StringUtils()


@pytest.mark.parametrize('text, result', [
    ('текст', 'Текст'),
    ('Текст', 'Текст'),
    ('1текст', '1текст'),
    (' текст', ' текст'),
])
def test_utils_first_string(text, result):
    util = utils.capitilize(text)
    assert util == result


@pytest.mark.parametrize('text, result', [
    (' текст', 'текст'),
    ('текст', 'текст'),
    ('текст  ', 'текст  '),
    ('  текст  ', 'текст  '),
])
def test_utils_trim(text, result):
    util = utils.trim(text)
    assert util == result


@pytest.mark.parametrize('text, separator, result', [
    ('1:2:3', ':', ['1', '2', '3']),
    ('1ж2ж3', 'ж', ['1', '2', '3']),
    ('абв-абв-абв', '-', ['абв', 'абв', 'абв']),
    ('1 2 3', ' ', ['1', '2', '3']),
])
def test_utils_to_list(text, separator, result):
    util = utils.to_list(text, separator)
    assert util == result


@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'е', True),
    ('Текст', 'у', False),
    ('Текст ', ' ', True),
    ('Текст', 'ек', True),
])
def test_utils_contains(text, symb, result):
    util = utils.contains(text, symb)
    assert util == result


@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'е', 'Ткст'),
    ('Текст1', '1', 'Текст'),
    ('ТеААААААкст', 'А', 'Текст'),
    ('У Текст', 'У ', 'Текст'),
])
def test_utils_delete(text, symb, result):
    util = utils.delete_symbol(text, symb)
    assert util == result


@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'Т', True),
    ('Текст', 'т', False),
    ('текст', 'т', True),
    (' Текст', ' ', True),
])
def test_utils_start(text, symb, result):
    util = utils.starts_with(text, symb)
    assert util == result


@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'т', True),
    ('Текст', 'Т', False),
    ('Текст ', ' ', True),
    ('Текст', ' ', False),
])
def test_utils_end(text, symb, result):
    util = utils.end_with(text, symb)
    assert util == result


@pytest.mark.parametrize('text, result', [
    ('', True),
    ('т', False),
])
def test_utils_empty(text, result):
    util = utils.is_empty(text)
    assert util == result


@pytest.mark.parametrize('text, separator, result', [
    (['1', '2', '3'], ':', '1:2:3'),
    (['1', '2', '3'], '-', '1-2-3'),
    (['а', 'аа', 'ааа'], '-а-', 'а-а-аа-а-ааа'),
    (['1', '2', '3'], '', '123'),
])
def test_utils_to_string(text, separator, result):
    util = utils.list_to_string(text, separator)
    assert util == result


