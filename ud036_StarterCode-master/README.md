Project Descriptions: 
entertainment_center & media & fresh_tomatoes are a simples scripts that gathering your
favorite movies in one web page and  displaying the movies Title, Poster and Trailer URL.

How to display the HTML web page:
1. install python 3.
2. install all the three files and save it in the same place.
3. open the entertainment_center file and the run the module.

How to watch the trailers:
Only one click in the image poster it will display the trailer movie.

How to use a Movie class in the entertainment_center file to add a new movie:
1. define the instant name for each movie, example: movie_name
2. assign the instant with constructor call, example: movie_name = media.Movie()
3. pass the Title of the movie, poster URL and trailer URL.
4. add the new instant to the movies list and run the file. 

Code explanations:
1. A 	Movie class in media file that encapsulate the properties of the movie, which they are:
1.1 title
1.2 poster_image_url 
1.3 trailer_youtube_url 
2. The entertainment_center file that contains the objects of all the movies that displaying
in the web page with their properties by calling media.Movie()  constructor.
3. Add the objects in one list and passes to open_movies_page() function to display HTML page.
