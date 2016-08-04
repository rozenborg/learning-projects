"""This file contains the content (titles, movie descriptions, poster urls, and trailer urls) to be hosted on the movie website."""

import fresh_tomatoes
import media

toy_story_4 = media.Movie("Toy Story 4", "Wow, they're still making these things...", "http://vignette1.wikia.nocookie.net/disney/images/2/29/Toy_Story_4_D23_Poster.png/revision/latest?cb=20151011015858", "https://www.youtube.com/watch?v=QW0sjQFpXTU")

kill_bill = media.Movie("Kill Bill", "Must... kill... Bill...", "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg", "https://www.youtube.com/watch?v=ot6C1ZKyiME")

reefer_madness = media.Movie("Reefer Madness", "Marijuana kills! You're next!", "https://upload.wikimedia.org/wikipedia/en/e/e2/ReeferMadnessPoster.jpg", "https://www.youtube.com/watch?v=sbjHOBJzhb0")

sex_lives_of_the_potato_men = media.Movie("Sex Lives of the Potato Men", "British people flerp about selling veggies and being gross.", "https://upload.wikimedia.org/wikipedia/en/b/be/Sex_Lives_of_the_Potato_Men_DVD_cover.jpg", "https://www.youtube.com/watch?v=VUmfu3Dgexs")

superbabies = media.Movie("Superbabies: Baby Geniuses 2", "Babies with super powers for some reason.", "https://upload.wikimedia.org/wikipedia/en/a/aa/Superbabies_poster.JPG", "https://www.youtube.com/watch?v=hyJuSjpoMfg")

drunken_master = media.Movie("Drunken Master", "Kung Fu guru fights at his best when he shwaystee.", "http://ia.media-imdb.com/images/M/MV5BMTc1NjYxMTExNl5BMl5BanBnXkFtZTYwNTU2NTI5._V1_.jpg", "https://www.youtube.com/watch?v=KQMNllz6aE0")

movies = [toy_story_4, reefer_madness, sex_lives_of_the_potato_men, superbabies, drunken_master]
fresh_tomatoes.open_movies_page(movies)