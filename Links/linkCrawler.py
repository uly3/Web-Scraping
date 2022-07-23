from urllib.error import *
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin


from links import LinkCollector


class Crawler: # does not inherit

    def __init__(self): # create "bins" for storage
        self.crawled = set() # urls that have been read
        self.found = set() # urls that have been found (includes crawled, but also one of greater depth)
        self.dead = set() #urls that could *not* be read successively read
    
    def getCrawled(self):
        return self.crawled
    def getFound(self):
        return self.found
    def getDead(self):
        return self.dead
    
    def crawl(self, url, depth,relativeOnly = True):
        # read the html at url
        # and collect the links found there
        lc = LinkCollector(url)
        try:
            html = urlopen(url).read().decode()
            lc.feed(html)
        except (UnicodeDecodeError, HTTPError, URLError, TypeError):
            self.dead.add(url)

        self.crawled.add(url) # mark url as read already!

        # extract links, relative/absolute depending on relativeOnly
        if relativeOnly == True:
            links = lc.getRelatives()
        else:
            links = lc.getLinks()
        self.found.update(links)

        # recursive crawl the links that were found
        if depth > 0: #empty base case
            for link in links:
                if link not in self.crawled:
                    self.crawl(link,depth-1,relativeOnly)
        


# c = Crawler()
# c.crawl('https://www.cnn.com/',depth=0,relativeOnly= True)
# print(c.getCrawled())
# print(c.getFound())
# print(len(c.getFound()))
# print(c.getDead())



# c = Crawler()
# c.crawl('https://www.cnn.com/',depth=2,relativeOnly= True)
# print(len(c.getCrawled()))
# # print(len(c.getFound()))
# # print(len(c.getDead()))
# # print(c.getDead())



# for hw, just include code in same module
from titles import TitleCollector #for a single page

# collect Titles while crawling
class TitleCrawler(Crawler): #

    #extend init
    def __init__(self):
        Crawler.__init__(self) # add sets for crawled, 
        self.titles = set()
    
    def getTitles(self):
        return self.titles

    # inheriting
    # getCrawled, getFound, getDead
    
    # extend crawl
    def crawl(self, url, depth,relativeOnly = True):
        # do some title collection first
        tc = TitleCollector()
        try:
            tc.feed( urlopen(url).read().decode() )
        except:
            pass
        self.titles.update( tc.getTitles() )

        # do what you would have anyway
        Crawler.crawl(self,url,depth,relativeOnly)



# tc = TitleCrawler()
# tc.crawl('https://www.cnn.com/',depth=0,relativeOnly=True)
# print(tc.getTitles())


# tc = TitleCrawler()
# tc.crawl('https://www.cnn.com/',depth=2,relativeOnly=True)
# print(tc.getTitles())
