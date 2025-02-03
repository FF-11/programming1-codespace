movies = [{'title': ..., 'genre': ..., 'rating': ..., ...}]

def start(genre, rating):
    out = []
    for i in movies:
        if i['genre'] == genre and i['rating'] >= rating:
            out.append(i)
    if out == []:
        out.append(max(movies, key = lambda x: x['rating']))
    print(out)
