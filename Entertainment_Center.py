import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=8KAtG68bIUc")
#print (avatar.storyline)
#avatar.show_trailer()

social_network = media.Movie("The Social Network",
                             "The movie detailing the creation of Facebook",
                             "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")


school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

wall_street = media.Movie("Wall Street",
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Wall_Street_film.jpg",
                          "https://www.youtube.com/watch?v=FCctqbRrsBQ")

movies = [toy_story,avatar,school_of_rock,social_network,ratatouille,wall_street]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)