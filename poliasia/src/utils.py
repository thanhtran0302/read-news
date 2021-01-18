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
