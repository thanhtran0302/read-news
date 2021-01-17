from .logger import Logger


def title_to_filename(title: str) -> str:
    return title.replace(' ', '-') \
        .replace(',', '-') \
        .replace('.', '-') \
        .replace('\n', '') \
        .lower()


def generate_html_filename(title: str) -> str:
    return title_to_filename(title) + '.html'


def write_html(title: str, html_content: str):
    filename = generate_html_filename(title)
    html_file = open('articles/' + filename, 'w')

    html_file.write(html_content)
    Logger.success(filename + ' is created.')


def build_title(title: str) -> str:
    return '<h1>' + title + '</h1>'
