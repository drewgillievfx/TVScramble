import csv
import random

# three lists used for storing data from csv file to create the random episode
show = []
episode = []
number = []
title = []
description = []


# open csv file and put data into the lists created earlier
with open('episodes.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        show.append(row[0])
        title.append(row[1])
        episode.append(row[2])
        number.append(row[3])
        description.append(row[-1])



## Random Number Generator
min = 0
max = len(show) # replace with max number of rows in .csv file

dannyRand = 0
dannyRand = random.randint(min,max) # my random number
# print dannyRand

SHOW = show[dannyRand]
EPISODE = episode[dannyRand]
NUMBER = number[dannyRand]
TITLE = title[dannyRand]
DESCRIPTION = description[dannyRand]

print # new line
# print the episode to watch at the random number inside each list
print "The random show to watch is: {0}".format(SHOW)
print "Episode Number: {0} {1}".format(EPISODE, NUMBER)
print "Episode Title: {0}".format(TITLE)
print "Episode Description: {0}".format(DESCRIPTION)
print # new line
