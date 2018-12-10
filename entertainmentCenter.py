from movies_project import fresh_tomatoes
from movies_project import media

toystory = media.Movie("toystory",
                       "a story about a boy ...",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "a file about ,,",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")

frances_ha = media.Movie("Frances HA",
                         "a film about two girls living ..",
                         "https://upload.wikimedia.org/wikipedia/en/6/69/Frances_Ha_poster.png",
                         "https://www.youtube.com/watch?v=y9YKHRQkf7k")
school_of_rock = media.Movie("school of rock",
                             "a movie about bla bla ",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
midnight_in_paris = media.Movie("midnight_in_paris",
                                "a night in paris ..",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
#print(toystory.title)
#print(avatar.storyline)
#avatar.Show_Trailer()
my_moveis =[toystory,avatar,frances_ha,school_of_rock,midnight_in_paris]
fresh_tomatoes.open_movies_page(my_moveis)