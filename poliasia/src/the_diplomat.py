from .utils import build_title, write_html
from .logger import Logger


def the_diplomat_scrapper(response):
    article = response.css('#td-story-body')
    title = response.css('#td-headline::text').get()
    date = response.css('.td-date [itemprop="datePublished"]').get()
    lead_title = response.css('#td-lead').get()
    paragraphs = article.css('p').getall()
    html = build_title(title) + lead_title + date

    for paragraph in paragraphs:
        if paragraph.find('td-ad-inline') == -1:
            Logger.info('Adding paragraph to html content')
            html = html + paragraph

    write_html(title, html)
