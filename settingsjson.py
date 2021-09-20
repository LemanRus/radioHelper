import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'example title'},
    {'type': 'numeric',
     'title': 'Размер шрифта заголовков',
     'desc': 'Numeric description text',
     'section': 'font',
     'key': 'header_size'},
    {'type': 'numeric',
     'title': 'Размер шрифта текста',
     'desc': 'Numeric description text',
     'section': 'font',
     'key': 'text_size'},
    {'type': 'numeric',
     'title': 'Размер шрифта кнопок',
     'desc': 'Numeric description text',
     'section': 'font',
     'key': 'button_size'},
])
