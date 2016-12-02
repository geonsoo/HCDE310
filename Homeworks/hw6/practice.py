# -*- coding: utf-8 -*-
import urllib2
import time
import datetime


stocktoPull = 'AAPL', 'GOOG'

def pullData(stock):
    try:
        print 'Currently pulling', stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        saveFileLine = stock + '.txt'
        
        try:
            readExistingData = open(saveFileLine, 'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = int(mostRecentLine.split(',')[0])
            
        
        except: 
            lastUnix = 0
            

        #fileLine = stock + '.txt'
#        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
 #       sourceCode = urllib2.urlopen(urlToVisit).read()
  #      splitSource = sourceCode.split('\n')
        
   #     for eachLine in splitSource:
    #        splitLine = eachLine.split(',')
     #       if len(splitLine) == 6:
      #          if 'values' not in eachLine:
       #             saveFile = open(fileLine, 'a')
        ##           saveFile.write(lineToWrite)
                        
       # print 'Pulled', stock
        #print 'sleeping'
        #time.sleep(5)

    except Exception, e:
        print 'main loop', str(e)
        
for eachStock in stocktoPull:
    pullData(eachStock)
        
        