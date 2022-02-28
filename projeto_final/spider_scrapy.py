import scrapy
from urllib.parse import urljoin


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.python.org/'
    ]

    visitado = set()
    fila = []
    nivel = 1
    def parse(self, response):
        for l in response.css('a::attr(href)').getall():
            link = urljoin(response.url, l)
            self.fila.append(link)
            self.visitado.add(link)
            yield {'link': link}
        self.nivel += 1

        while len(self.fila) != 0 and self.nivel <= 5:
            prox_pag = self.fila.pop(0)
            yield scrapy.Request(prox_pag, callback=self.parse)
        return self.visitado