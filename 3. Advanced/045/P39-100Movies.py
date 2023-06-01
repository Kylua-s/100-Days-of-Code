import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get the HTML content of the web page
webpage = requests.get(URL).text
soup = BeautifulSoup(webpage, "html.parser")

# Finds all the movies
movies = soup.find_all("h3", class_="title")
movies_sorted = []

# Reveres the order and gets the movie titel
for movie in movies:
    movies_sorted.insert(0, movie.getText())

# Writes all movie titles in the txt file
with open("movies.txt", "w") as file:
    for movie in movies_sorted:
        if "59)" not in movie:
            file.write(movie + "\n")
        else:
            movie = movie.replace("â", "-")
            file.write(movie + "\n")

"""
Movie 59 is a bit out of space ...
The raw html code is: <h3 class="title">59) E.T. â The Extra Terrestrial</h3>
And the titel is: E.T. â\x80\x93 The Extra Terrestrial
So I don't know why or what this means, but it seems to be wrong on the web side?
HTML unescape didn't help either. But it could be connected to the unicode \xe2\x80\x93 witch is a –.
Since this is the only movie with this sort of problem and after 2h of searching, I don't think it is worth any more 
time and I just worked around it.
"""
