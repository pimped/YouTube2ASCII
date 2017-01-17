import urllib
import urllib2
from bs4 import BeautifulSoup
import os, sys, math, random, webbrowser
#$$ Make sure you have YouTube-DL installed

print """
YouTube ASCII Player
by shade

"""
while True:
	search = raw_input("Search:")
	textToSearch = (search)
	query = urllib.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    		command = "https://www.youtube.com" + vid['href']
    	os.system("youtube-dl " + (command) + " -o - |     mplayer -vo aa -monitorpixelaspect 0.5 -")
