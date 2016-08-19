import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=8KAtG68bIUc")
print (avatar.storyline)
#avatar.show_trailer()

social_network = media.Movie("The Social Network",
                             "The movie detailing the creation of Facebook",
                             "https://en.wikipedia.org/wiki/The_Social_Network#/media/File:Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")
social_network.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

wall_street = media.Movie("Wall Street",
                          "Storyline",
                          "https://en.wikipedia.org/wiki/Wall_Street_(1987_film)#/media/File:Wall_Street_film.jpg",
                          "https://www.youtube.com/watch?v=FCctqbRrsBQ")

movies = [toy_story,avatar,school_of_rock,social_network,ratatouille,wall_street]
fresh_tomatoes.open_movies_page(movies)