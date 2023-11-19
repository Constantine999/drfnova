from rest_framework import status

from drfnova.settings import drive


def create_file(file_name: str, file_content: str) -> tuple[str, str]:
    '''Создает в Google Drive файл "file_name".doc c текстом "file_content" '''

    try:
        my_file = drive.CreateFile({'title': f'{file_name}.doc'})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'Файл с именем {file_name}.doc успешно загружен в Google Drive', status.HTTP_201_CREATED
    except Exception as error:
        return f'Файл не был создан, ошибка - {error}', status.HTTP_400_BAD_REQUEST
