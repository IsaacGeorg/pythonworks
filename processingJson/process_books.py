from json import load
f=open("D:/vs code/Pythonworks/Datasets_ for_file_Operations/books.json")

data=load(f)

all_titles=[book.get("title") for book in data]
# print(all_titles)

page_filter=[book.get("title") for book in data if book.get("pages")<250]
# print(page_filter)

fiction_filter=[book.get("title") for book in data if book.get("genre")=="Fiction"]
# print(fiction_filter)

# print all genres
all_genres=[book.get("genre") for book in data]
# print(set(all_genres))



genre_count={genre:all_genres.count(genre) for genre in all_genres}
# print(genre_count)


# print costly book
costly=max(data,key=lambda d:d.get("price"))
# print(costly)


# Author with more than one book
authors=[book.get("author") for book in data]
author_count={i:authors.count(i) for i in authors}
count=[k for k,v in author_count.items() if v>1]
print(count)