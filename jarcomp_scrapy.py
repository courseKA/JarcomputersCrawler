import scrapy

class JarcomputersSpider(scrapy.Spider):
  name = "Jarcomputers"
  urls = urls = [
    "https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1",
    "https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page=2",
    "https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page=3",
    "https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page=4",
    "https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page=5",
]

def parse(self.response):
  
