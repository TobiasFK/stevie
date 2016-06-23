import urllib2
from bs4 import BeautifulSoup, SoupStrainer

lyrics_directory = urllib2.urlopen("http://www.metrolyrics.com/stevie-wonder-lyrics.html")
html = lyrics_directory.read()

def correct_links(tag):
	return tag.has_attr("href") and tag.has_attr("onmousedown")

def lyric_links():
	link_list = []
	html_soup = BeautifulSoup(html, "html.parser")
	for link in html_soup.find_all(correct_links):
		url = link.get("href")
		if "lyrics-stevie-wonder.html" in url and "correction" not in url:
			link_list.append(url)
	print link_list

def lyric_links_test():
	link_list_test = [u'http://www.metrolyrics.com/superstition-lyrics-stevie-wonder.html', u'http://www.metrolyrics.com/i-just-called-to-say-i-love-you-lyrics-stevie-wonder.html', u'http://www.metrolyrics.com/isnt-she-lovely-lyrics-stevie-wonder.html']
	lyrics_list = []
	for url in link_list_test:
		lyrics_from_list = urllib2.urlopen(url)
		read_lyrics = lyrics_from_list.read()
		bs_read_lyrics = BeautifulSoup(read_lyrics, "html.parser")
		for verse in bs_read_lyrics.find_all("p", class_='verse'):
			lyrics_list.append(verse.get_text())
	print "\n".join(lyrics_list)


lyric_links_test()
