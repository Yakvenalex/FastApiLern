import json


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет её в файл.

    :param dict_list: Список словарей
    :param filename: Имя файла для сохранения JSON-строки
    :return: JSON-строка или None в случае ошибки
    """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


def json_to_dict_list(filename):
    """
    Преобразует JSON-строку из файла в список словарей.

    :param filename: Имя файла с JSON-строкой
    :return: Список словарей или None в случае ошибки
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None
