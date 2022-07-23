from urllib.request import *

# we won't use it but its useful
# urlretrieve()# input url link
#saves link in your computer


#print parser

from html.parser import HTMLParser

class PrintParser(HTMLParser):
    
    # three methods
    # parameters always the same

    def handle_starttag(self,tag,attrs):
        print('handle_starttag',tag,attrs)
    
    def handle_data(self,data):
        print('handle_data',data)
    
    def handle_endtag(self,tag):
        print('handle_endtag',tag)


# p = PrintParser()
# p.feed()#feed it html # '<a target = blank href=https://www.cnn.com/> CNN </a>'


# Title Collector

class TitleCollector(HTMLParser):

    def __init__(self):
        # always do this
        HTMLParser.__init__(self)
        # container to store titles
        self.titles = []
        #create a flag variable
        self.inTitle = False
    
    def handle_starttag(self,tag,attrs):
        if tag == 'title':
            self.inTitle = True
    
    def handle_data(self,data):
        if self.inTitle == True:
            self.titles.append( data )
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.inTitle = False

    
    def getTitles(self):
        return self.titles



# tc = TitleCollector()
# tc.feed( open('HW7\sample.html').read() )
# print(tc.getTitles())

# cn = TitleCollector()
# cn.feed( urlopen("https://www.cnn.com/").read().decode())
# print(cn.getTitles())
