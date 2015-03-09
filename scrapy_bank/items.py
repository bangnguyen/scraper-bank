from scrapy import Item, Field


class BankData(Item):
    name = Field()
    url = Field()
    duration = Field()
    rate = Field()
