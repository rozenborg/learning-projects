# import webbrowser

class Movie():
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""This function is a constructor which initiates the Movie() class with the attributes title, storyline, poster_image_url, and trailer_youtube_url"""

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	

	# def show_trailer(self):
	# 	"""this function launches a web browser to play the video link from youtube displaying the trailer for the movie of interest."""

	# 	webbrowser.open(self.trailer_youtube_url)