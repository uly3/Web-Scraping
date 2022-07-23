from urllib.request import *
from html.parser import HTMLParser

#Problem 1

class HeadingParser(HTMLParser):

    def __init__(self):
        # always do this
        HTMLParser.__init__(self)
        # container to store headings
        self.headings = []
        #create a flag variable
        self.inHeading = False
    
    def handle_starttag(self,tag,attrs):
        if tag == 'h1' or tag == 'h2' or tag == 'h3' or tag == 'h4' or tag == 'h5' or tag == 'h6':
            self.inHeading = True
    
    def handle_data(self,data):
        if self.inHeading == True:
            self.headings.append( data.strip() )
    
    def handle_endtag(self, tag):
        if tag == 'h1' or tag == 'h2' or tag == 'h3' or tag == 'h4' or tag == 'h5' or tag == 'h6':
            self.inHeading = False
    
    def getHeadings(self):
        cleanList = []
        for i in self.headings:
            if i == '':
                pass
            else:
                cleanList.append(i)
        return cleanList
    


# test = HeadingParser()
# test.feed( open('HW7\sample.html').read() )
# print(test.getHeadings())

# hp = HeadingParser()
# html = urlopen('http://www.pmichaud.com/toast/').read().decode()
# hp.feed( html )
# print(hp.getHeadings())


#Problem 2

def testHP(url):
    hp = HeadingParser()
    hp.feed( urlopen(f'{url}').read().decode() )
    return hp.getHeadings()

print(testHP('http://www.pmichaud.com/toast/'))
# print(testHP('http://home.mcom.com/home/welcome.html'))
# print(testHP('http://usatoday30.usatoday.com/sports/baseball/sbfant.htm'))
