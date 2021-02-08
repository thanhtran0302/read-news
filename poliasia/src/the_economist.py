import json
from .utils import build_title, write_html


def get_attribs(attribs: dict) -> str:
    attributs = []

    for key, value in attribs.items():
        attributs.append(key + '="' + value + '"')
    return ''.join(attributs)


def build_tag(element):
    data = ''

    if element['type'] == 'tag':
        data = data + '<' + element['name']
        if len(element['attribs']) != 0:
            data = data + ' ' + get_attribs(element['attribs']) + '>'
        else:
            data = data + '>'
    elif element['type'] == 'text':
        data = data + element['data']

    if 'children' in element:
        for child in element['children']:
            data = data + build_tag(child)
        data = data + '</' + element['name'] + '>'
    return data


def json_to_html(data):
    text = data['props']['pageProps']['content']['text']
    html_content = ''

    for item in text:
        html_content = html_content + build_tag(item)
    return html_content


def the_economist(response):
    title = response.css('.article__headline::text').get()
    description = response.css('.article__description').get()
    image = response.css('.article__lead-image').get()
    publish_date = response.css('.article__dateline-datetime').get()
    content = response.css('#__NEXT_DATA__::text').get()
    article = json_to_html(json.loads(content))
    html = build_title(title) + description + image + publish_date + article

    write_html(title, html)
