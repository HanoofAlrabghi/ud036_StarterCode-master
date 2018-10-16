# Create a Movie class contain __init__ Constructor that assign the instants
class Movie():
    # define a instant variables for the movies name, poster, trailer URL
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
