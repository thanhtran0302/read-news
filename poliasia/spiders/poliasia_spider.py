import json
import scrapy
from poliasia.src.logger import Logger
from poliasia.src.the_economist import json_to_html
from poliasia.src.utils import write_html, build_title


class DiplomatSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        f = open('./URLs.txt', 'r')
        urls = f.read().split('\n')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url

        if url.find('thediplomat.com') != -1:
            yield self.the_diplomat_scrapper(response)
        elif url.find('foreignpolicy.com') != -1:
            yield self.foreign_policy_scrapper(response)
        elif url.find('asia.nikkei.com') != -1:
            yield self.asia_nikkei_scrapper(response)
        elif url.find('economist.com') != -1:
            yield self.the_economist(response)
        elif url.find('nytimes.com') != -1:
            yield self.nytimes(response)

    def the_diplomat_scrapper(self, response):
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

    def foreign_policy_scrapper(self, response):
        title = response.css('span.hed-heading .hed::text').get()
        description = response.css('h2.dek-heading').get()
        article = response.css('div.post-content-main').get()
        html = build_title(title) + description + article

        write_html(title, html)


    def asia_nikkei_scrapper(self, response):
        title = response.css('h1.article-header__title span.ezstring-field::text').get()
        subtitle = response.css('p.article-header__sub-title').get()
        main_image = response.css('[data-trackable="image-main"] .img-fluid').get()
        article = response.css('.ezrichtext-field').get()
        html = build_title(title) + subtitle + main_image + article

        write_html(title, html)

    def the_economist(self, response):
        title = response.css('.article__headline::text').get()
        description = response.css('.article__description').get()
        image = response.css('.article__lead-image').get()
        publish_date = response.css('.article__dateline-datetime').get()
        content = response.css('#__NEXT_DATA__::text').get()
        article = json_to_html(json.loads(content))
        html = build_title(title) + description + image + publish_date + article

        write_html(title, html)

    def nytimes(self, response):
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
