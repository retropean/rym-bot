import scrapy
import datetime
import time as timer
from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import date, time
from rymbot.items import RymbotItem

class rymSpider(Spider):
	name = "rym"
	allowed_domains = ["https://rateyourmusic.com"]
	urls = []

	def __init__(self, daysoutcmmd=0, *args, **kwargs):
		self.daysout = daysoutcmmd
		now = datetime.datetime.now() + datetime.timedelta(int(self.daysout))
		self.readyear = now.year
		self.readday = now.strftime('%d')
		self.readmonth = now.strftime('%m')
	
	def start_requests(self):
		years = []
		year = 1960
		while (year <=2018):
			years.append(year)
			year = year + 1
		pagecounter = range(1,5)
		url_pattern = "https://rateyourmusic.com/charts/top/album/{year}/{page}"

		for yearage in years:
			for page in pagecounter:
				self.urls.append(url_pattern.format(year=yearage,page=page))

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)
			
	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('.//table[@class="mbgen"]//tr')
		items = []
		for site in sites:
			item = RymbotItem()
			item['year'] = (response.request.url[-6:])[:4] #year of album
			item['ranking'] = site.xpath('.//td[1]/span/text()').extract() #rank
			item['artist'] = site.xpath('.//td[3]/div[1]/div[2]/span/a/text()').extract() #artist
			item['album'] =  site.xpath('.//td[3]/div[1]/div[2]/div[1]/a/text()').extract() #album
			item['genre'] = site.xpath('.//td[3]/div[1]/div[2]/div[2]/span/a[1]/text()').extract() #genre
			item['rating'] = site.xpath('.//td[3]/div[2]/a[1]/b[1]/text()').extract() #rym rating
			item['ratings'] = site.xpath('.//td[3]/div[2]/a[1]/b[2]/text()').extract() #num of ratings
			item['reviews'] = site.xpath('.//td[3]/div[2]/a[1]/b[3]/text()').extract() #num of reviews
			items.append(item)
		return items