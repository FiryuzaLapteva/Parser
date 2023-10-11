def url_mod(input_file_path, output_file_path):

    """
    Модифицирует файл, добавляя "https://" к каждой строке и сохраняя результат в другой файл.

    :param input_file_path: Путь к входному файлу.
    :param output_file_path: Путь к выходному файлу.

    :return: None
    """
# открываем исходный файл для чтения и изменный файл для записи
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Итеративно проходим по каждой строчки файла
        for line in input_file:
        # Добавляем "https://" в начале каждой строчки
            modified_line = 'https://' + line.strip()
        # записываем изменения в modified_line
            output_file.write(modified_line + '\n')