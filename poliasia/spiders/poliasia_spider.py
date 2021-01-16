import json
import scrapy
from poliasia.src.logger import Logger
from poliasia.src.the_economist import json_to_html


class DiplomatSpider(scrapy.Spider):
    name = 'news'
    url = ''

    def __init__(self, *args, **kwargs):
        self.url = kwargs['url']
        self.html_file = open('article.html', 'w')

        super(DiplomatSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

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

    def the_diplomat_scrapper(self, response):
        article = response.css('#td-story-body')
        title = response.css('#td-headline').get()
        date = response.css('.td-date [itemprop="datePublished"]').get()
        lead_title = response.css('#td-lead').get()
        paragraphs = article.css('p').getall()
        html = title + lead_title + date

        for paragraph in paragraphs:
            if paragraph.find('td-ad-inline') == -1:
                Logger.info('Adding paragraph to html content')
                html = html + paragraph

        self.html_file.write(html)
        Logger.success('HTML file created. Ready to read.')

    def foreign_policy_scrapper(self, response):
        title = response.css('span.hed-heading').get()
        description = response.css('h2.dek-heading').get()
        article = response.css('div.post-content-main').get()
        html = title + description + article

        self.html_file.write(html)
        Logger.success('HTML file created. Ready to read.')

    def asia_nikkei_scrapper(self, response):
        title = response.css('h1.article-header__title').get()
        subtitle = response.css('p.article-header__sub-title').get()
        main_image = response.css('[data-trackable="image-main"] .img-fluid').get()
        article = response.css('.ezrichtext-field').get()
        html = title + subtitle + main_image + article

        self.html_file.write(html)
        Logger.success('HTML file created. Ready to read.')

    def the_economist(self, response):
        title = response.css('.article__headline').get()
        description = response.css('.article__description').get()
        image = response.css('.article__lead-image').get()
        publish_date = response.css('.article__dateline-datetime').get()
        content = response.css('#__NEXT_DATA__::text').get()
        article = json_to_html(json.loads(content))
        html = title + description + image + publish_date + article

        self.html_file.write(html)
        Logger.success('HTML file created. Ready to read.')
