from .utils import  build_title, write_html


def nytimes(response):
    title = response.css('[data-test-id="headline"]::text').get()
    description = response.css('#article-summary').get()
    image = response.css('header picture img').get()
    publish_date = response.css('time.css-129k401.e16638kd0').get()
    body = response.css('[name="articleBody"]').get()
    html = ''

    if title is not None:
        html = html + build_title(title)
    if description is not None:
        html = html + description
    if image is not None:
        html = html + image
    if publish_date is not None:
        html = html + publish_date
    if body is not None:
        html = html + body
    write_html(title, html)
