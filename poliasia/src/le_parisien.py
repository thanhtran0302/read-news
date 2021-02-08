from .utils import build_title, write_html


def le_parisien(response):
    title = response.css('h1.title_xl::text').get()
    subtitle = response.css('h2.subheadline::text').get()
    image = response.css('section #primary_left img.image').get()
    paragraphs = response.css('.article-section section.content').getall()
    text = ''
    html = build_title(title) + subtitle + image

    for paragraph in paragraphs:
        text = text + paragraph
    html = html + text
    write_html(title, html)
