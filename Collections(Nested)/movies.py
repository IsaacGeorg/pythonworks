# Nested Dictionary for movies

movies=[
    {'id':1,'title':"kishkindakandam","language":"malayalam","year":2024,"runtime":160,"rating":4.5},
    {'id':2,'title':"stree","language":"hindi","year":2018,"runtime":170,"rating":4.6},
    {'id':3,'title':"aquaman: the lost kingdom","language":"english","year":2023,"runtime":160,"rating":4.0},
    {'id':4,'title':"stree 2","language":"hindi","year":2024,"runtime":180,"rating":4.6},
    {'id':5,'title':"salaar","language":"telungu","year":2023,"runtime":150,"rating":4.9},
    {'id':6,'title':"kgf","language":"telungu","year":2018,"runtime":150,"rating":4.6},
    {'id':7,'title':"kgf: chapter 2","language":"telungu","year":2022,"runtime":160,"rating":4.9},
    {'id':8,'title':"maleficient","language":"english","year":2016,"runtime":140,"rating":4.2},
    {'id':9,'title':"GOAT","language":"tamil","year":2024,"runtime":180,"rating":4.4},
] 

# Total number of movies
print(len(movies))

# To print movie titles 
movie_title=[m.get("title") for m in movies]
print(movie_title)

# To print hindi movies
movie_lang=[m.get("title") for m in movies if m.get("language")=="hindi"]
print(movie_lang)

# To print a telungu movie with respect to its year
movielang_year=[m.get("title") for m in movies if m.get("language")=="telungu" and m.get("year")==2023]
print(movielang_year)

# To get maximum runtime movie
max_run=max(movies,key=lambda mr:mr.get("runtime"))
print(max_run)

# Minimum runtime movie
min_run=min(movies,key=lambda mir:mir.get("runtime"))
print(min_run)

same_maxruntime=max(movies,key=lambda m:m.get("runtime"))
same_runtime=same_maxruntime.get("runtime")
samemovie=[m.get("title")for m in movies if m.get("runtime")==same_runtime]
print(samemovie)

# languages
lanuages=[m.get("language") for m in movies]
lang={l:lanuages.count(l) for l in lanuages}
print(lang)

same_runtime=[m.get("runtime") for m in movies]
same={r:same_runtime.count(r) for r in same_runtime}
print(same)