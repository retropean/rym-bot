import scrapy

class RymbotItem(scrapy.Item):
	ranking = scrapy.Field()
	artist = scrapy.Field()
	album = scrapy.Field()
	genre = scrapy.Field()
	rating = scrapy.Field()
	ratings = scrapy.Field()
	reviews = scrapy.Field()
	year = scrapy.Field()
	pass
