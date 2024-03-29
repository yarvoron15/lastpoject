import requests
from parsel import Selector

class NewsScraper:
    PLUS_URL = "https://edu.gov.kg"
    URL = 'https://edu.gov.kg/posts/'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }

    LINK_XPATH = '//a[@class="nav-link"]/@href'
    TITLE_XPATH = '//p[@class="footer-rights text-center"]/text()'
    DESCRIPTION_XPATH = '//li[@class="list-group-item"]/a/text()'
    IMG_XPATH = '//div[@class="col-md-2"]/img/@src'




    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        titles = tree.xpath(self.TITLE_XPATH).getall()
        descriptions = tree.xpath(self.DESCRIPTION_XPATH).getall()
        imgs = tree.xpath(self.IMG_XPATH).getall()
        # for link in links:
        #     print(self.PLUS_URL + link)
        # for img in imgs:
        #     print(img)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()