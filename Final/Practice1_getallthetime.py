# -*- coding: utf-8 -*-
import urllib2
import time

stocktoPull = 'AAPL', 'GOOG'

def pullData(stock):
    try:        

        fileLine = stock + '.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite = eachLine + '\n'
                    saveFile.write(lineToWrite)
                        
        print 'Pulled', stock
        print 'sleeping'
        time.sleep(5)

    except Exception, e:
        print 'main loop', str(e)
        
for eachStock in stocktoPull:
    pullData(eachStock)
        