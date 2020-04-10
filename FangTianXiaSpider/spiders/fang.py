# -*- coding: utf-8 -*-
import re
import scrapy
from FangTianXiaSpider.items import NewHouseFangItem, EsfFangItem


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.com', 'esf.fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']
    COUNT = 0  # 计数器，用于设计每个城市对应新房列表页首页广告栏的处理开关

    def parse(self, response):
        """
        抓取房天下网站全国已开通658个城市的新房以及二手房的url地址
        :param response: 向房天下网站后台服务器发送start_urls[0]请求资源返回的响应数据
        :return:
        """
        tr_list = response.xpath("//div[@class='outCont']/table[@class='table01']//tr")
        province = None
        for tr in tr_list:
            td_list = tr.xpath(".//td[not(@class)]")
            province_text = td_list[0].xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            if province == "其它":
                continue
            city_links = td_list[1].xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建各大城市新房、二手房对应的url地址
                """
                备注：
                    城市url地址：
                               https://anqing.fang.com/
                    对应新房url地址：
                                  https://anqing.newhouse.fang.com/house/s/
                    对应二手房url地址：
                                    https://anqing.esf.fang.com/

                    特列：北京url地址：
                                    https://bj.fang.com/
                    北京对应新房url地址：
                                      https://newhouse.fang.com/house/s/
                    北京对应二手房url地址：
                                        https://esf.fang.com/
                """
                url_model = city_url.split(".")[0]
                if "bj" in city_url:
                    new_house_url = "https://newhouse.fang.com/house/s/"
                    esf_url = "https://esf.fang.com/"
                else:
                    new_house_url = url_model + ".newhouse" + ".fang.com/house/s/"
                    esf_url = url_model + ".esf" + ".fang.com/"
                # print({"province": province, "city": city, "new_house_url": new_house_url, "esf_url": esf_url})
                yield scrapy.Request(
                    url=new_house_url,
                    callback=self.parse_new_house,
                    meta={"info": (province, city, new_house_url)}
                )

                yield scrapy.Request(
                    url=esf_url,
                    callback=self.parse_esf,
                    meta={
                        "info": (province, city),
                        # 'dont_redirect': True,
                        # 'handle_httpstatus_list': [301, 302]
                    }
                )
            #     break
            # break

    def parse_new_house(self, response):
        """
        解析各大城市对新房的url列表页的相关数据
        :param response: 向房天下网站后台服务器发送各大城市对应的新房(new_house_url)请求资源返回的响应数据
        :return:
        """
        province, city, new_house_url = response.meta.get("info")

        # 获取列表页所有包含lp_属性值的id属性为li节点的元素
        li_list = response.xpath('//div[@id="newhouse_loupai_list"]/ul/li[contains(@id, "lp_")]')
        for li in li_list:
            name = li.xpath('.//div[@class="nlc_img"]//img/@alt').get()
            house_type_text = li.xpath(".//div[contains(@class, 'house_type')]/a/text()").getall()
            house_type_text = list(map(lambda x: re.sub(r"\s|/", "", x), house_type_text))
            rooms = "/".join(list(filter(lambda x: x.endswith("居"), house_type_text)))
            area = "".join(li.xpath(".//div[contains(@class, 'house_type')]/text()").getall())
            area = re.sub(r"\s|/|－", "", area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(r".*\[(.*?)\].*", district_text)
            if district:
                district = district.group(1)
            else:
                district = address
            sale = li.xpath(".//div[contains(@class, 'fangyuan')]/span[1]/text()").get()
            price_text = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price_text)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            origin_url = response.urljoin(origin_url)
            item = NewHouseFangItem(province=province, city=city, name=name, rooms=rooms, price=price,
                                    area=area, address=address, district=district, sale=sale, origin_url=origin_url)
            yield item

        # 翻页
        next_url = response.xpath("//a[text()='下一页']/@href").get()
        if next_url:
            next_url = new_house_url + next_url.split("/")[-2] + "/"
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_new_house,
                meta={"info": (province, city, new_house_url)}
            )

    def parse_esf(self, response):
        """
         解析各大城市对二手房的url列表页的相关数据
        :param response: 向房天下网站后台服务器发送各大城市对应的二手房(esf_house_url)请求资源返回的响应数据
        :return:
        """
        print(response.url)
        province, city = response.meta.get("info")

        # 过滤各大城市新房对应的列表页首页插入的广告li标签
        if self.COUNT >= 1:
            dl_list = response.xpath("//div[contains(@class, 'shop_list')]/dl")
        else:
            dl_list1 = response.xpath("//div[contains(@class, 'shop_list')]/dl")[:6]
            dl_list2 = response.xpath("//div[contains(@class, 'shop_list')]/dl")[7:]
            dl_list = dl_list1 + dl_list2
        for dl in dl_list:
            item = EsfFangItem(province=province, city=city)
            item["name"] = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            room_infos = dl.xpath(".//p[@class='tel_shop']//text()").getall()
            room_infos = list(map(lambda x: re.sub(r"\s|\|", "", x), room_infos))
            for room_info in room_infos:
                if "厅" in room_info:
                    item["rooms"] = room_info
                elif "层" in room_info:
                    item["floor"] = room_info
                elif "向" in room_info:
                    item["toward"] = room_info
                elif "㎡" in room_info:
                    item["area"] = room_info
                elif "建" in room_info:
                    item["year"] = room_info

            item["address"] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item["price_total"] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item["price_unit"] = dl.xpath(".//dd[@class='price_right']/span[2]//text()").get()
            origin_url = dl.xpath(".//h4/a/@href").get()
            item["origin_url"] = response.urljoin(origin_url)

            yield item

            # 翻页
            next_url = response.xpath("//a[text()='下一页']/@href").get()
            if next_url:
                next_url = response.urljoin(next_url)
                self.COUNT += 1
                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse_esf,
                    meta={"info": (province, city)}
                )






