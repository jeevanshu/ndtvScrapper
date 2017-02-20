from bs4 import BeautifulSoup
import urllib2
import requests
import sys
import io

index=1

def scraper(url):
	global index
	page=urllib2.urlopen(url)

	soup=BeautifulSoup(page,'lxml')

	for i in soup.find_all('div',attrs={'id':'news_list'}):
		for j in i.find_all('li'):
			with io.open('news.txt', 'a', encoding='utf8') as logfile:
				news_link =j.find('a')['href']
				news_title =j.find ('a')['title']
				image_link =j.find('img')['src']
			#print news_title	
				logfile.write(u"%s, %s, %s\n" % (news_title, news_link, image_link))
			
	index+=1
	scraper('https://khabar.ndtv.com/topic/news/news/page-'+str(index))

'''if __name__=='__main__':
	index=1
	scraper('https://khabar.ndtv.com/topic/news/news/page-'+str(index))'''
scraper('https://khabar.ndtv.com/topic/news/news/page-'+str(index))