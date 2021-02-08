from .utils import build_title, write_html


def foreign_policy_scrapper(response):
    title = response.css('span.hed-heading .hed::text').get()
    description = response.css('h2.dek-heading').get()
    article = response.css('div.post-content-main').get()
    html = build_title(title) + description + article

    write_html(title, html)
