# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Rf4WikiScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FoodItem(scrapy.Item):
    sql = "INSERT INTO food (name, description, img, type, class, producer, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    fields_list = ["name", "description", "img", "type", "cls", "producer", "price"]
    name = scrapy.Field()
    description = scrapy.Field()
    img = scrapy.Field()
    type = scrapy.Field()
    cls = scrapy.Field()
    producer = scrapy.Field()
    price = scrapy.Field()

class FishItem(scrapy.Item):
    sql = "INSERT INTO fish (name, description, img, class, rare_weight, super_rare_weight) VALUES (%s, %s, %s, %s, %s, %s)"
    fields_list = ["name", "description", "img", "cls", "rare_weight", "super_rare_weight"]
    name = scrapy.Field()
    description = scrapy.Field()
    img = scrapy.Field()
    cls = scrapy.Field()
    rare_weight = scrapy.Field()
    super_rare_weight = scrapy.Field()