#!/usr/bin/env python3
import media
import fresh_tomatoes
# import media class and create instant for each movie
# That contains movie name, poster, trailer URL
titanic_movie = media.Movie("TITANIC",
                            "https://www.onthisday.com/images/articles/titanic-the-movie.jpg",
                            "https://www.youtube.com/watch?v=-iRajLSA8TA")
rise_movie = media.Movie("Dark Knight Rises",
                         "https://a.ltrbxd.com/resized/film-poster/1/6/5/5/0/16550-the-dark-knight-rises-0-230-0-345-crop.jpg?k=38a6974b66",
                         "https://www.youtube.com/watch?v=GokKUqLcvD8")
cinderella_movie = media.Movie("Cinderella",
                               "https://images-na.ssl-images-amazon.com/images/I/91q8P5pre-L._SY679_.jpg",
                               "https://www.youtube.com/watch?v=20DF6U1HcGQ")
heat_movie = media.Movie("HEAT",
                         "https://images-na.ssl-images-amazon.com/images/I/81CP5MtTvYL._SL1500_.jpg",
                         "https://www.youtube.com/watch?v=2GfZl4kuVNI")
salt_movie = media.Movie("SALT",
                         "https://orig00.deviantart.net/096f/f/2010/234/4/1/salt_fan_movie_poster_by_amidsummernights.jpg",
                         "https://www.youtube.com/watch?v=QZ40WlshNwU")
guest_movie = media.Movie("Invisible Guest",
                          "https://images-cdn.9gag.com/photo/abz0j5O_700b.jpg",
                          "https://www.youtube.com/watch?v=epCg2RbyF80")
train_movie = media.Movie("Train To Busan",
                          "http://barkerhost.com/wp-content/uploads/sites/4/2016/10/duzUfxOZlGoVoN2i3C0XJrQ66YG-3.jpg",
                          "https://www.youtube.com/watch?v=1ovgxN2VWNc")
hard_movie = media.Movie("A Hard Day",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/A_Hard_Day_2014.jpg/220px-A_Hard_Day_2014.jpg",
                         "https://www.youtube.com/watch?v=lP4Y-fExtR4")
meg_movie = media.Movie("The Meg",
                        "https://media.kg-portal.ru/movies/m/meg/posters/meg_12.jpg",
                        "https://www.youtube.com/watch?v=udm5jUA-2bs")
# Group all the instant in one list and pass the list to open_movies_page
# function from fresh_tomatoes class to display the movies in html page
movies = [titanic_movie, rise_movie, cinderella_movie, heat_movie, salt_movie,
          guest_movie, train_movie, hard_movie, meg_movie]
fresh_tomatoes.open_movies_page(movies)
