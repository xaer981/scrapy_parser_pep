import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        all_peps = response.css(
            'section[id="numerical-index"] a[href^="pep-"]')

        for pep_link in all_peps:

            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'PEP (?P<number>\d+) \W (?P<name>.*)'
        pep_title = response.css('h1.page-title::text').get()
        number, name = re.search(pattern, pep_title).groups()

        yield PepParseItem(
            {'number': number,
             'name': name,
             'status': (response.css('dt:contains("Status") + dd abbr::text')
                        .get())}
        )
