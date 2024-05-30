# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import pymysql
from itemadapter import ItemAdapter

class MySQLPipeline:

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=spider.settings.get('MYSQL_HOST'),
            user=spider.settings.get('MYSQL_USER'),
            password=spider.settings.get('MYSQL_PASSWORD'),
            port=spider.settings.get('MYSQL_PORT'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

        # Read and execute SQL file

        with open(r'db.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            print(sql_script)
        for statement in sql_script.split(';'):
            if statement.strip():
                self.cursor.execute(statement)
        self.connection.commit()

        # Connect to the newly created database
        self.connection.select_db(spider.settings.get('MYSQL_DATABASE'))

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        sql = "INSERT INTO food (name, description, img, type, class, producer, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (
            adapter.get('name'),
            adapter.get('description'),
            adapter.get('img'),
            adapter.get('type'),
            adapter.get('cls'),
            adapter.get('producer'),
            adapter.get('price')
        ))
        self.connection.commit()
        return item
