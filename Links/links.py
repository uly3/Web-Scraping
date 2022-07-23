from urllib.parse import urljoin


from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class LinkCollector(HTMLParser):

    def __init__(self,url):
        HTMLParser.__init__(self)
        # add attributes/containers
        self.url = url
        # sets for storing links
        self.relatives = set()
        self.absolutes = set()
    
    def handle_starttag(self,tag,attrs): # attrs is a list of tuples (pairs)
        if tag == 'a':
            # print( tag, attrs)
           for attr,val in attrs:
                if attr == 'href': # collect value
                    # convert to absolute form
                    link = urljoin( self.url,val)
                    if val[:4] == 'http': # absolute
                       self.absolutes.add( link )
                    else: #relative
                        self.relatives.add( link )


    def getAbsolutes(self):
        return self.absolutes
    
    def getRelatives(self):
        return self.relatives
    
    def getLinks(self): # relative + absolute
        return self.absolutes | self.relatives
        # return self.absolutes.union(self.relatives)



# lc = LinkCollector('http://cnn.com') # base URL
# lc.feed( urlopen('http://cnn.com').read().decode() )
# lc.getAbsolutes()
# # .. returns SET of absolute links ...
# lc.getRelatives()
# # ... returns SET of relative links (written in absolute form)...
# lc.getLinks()
# # ... returns SET of all links found (in absolute form) ...



def scrapeLinks( url, filename):
    # ''' collect all links found at url and write to the html file filename'''

    # use a LinkCollector to collect links
    lc = LinkCollector(url)
    lc.feed( urlopen(url).read().decode() )

    # write links to a file
    with open(filename, 'w') as file: #"file = open(filename, 'w'), won't have to close it!!!"
        
        file.write('<html><body>\n')
        #write all the links
        for link in lc.getLinks():
            file.write( f"<a href={link}> {link} </a><br>\n" )
        #close html
        file.write('</body></html>')

# scrapeLinks('https://www.cnn.com/', 'cnn.html')



#This whole code file scrapes a list of links from a website
