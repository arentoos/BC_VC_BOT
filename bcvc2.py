#/usr/bin/env Python
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.firefox.options import Options

from io import open
import time
import datetime
from datetime import date
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from Tkinter import *
import requests
from bs4 import BeautifulSoup
from random import choice
from random import randint

def GetProxy():
	url = 'https://www.sslproxies.org/'
	r = requests.get(url)
	soup = BeautifulSoup(r.content,'html5lib')
	return choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])),(map(lambda x: x.text, soup.find_all('td')[1::8])))))))

def ana2():
	pencere = Tk()
	pencere.title("BCVC BOT")


	l = Label(pencere)
	l.config(text=u"Deneme Sayısı : ")
	l.grid(row=0,column=0)

	global l1

	l1 = Label(pencere)
	l1.config(text=u"")
	l1.grid(row=0,column=1)

	l = Label(pencere)
	l.config(text=u"Denen Proxy Adresi : ")
	l.grid(row=1,column=0)

	global l2

	l2 = Label(pencere)
	l2.config(text=u"")
	l2.grid(row=1,column=1)

	l = Label(pencere)
	l.config(text=u"Denen Link Adresi : ")
	l.grid(row=2,column=0)

	global l3

	l3 = Label(pencere)
	l3.config(text=u"")
	l3.grid(row=2,column=1)

	l = Label(pencere)
	l.config(text=u"Sonuç : ")
	l.grid(row=3,column=0)

	global sonuc

	sonuc = Label(pencere)
	sonuc.config(text=u"")
	sonuc.grid(row=3,column=1)

	global tekrar
	global linkd

	tekrar = int(tekrar.get())
	for tekrars in range(tekrar):
		links = linkd.get()
		filehandle = open('%s.txt' % links, 'r')
		link = [current_place.rstrip() for current_place in filehandle.readlines()]
		url = link[randint(0, 150)]
		proxy = GetProxy()
		l1.config(text=u"" + str(tekrars))
		pencere.update()

		firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
		firefox_capabilities['marionette'] = True

		firefox_capabilities['proxy'] = {
   			"proxyType": "MANUAL",
    		"httpProxy": proxy,
    		"ftpProxy": proxy,
    		"sslProxy": proxy
		}

		options = Options()
		options.headless = True

		driver = webdriver.Firefox(capabilities=firefox_capabilities,options=options)
			
		try:
			l2.config(text=u"" + proxy)
			l3.config(text=u"" + url)
			pencere.update()
			driver.get("%s" % url)
			button = driver.find_element_by_xpath('//*[@id="getLink"]')
			time.sleep(7)
			button.click()
			time.sleep(10)
			driver.quit()
			sonuc.config(text=u"" + proxy + " : ~~ BAŞARILI OLDU! ~~")
			pencere.update()
		except:
			driver.quit()
			sonuc.config(text=u"" + proxy + " : ~~ BAŞARISIZ OLDU! ~~")
			pencere.update()
			continue
				
	pencere.mainloop()
	
def ana():
	pencere = Tk()
	pencere.title("BCVC BOT")

	l = Label(pencere)
	l.config(text=u"Kaç Defa Proxy Denesin : ")
	l.grid(row=0,column=0)

	global tekrar

	tekrar = Entry(pencere)
	tekrar.grid(row=0,column=1)

	l = Label(pencere)
	l.config(text=u"Denenecek Linklerin Dosyasını Yazınız : ")
	l.grid(row=1,column=0)

	global linkd

	linkd = Entry(pencere)
	linkd.grid(row=1,column=1)

	b1 =Button(pencere,text=u"BOTU BAŞLAT",command=ana2)
	b1.grid(row=2,column=1)

	pencere.mainloop()

ana()