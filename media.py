import webbrowser
"Project 1 of FSND. Movie Trailers website. The Movie Class stores relevant information for favorite movies"
class Movie:
    def __init__(self, movie_title , movie_storyline, poster_image, trailer_youtube, year_release):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
    	self.trailer_youtube_url = trailer_youtube
    	self.release_year = year_release

    def show_trailer(self):
    	open.webbrowser(self.trailer_youtube)

        
    
