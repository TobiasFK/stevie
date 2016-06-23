from markov_python.cc_markov import MarkovChain
import time

print "\nSTEVIE WONDER'S WORDS OF WISDOM."
time.sleep(2)
print "\nStevie Wonder is the master of life. Ask him anything, and his reply will change your life!"
time.sleep(2)
question = raw_input("\nWhat would you like to ask Stevie? ")
markov_lyrics = open("lyrics.txt", "r")
mc = MarkovChain()
mc.add_string(markov_lyrics.read())
markov_lyrics.close()

time.sleep(1)

print "\nStevie is thinking..."

time.sleep(3)

answer = " ".join(mc.generate_text())
answer = answer.capitalize()
print "\n***********************************************\n\nSTEVIE: %s\n\n********************************************" % answer