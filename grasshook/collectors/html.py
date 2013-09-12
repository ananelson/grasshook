from bs4 import BeautifulSoup
import grasshook.collector
import urllib

class HtmlSelector(grasshook.collector.Collector):
    alias = "html-selector"

    def url(self):
        url = self.settings['url']
        username = self.settings['username']
        return "%s/%s" % (url, username)

    def value(self):
        url = self.url()
        f = urllib.urlopen(url)
        html = f.read()
        soup = BeautifulSoup(html)
        selector = self.settings['selector']
        values = soup.select(selector)

        if len(values) != 1:
            msg = "expected one entity to correspond to selector '%s'" % selector
            raise Exception(msg)

        return float(values[0])
