Hello!

TV Scramble Version: 1.0.0

This project uses the BeautifulSoup API to get information from IMDB
You may need to install a few things before you can run this code!

BeautifulSoup:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

You need to run episodeSearch.py first to generate a csv file with your shows in
it so that TVScramble.py can be run to generate a random episode.
It grabs the info from the csv file and places it in a list to grab from.

To add shows:
in episodeSearch.py navigate to the show list and create a show with the code
found in the url on IMDB, it should look like this one from the show Monk:
https://www.imdb.com/title/tt0312172/episodes?season=1
the "tt0312172" is the code for the show and by changing this you can add new
shows for your own custom generator.

If you run into any badChars and it causes the program to stop midway, here is
the table I use:
https://en.wikipedia.org/wiki/ISO/IEC_8859-1



There will be more features to come! This is only the beginning! There are plans
to make it so that the user no longer needs to search for a show, and replace
the code. With this also, make a prompt for the user to type any shows they want
for a custom generator. 
