import json
import scrapy
from poliasia.src.logger import Logger
from poliasia.src.the_economist import json_to_html, the_economist
from poliasia.src.the_diplomat import the_diplomat_scrapper
from poliasia.src.foreign_policy import foreign_policy_scrapper
from poliasia.src.asia_nikkei import asia_nikkei_scrapper
from poliasia.src.nytimes import nytimes
from poliasia.src.utils import write_html, build_title, is_directory_exists,\
    create_today_directory


class DiplomatSpider(scrapy.Spider):
    name = 'news'

    def __init__(self):
        is_dir_exists = is_directory_exists()
        if is_dir_exists is False:
            create_today_directory()

    def start_requests(self):
        f = open('./URLs.txt', 'r')
        urls = f.read().split('\n')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url

        if url.find('thediplomat.com') != -1:
            yield the_diplomat_scrapper(response)
        elif url.find('foreignpolicy.com') != -1:
            yield foreign_policy_scrapper(response)
        elif url.find('asia.nikkei.com') != -1:
            yield asia_nikkei_scrapper(response)
        elif url.find('economist.com') != -1:
            yield the_economist(response)
        elif url.find('nytimes.com') != -1:
            yield nytimes(response)
        elif url.find('leparisien.fr') != -1:
            yield le_parisien(response)
