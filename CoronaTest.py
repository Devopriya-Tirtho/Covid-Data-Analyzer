from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=6
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ =="__main__":
    while True:
        myHtmlData=getData('https://www.mohfw.gov.in/')    
        
        soup= BeautifulSoup(myHtmlData,'html.parser')
        
        myDataStr=""
        
        for tr in soup.find_all('tbody'):
            myDataStr += tr.get_text()
        
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")
        states=['Telengana','Uttar Pradesh']
        
        for item in itemList[0:22]:
            dataList=item.split('\n')
            if dataList[1] in states:
                nTitle = 'Cases of Covid-19'
                nText = f"state {datalist[1]}\n Indian :{datalist[2]} : {datalist[3]} : {datalist[4]} : {datalist[5]}"
                notifyme(nTitle,ntext)
                time.sleep(2)
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        