from markov_python.cc_markov import MarkovChain
from fetch_data import lyric_links

lyric_links()

markov_lyrics = open("lyrics.txt", "r")
mc = MarkovChain()
mc.add_string(markov_lyrics.read())
markov_lyrics.close()

answer = " ".join(mc.generate_text())
answer = answer.capitalize()
print answer