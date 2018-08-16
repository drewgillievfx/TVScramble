import urllib2
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup



def getSeasons(show):

    my_url = "https://www.imdb.com/title/{0}/episodes?ref_=tt_ov_epl".format(show)

    # open connection and grab page
    uClient = uReq(my_url)

    # put into a variable
    page_html = uClient.read()

    # close connection
    uClient.close()

    #html parsing
    page_soup = soup(page_html, "html.parser")

    # finds how many seasons are in this show
    containers = page_soup.findAll("div", {"class": "seasonAndYearNav"})

    container = containers[0]
    # the location of the season information
    seasons = container.div.div.text.split()

    seasons.pop(0)
    ## If errors occur, the following lines may be helpful in determining problems
    # for i in seasons:
    #     print type(i)

    # find the length of the list to determine the number of seasons in a show
    Seasons = len(seasons)
    # print Seasons # This is the answer!
    return Seasons # This is the answer!


## for testing purposes
# Monk = 'tt0312172'
# getSeasons(Monk)
