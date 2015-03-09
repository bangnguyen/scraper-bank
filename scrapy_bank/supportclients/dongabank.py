from scrapy import Item, Field
import re
import pdb
import traceback
from scrapy_bank.items import  *

class dongabank:

    @classmethod
    def create_date(cls,response):
        all_tr=response.xpath("//div[@id='main-content']//table//tr")
        result = []
        for tr in all_tr:
            try:
                item = BankData()
                duration_raw =tr.xpath("./td//span//text()")[0].extract()
                rate_raw=tr.xpath("./td//span//text()")[1].extract()
                duration = re.search("\d+",duration_raw).group(0)
                rate = re.search("\d+\.\d+",rate_raw).group(0)
                item['duration'] = "%s month"%(duration)
                item['rate'] = rate
                item['url'] = "http://www.dongabank.com.vn/interest/1206/tiet-kiem-uu-viet-vnd"
                item['name']='Dong A'
                result.append(item)
                print "%s %s"%(duration,rate)
            except:
                traceback.print_exc()
                pass
        for item in result:
            yield item
