import scrapy


class Amazon(scrapy.Spider):
    # identify
    name = 'amazon'

    # request
    def start_requests(self):
        file = open('links.txt', 'r')
        urls = []
        for line in file.readlines():
            urls.append(line.replace('\n', ''))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse
    def parse(self, response):
        review = response.css('.review-text')
        comments = review.css('.review-text')
        for comment in comments:
            yield {
                'comment': ''.join(comment.xpath(".//text()").extract())
            }
