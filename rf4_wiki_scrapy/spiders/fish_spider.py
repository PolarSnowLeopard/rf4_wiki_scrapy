from pathlib import Path

import scrapy
from rf4_wiki_scrapy.items import FishItem

class FishSpider(scrapy.Spider):
    name = "fish"

    def start_requests(self):
        urls = [
            "https://www.gamekee.com/rf4/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 鱼类图鉴block
        block = response.xpath(r'//*[@id="menu-126030"]/div[position() >= 2 and position() <= 3]/div[2]')

        # 鱼类图鉴下的所有物品
        for div in block.xpath('div[*]'):
            for item in div.css("a.item"):
                detail_page = response.urljoin(item.attrib["href"])
                yield scrapy.Request(detail_page, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        从详情页面提取名称等信息。
        """
        item = FishItem()

        # item['name'] = response.css("div.cheracter-profile-main > div.info-main > div.name > div > div > span")[0].css("::text").get()
        try:
            item['name'] = response.css("div.cheracter-profile-main > div.info-main > div.name > div > div > span")[0].css("::text").get()
        except Exception as e:
            item['name'] =  response.css("h1")[0].css("::text").get()

        try:
            item['img'] = response.css('.cheracter-profile-main > div.image-album').css("img").attrib["src"]
        except Exception as e:
            item['img'] = None

        try:
            item['cls'] = response.css("div.attr-list")[0].css('div.attr-box')[1].css("span::text")[1].get()
        except Exception as e:
            item['cls'] = None

        try:
            item['description'] = response.css('.cheracter-profile-desc')[0].css("*::text")[1].get()
        except Exception as e:
            item['description'] = None

        try:
            item['rare_weight'] = response.css("div.attr-list")[0].css('div.attr-box')[2].css("span::text")[2].get()
        except Exception as e:
            item['rare_weight'] = None

        try:
            item['super_rare_weight'] = response.css("div.attr-list")[0].css('div.attr-box')[3].css("span::text")[2].get()
        except Exception as e:
            item['super_rare_weight'] = None

        yield item