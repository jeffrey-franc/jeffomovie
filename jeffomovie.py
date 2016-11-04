import media
import fresh_tomatoes

starwars = media.Movie("Return of the Jedi",
                       "Space thing about a bad dude",
                       "https://images-na.ssl-images-amazon.com/images/I/51UdiBUkerL._SY450_.jpg",
                       "https://www.youtube.com/watch?v=5UfA_aKBGMc")

dolce_vita = media.Movie("La Dolce Vita",
                         "Why it is cool to be Italian",
                         "https://pccdn.perfectchannel.com/christies/live/images/item/VintageFilmPosters25099/5812423/original/CSK_10275_0068.jpg",
                         "https://www.youtube.com/watch?v=2YZjAn0GZfE")

casablanca = media.Movie("Casablanca",
                         "Being in love sucks",
                         "https://www.movieposter.com/posters/archive/main/23/MPW-11602",
                         "https://www.youtube.com/watch?v=jQTWfGOv1JY")

gladiator = media.Movie("Gladiator",
                        "Strength and Honor",
                        "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/uploads/2013/10/gladiatorbg.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo")

movies = [starwars, dolce_vita, casablanca,gladiator]
fresh_tomatoes.open_movies_page(movies)

print(starwars.__name__)
print(starwars.__doc__)
