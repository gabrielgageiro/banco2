from scrapy import Spider

import scrapy

class StackSpider(Spider):
    name = "stack"
    def start_requests(self):
        urls = ["http://200.187.8.90/boletim-stelecom/?bo_cod=3196",
               ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for linha in response.xpath('//*[@id="content-i"]/article/table[2]'):
            yield {
                'veiculos': linha.xpath('//*[@id="content-i"]/article/table[2]/tbody/tr[2]/td[1]//text()').extract_first(),
                'marca': linha.xpath('//*[@id="content-i"]/article/table[2]/tbody/tr[2]/td[2]//text()').extract_first(),
                'modelo': linha.xpath('//*[@id="content-i"]/article/table[2]/tbody/tr[2]/td[3]//text()').extract_first(),
                'placa': linha.xpath('//*[@id="content-i"]/article/table[2]/tbody/tr[2]/td[4]//text()').extract_first(),

            }
