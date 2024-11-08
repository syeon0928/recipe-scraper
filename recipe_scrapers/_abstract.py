from urllib import request
from bs4 import BeautifulSoup
import ssl
import certifi


# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}

class AbstractScraper:
    def __init__(self, url, test=False):
        if test:  # when testing, we load a file
            with url:
                self.soup = BeautifulSoup(url.read(), "html.parser")
        else:
            # Create an SSL context that uses the certifi certificate authority
            context = ssl.create_default_context(cafile=certifi.where())

            self.soup = BeautifulSoup(request.urlopen(
                request.Request(url, headers=HEADERS), context=context).read(), "html.parser", from_encoding="utf-8")

    def host(self):
        """ get the host of the url, so we can use the correct scraper (check __init__.py) """
        raise NotImplementedError("This should be implemented.")

    def title(self):
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    def instructions(self):
        raise NotImplementedError("This should be implemented.")

    def picture(self):
        raise NotImplementedError("This should be implemented.")

    def tags(self):
        raise NotImplementedError("This should be implemented.")

    def servings(self):
        raise NotImplementedError("This should be implemented.")

    def ratings(self):
        raise NotImplementedError("This should be implemented.")

    def author(self):
        raise NotImplementedError("This should be implemented.")

    def publish_date(self):
        raise NotImplementedError("This should be implemented.")