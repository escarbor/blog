from django.core import serializers


def comment_serializer(comments):
    data = serializers.serialize('json', comments)
    return data
