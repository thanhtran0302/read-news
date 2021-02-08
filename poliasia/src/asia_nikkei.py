import json
from .utils import build_title, write_html


def asia_nikkei_scrapper(response):
    title = response.css('h1.article-header__title span.ezstring-field::text').get()
    subtitle = response.css('p.article-header__sub-title').get()
    main_image = response.css('[data-trackable="image-main"] .img-fluid').get()
    article = response.css('.ezrichtext-field').get()
    html = build_title(title) + subtitle + main_image + article

    write_html(title, html)
