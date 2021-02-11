from rest_framework.exceptions import ParseError
from django.conf import settings
from rest_framework import renderers
from rest_framework.parsers import BaseParser
import json

class MyJSONParser(BaseParser):
    media_type = 'application/json'
    renderer_class = renderers.JSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        request = parser_context.get('request')
        try:
            data = stream.read().decode(encoding)
            setattr(request, 'raw_body', data) # setting a 'body' alike custom attr with raw POST content
            return json.loads(data)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % str(exc))
