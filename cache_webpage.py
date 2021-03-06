from urllib.request import urlopen
import time


class WebPage:
    refresh_interval = 1 # in seconds

    def __init__(self, url):
        self.url = url
        self._content = None
        self.lastupdatetime = time.time()


    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self.lastupdatetime = time.time()
        return self._content


    @property
    def refresh(self):
        rgt_now = time.time()

        if self.lastupdatetime < (rgt_now - self.refresh_interval):
            self._content = urlopen(self.url).read()
            self.lastupdatetime = time.time()
            print("refresh")
        return self._content
