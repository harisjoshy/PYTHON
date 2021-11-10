from omdbapi.movie_search import GetMovie as g
m= g(api_key='630a080f')
print("----Movie details---------")
mv = input('\n Enter movie name')
det = m.get_movie(title=mv)
print(det)

plot = m.get_movie(title=mv,plot='full')
print(plot)

dt = m.get_data('actors','year'
                )
print(dt)
