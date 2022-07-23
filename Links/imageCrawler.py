from links import LinkCollector  
from linkCrawler import Crawler
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError


#Problem 1

class ImageCollector(LinkCollector):
    
    def __init__(self,url):
        # self.url = url
        HTMLParser.__init__(self)
        LinkCollector.__init__(self,url)
    
    # override method
    def handle_starttag(self,tag,attrs): # attrs is a list of tuples (pairs)
        if tag == 'img':
            # print( tag, attrs)
           for attr,val in attrs:
                if attr == 'src': # collect value
                    # convert to absolute form
                    link = urljoin( self.url,val)
                    if val[:4] == 'http': # absolute
                       self.absolutes.add( link )
                    else: #relative
                        self.relatives.add( link )
    
    def getImages(self): # relative + absolute
        return self.absolutes | self.relatives
        # return self.absolutes.union(self.relatives)  


# ic = ImageCollector('http://www.kli.org/')
# ic.feed( urlopen('http://www.kli.org/').read().decode())
# # print(type( ic.getImages() ))
# print(sorted( ic.getImages() ) )


class ImageCrawler(Crawler):
    #extend init
    def __init__(self):
        Crawler.__init__(self) # add sets for crawled, 
        self.images = set()

    def getImages(self):
        return self.images
    
    # inheriting
    # getCrawled, getFound, getDead
    
    # extend crawl
    def crawl(self, url, depth,relativeOnly = True):
        # do some title collection first
        tc = ImageCollector(url)
        try:
            tc.feed( urlopen(url).read().decode() )
        except:
            pass
        self.images.update( tc.getImages() )

        # do what you would have anyway
        Crawler.crawl(self,url,depth,relativeOnly)
        


# c = ImageCrawler()
# c.crawl('http://www.pmichaud.com/toast/',1,True)
# print(type( c.getImages() ) )
# print(sorted( c.getImages() ))
# print(len( c.getImages() ))


def scrapeImages(url,filename,depth,relativeOnly):
    #crawl images
    im = ImageCrawler()
    im.crawl(url,depth,relativeOnly)

    # create file for images
    with open(filename, 'w') as file: #"file = open(filename, 'w'), won't have to close it!!!"
        
        file.write('<html><body>\n')
        #write all the links
        for link in im.getImages():
            file.write( f"<img src={link}> {link} </a><br>\n" )
        #close html
        file.write('</body></html>')



# scrapeImages('http://www.pmichaud.com/toast/','toast.html',1,True)
# print(open('toast.html').read().count('img'))
