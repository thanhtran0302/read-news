import os
from .logger import Logger
from datetime import date


def create_today_directory():
    today = today_date()
    if not is_directory_exists():
        os.mkdir('./articles/' + today)
        Logger.success('Today directory is created: ' + today)
    else:
        Logger.warn('Today directory is already existed.')


def is_directory_exists() -> bool:
    return os.path.exists(today_date())


def today_date() -> str:
    return date.today().strftime('%d-%m-%Y')


def title_to_filename(title: str) -> str:
    return title.replace(' ', '-') \
        .replace(',', '-') \
        .replace('.', '-') \
        .replace('\n', '') \
        .lower()


def generate_html_filename(title: str) -> str:
    return title_to_filename(title) + '.html'


def write_html(title: str, html_content: str):
    today = today_date()
    filename = generate_html_filename(title).strip()
    html_file = open('articles/' + today + '/' + filename, 'w')

    html_file.write(build_html_page(html_content))
    Logger.success(filename + ' is created.')


def build_title(title: str) -> str:
    return '<h1>' + title + '</h1>'


def build_html_page(html_content: str) -> str:
    return """
    <html>
        <head>
            <link rel="stylesheet" href="style.css">
            <link
                href="https://fonts.googleapis.com/css2?family=Anton&family=Source+Sans+Pro:wght@300;400;600;700&display=swap"
                rel="stylesheet"
            />
            <meta charset="utf-8" />
        </head>
        <body>
            <article id="main-article">
                {0}
            </article>
        </body>
    </html>
    """.format(html_content)
