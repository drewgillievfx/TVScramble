import urllib2
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from seasons import *


DEBUG = False

"""
Some show descriptions use unicode characters and are in need of replacement
as more characters populate, this table will be used for replacing characters
"""
badChars = {u'\xe4':'a',
            u'\xe9':'e'}


"""
Create a .csv file to export show data into.
This could also be turned into a list later on depending on the scope of the
of the project
"""
filename = "episodes.csv"
f = open(filename, "w")

headers = "Show, Title, Season, Episode, Description\n"
f.write(headers)

################################################################################
"""
add new shows here and in the list
to find a shows code, go to IMDb and search a show. then go to episode listing
and select a season. it is the number that starts with tt
"""
Monk = 'tt0312172'
Psych = 'tt0491738'
HIMYM = 'tt0460649'

# list for grabbing episodes from
# This could also be a promt to ask the user which shows they want to shuffle
shows = [Monk, Psych, HIMYM]

################################################################################
## start the main portion of the script
## start the for loop for getting episode info

"""
This first loop is for iterating through every unique show in the users list
1. Get show Title
2. Get the number of seasons in the show
3. Get
"""
for j in shows:

    show = j
    seasons = 0
    seasons = getSeasons(j)

    # This sets up the number of seasons for the loop
    z = seasons + 1
    # This loop will iterate through every season in each specific show
    for i in range(1, z):
        seasons = i

        my_url = "https://www.imdb.com/title/{0}/episodes?season={1}".format(show, seasons)
        # print my_url

        # open connection and grab page
        uClient = uReq(my_url)

        # put into a variable
        page_html = uClient.read()

        # close connection
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        # finds the episodes in this particular season
        containers = page_soup.findAll("div", {"class": "list_item"})

        # Show Title
        titleOfShow = page_soup.findAll("div", {"class": "subpage_title_block"})
        showTitle1 = titleOfShow[0].div.a #text.strip()
        showTitle = showTitle1.text.strip()

        # how many episodes were found
        # hm  = len(containers)

        # print str(hm) + " Episodes"
        # print

        container = containers[0]

        for container in containers:


            # Episode Title
            episodeTitle = container.div.div.img["alt"]

            # Episode Number
            episode = container.div.div.div
            episodeNumber = episode.text

            # Episode Description
            description = container.findAll("div", {"class": "item_description"})
            episodeDescription = description[0].text.strip()


            #print(showTitle)
            # print("episodeTitle: " + episodeTitle)
            # print("episodeNumber: " + episodeNumber)
            # print("episodeDescription: " + episodeDescription)
            # print


            # if the first statment does not work, there may be badChars in it
            try:
                f.write(showTitle + "," + episodeTitle.replace(",", " ") + "," + episodeNumber + "," + episodeDescription.replace(",", " ") + "\n")
            except UnicodeEncodeError:
                for key in badChars:
                    for char in episodeDescription:
                        if char == key:
                            # print char + " " + badChars[key]
                            episodeDescription = episodeDescription.replace(char, badChars[key])

                f.write(showTitle + "," + episodeTitle.replace(",", " ") + "," + episodeNumber + "," + episodeDescription.replace(",", " ") + "\n")



# Close the document and finish the script
f.close()
print 'This script has finished running'
