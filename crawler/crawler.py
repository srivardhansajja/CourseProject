import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess

import time
import sys

ignore = ["contrib", "expert", "mail", "covid", "provost", "registrar", "publish", 
          "activit", "organisation", "entry", "\?", "%", "publication", "calendar", 
          "category", "blog", "store", "shop", "resources", "policies", "calendars", 
          "library", "twitter", "facebook", "careers", "login", "query", "queries", 
          "disability", "research", "product", "services", "mediaspace", "search", 
          "diversity", "youtube", "instagram", "linkedin", "news"]

a = set()
matching_urls = set()

start_time = 0
elapsed_time = 0

time_limit = 0
match_limit = 0


class FacultyPageSpider(scrapy.Spider):

    name = 'fcrawler'

    def parse(self, response):

        global elapsed_time

        le = LinkExtractor(deny=ignore)
        for link in le.extract_links(response):

            elapsed_time = time.time() - start_time

            if len(matching_urls) >= match_limit or elapsed_time >= time_limit:
                raise scrapy.exceptions.CloseSpider(reason='limit_reached')
            if ('faculty' in link.url or 'staff' in link.url) and link.url not in a:
                with open('crawler/matched_urls.txt', 'a') as f:
                    f.write(link.url + '\n')
                matching_urls.add(link.url)
            if link.url not in a:
                a.add(link.url)
                yield Request(link.url, callback=self.parse)


def callSpider(domain_, start_url_, time_limit_, match_limit_):

    global time_limit
    global match_limit
    global start_time
    global elapsed_time

    time_limit = time_limit_
    match_limit = match_limit_
    start_time = time.time()
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)', 
        'LOG_LEVEL': 'CRITICAL',
    })

    process.crawl(FacultyPageSpider, allowed_domains = [domain_], 
                                     start_urls      = [start_url_],)
    process.start()

    return matching_urls, len(matching_urls), elapsed_time


if __name__ == "__main__":

    # domain_ = 'illinois.edu'
    # start_url_ = 'https://illinois.edu'
    # time_limit_ = 100
    # match_limit_ = 20

    domain_ = sys.argv[1]
    start_url_ = sys.argv[2]
    time_limit_ = int(sys.argv[3])
    match_limit_ = int(sys.argv[4])
    
    with open('crawler/matched_urls.txt', 'w') as f:
        f.write('')

    urls, size, time = callSpider(domain_, start_url_, time_limit_, match_limit_)

    # print("size:", size)
    # print("time:", time)
    # print("\nURLS:")
    # for url in matching_urls:
    #     print(url)
