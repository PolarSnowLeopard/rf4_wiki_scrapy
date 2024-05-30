from pathlib import Path

import scrapy
from rf4_wiki_scrapy.items import FoodItem

class FoodSpider(scrapy.Spider):
    name = "food"

    def start_requests(self):
        urls = [
            "https://www.gamekee.com/rf4/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 食品图鉴block
        block = response.xpath(r'//*[@id="menu-137366"]/div[position() >= 2 and position() <= 4]/div[2]')

        # 食品图鉴下的所有物品
        for div in block.xpath('div[*]'):
            for item in div.css("a.item"):
                detail_page = response.urljoin(item.attrib["href"])
                yield scrapy.Request(detail_page, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        从物品详情页面提取名称价格等信息。
        """
        item = FoodItem()

        item['img'] = response.css('.cheracter-profile-main > div.image-album').css("img").attrib["src"]
        item['name'] = response.css("div.cheracter-profile-main > div.info-main > div.name > div > div > span")[0].css("::text").get()

        item['type'] = response.css("div.attr-list")[0].css('div.attr-box')[0].css('span::text')[1].get()
        item['cls'] = response.css("div.attr-list")[0].css('div.attr-box')[2].css('span::text')[1].get()
        try:
            item['producer'] = response.css("div.attr-list")[0].css('div.attr-box')[3].css('span::text')[1].get()
            item['producer'] = item['producer'].replace("\ufeff", "")
        except Exception as e:
            item['producer'] = ""

        item['description'] = response.css('.cheracter-profile-desc')[0].css("span::text")[1].get()

        price = dict()
        price_selectors = response.css('.cheracter-profile')[1].css("span::text")
        for i in range(1, len(price_selectors), 2):
            key = price_selectors[i].get()
            value = price_selectors[i+1].get() if i+1 < len(price_selectors) else ""
            price[key] = value
        item['price'] = str(price)

        yield item