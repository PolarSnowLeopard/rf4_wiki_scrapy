@echo off
python init_db.py
scrapy crawl food -O results/food.json
scrapy crawl fish -O results/fish.json
pause
