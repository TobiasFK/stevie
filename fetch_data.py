import urllib2
from bs4 import BeautifulSoup, SoupStrainer

def correct_links(tag):
	return tag.has_attr("href") and tag.has_attr("onmousedown")

def lyric_links():
	lyrics_directory = urllib2.urlopen("http://www.metrolyrics.com/stevie-wonder-lyrics.html")
	html = lyrics_directory.read()
	link_list = []
	lyrics_list = []
	html_soup = BeautifulSoup(html, "html.parser")

	"""
	""This code collects all lyrics urls and stores them in a list
	"""
	for link in html_soup.find_all(correct_links):
		url = link.get("href")
		if "lyrics-stevie-wonder.html" in url and "correction" not in url:
			link_list.append(url)
	"""
	""This code extracts lyrics text from the list of urls that contains Stevie Wonder lyrics
	"""
	
	for link in link_list:
		lyrics_from_list = urllib2.urlopen(link)
		read_lyrics = BeautifulSoup(lyrics_from_list.read(), "html.parser")
		for verse in read_lyrics.find_all("p", class_='verse'):
			lyrics_list.append(verse.get_text())


	"""
	""This code creates/updates file that stores the consolidated lyrics
	"""
	lyrics = str(" ".join(lyrics_list))
	lyrics_file = open("lyrics.txt", "w")
	lyrics_file.write(lyrics)
	lyrics_file.close()