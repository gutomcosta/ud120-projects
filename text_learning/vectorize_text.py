#!/usr/bin/python

import pickle
import sys
import re
import os

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        # if temp_counter < 200:
        path = os.path.join('..', 'tools', path[:-1])
        print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        words = parseOutText(email)

        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        for v in ["sara", "shackleton", "chris", "germani"]:
            words = words.replace(v, "")
        # words = words.replace("sara", "").replace("shackleton", "").replace("chris", "").replace("germani", "")
        ### append the text to word_data
        word_data.append(words)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        from_label = 0 if from_person == "sara" else "1"
        from_data.append(from_label)

        email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

print word_data[152]




### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer

vect = TfidfVectorizer(stop_words="english", strip_accents="unicode", lowercase=True)
bag_of_words = vect.fit_transform(word_data)

print vect.vocabulary_
for k, v in  vect.vocabulary_.iteritems():
    if v == 34597:
        print "Word: ", k
print len(vect.get_feature_names())





