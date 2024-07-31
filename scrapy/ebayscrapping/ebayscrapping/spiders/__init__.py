"""
This module contains Scrapy spiders for scraping eBay and Computer Zone.

Classes:
- EbayScrapper: A Scrapy spider to scrape product information from eBay.
- ComputerZoneScrapper: A Scrapy spider to scrape product information from Computer Zone.
"""

import scrapy
from urllib.parse import urlparse, unquote


class EbayScrapper(scrapy.Spider):
    """
    A Scrapy spider to scrape product information from eBay.

    Attributes:
        name (str): The name of the spider.
        allowed_domains (list): The domains that the spider is allowed to crawl.
        start_urls (list): The initial URLs to start scraping from.
        category (str): The category extracted from the provided URL.

    Methods:
        __init__(self, url=None, *args, **kwargs):
            Initializes the spider with the provided URL and extracts the category from it.

        start_requests(self):
            Generates initial requests to start the scraping process.

        parse(self, response):
            Parses the product list from the response and follows product URLs.

        parse_product_details(self, response):
            Extracts detailed information about each product from the product page.
    """
    name = 'ebay_scrapper'
    allowed_domains = ['ebay.com']

    def __init__(self, url=None, *args, **kwargs):
        """
        Initializes the EbayScrapper spider with the provided URL.

        Args:
            url (str, optional): The URL to start scraping from. If provided, it will be used to extract the category.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super(EbayScrapper, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        if url:
            parsed_url = urlparse(url)
            self.category = unquote(parsed_url.path.split('/')[2]) if len(parsed_url.path.split('/')) > 2 else 'Unknown'

    def start_requests(self):
        """
        Generates initial requests to start the scraping process.

        Yields:
            scrapy.Request: Request objects for the URLs in start_urls.
        """
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """
        Parses the product list from the response and follows product URLs.

        Args:
            response (scrapy.http.Response): The response object containing the product list.

        Yields:
            scrapy.Request: Request objects for each product page.
        """
        products = response.css('li.s-item')
        for product in products:
            product_url = product.css('a::attr(href)').get()
            if product_url:
                yield scrapy.Request(product_url, callback=self.parse_product_details)

    def parse_product_details(self, response):
        """
        Extracts detailed information about each product from the product page.

        Args:
            response (scrapy.http.Response): The response object containing the product details.

        Yields:
            dict: A dictionary containing product details such as name, price, image URL, seller, and sold count.
        """
        name = response.css('h1 span::text').get()
        price = response.css('.x-price-primary span::text').get()
        img_url = response.css('.ux-image-carousel-item img::attr(src)').get()
        seller = response.css('.x-sellercard-atf__info__about-seller::attr(title)').get()
        sold_count = response.css('.x-quantity__availability span::text').getall()
        product_data = {
            'name': name,
            'price': price,
            'img_url': img_url,
            'seller': seller,
            'sold_count': sold_count,
            'category': self.category,
            'url': response.url
        }

        yield product_data


class ComputerZoneScrapper(scrapy.Spider):
    """
    A Scrapy spider to scrape product information from Computer Zone.

    Attributes:
        name (str): The name of the spider.
        allowed_domains (list): The domains that the spider is allowed to crawl.
        start_urls (list): The initial URL to start scraping from.

    Methods:
        parse(self, response):
            Parses the product list from the response and follows product URLs and category links.

        parse_category(self, response):
            Parses the product list from the category page and handles pagination.

        parse_product_detail(self, response):
            Extracts detailed information about each product from the product page.
    """
    name = 'computer_zone_scrapper'
    allowed_domains = ['czone.com.pk']
    start_urls = ['https://www.czone.com.pk/']

    def parse(self, response):
        """
        Parses the product list from the home page and follows product URLs and category links.

        Args:
            response (scrapy.http.Response): The response object containing the product list and category links.

        Yields:
            scrapy.Request: Request objects for each product page and each category page.
        """
        products = response.css('.product')
        for product in products:
            product_url = product.css('.image a::attr(href)').get()
            if product_url:
                full_product_url = response.urljoin(product_url)
                yield scrapy.Request(full_product_url, callback=self.parse_product_detail)

        categories = response.css('.navbar-nav ul li a::attr(href)').getall()
        print(categories)

        for category_url in categories:
            full_category_url = response.urljoin(category_url)
            yield scrapy.Request(full_category_url, callback=self.parse_category)

    def parse_category(self, response):
        """
        Parses the product list from the category page and handles pagination.

        Args:
            response (scrapy.http.Response): The response object containing the product list and pagination links.

        Yields:
            scrapy.Request: Request objects for each product page and the next page if available.
        """
        products = response.css('.product')
        for product in products:
            product_url = product.css('.image a::attr(href)').get()
            if product_url:
                full_product_url = response.urljoin(product_url)
                yield scrapy.Request(full_product_url, callback=self.parse_product_detail)

        next_page_url = response.css('.pagination .NextPage::attr(href)').get()
        if next_page_url:
            full_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(full_next_page_url, callback=self.parse_category)

    def parse_product_detail(self, response):
        """
        Extracts detailed information about each product from the product page.

        Args:
            response (scrapy.http.Response): The response object containing the product details.

        Yields:
            dict: A dictionary containing product details such as name, brand, description, price, and image URL.
        """
        name = response.css('.product-title::text').get()
        brand = response.css('.product-brand span::text').getall()
        description = response.css('.details-description::text').get()
        details = response.css(".details-description ul li::text").getall()
        price = response.css('.price-sales::text').get()
        image_url = response.css('img::attr(src)').getall()[1]

        if image_url and image_url.startswith('/'):
            image_url = response.urljoin(image_url)

        product_data = {
            'name': name,
            'brand': brand,
            'description': description,
            'price': price,
            'image_url': image_url,
            'details': details,
        }
        yield product_data
