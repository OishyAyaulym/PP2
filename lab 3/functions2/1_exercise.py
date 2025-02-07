def smth(a):
    return a["imdb"]>5.5
movies = {
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}
print(smth(movies))