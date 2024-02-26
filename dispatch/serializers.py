from collections import OrderedDict

from rest_framework import serializers


class DocumentSerializer(serializers.Serializer):
    """
    Поля для работы с POST запросом:
    "name" = название файла,
    "data" = текстовое содержимое файла.
    """

    name = serializers.CharField(max_length=100)
    data = serializers.CharField()

    def validate(self, data: OrderedDict[str, str]) -> OrderedDict[str, str]:
        """Проверяет поле "name" на наличие недопустымих символов"""

        if data['name'] != data['name'].translate(str.maketrans('', '', r'+=[]:*?;«,./\<>|')):
            raise serializers.ValidationError('В поле \'name\' присутствуют недопустимые символы')
        return data

    class Meta:
        fields = ('data', 'name')
