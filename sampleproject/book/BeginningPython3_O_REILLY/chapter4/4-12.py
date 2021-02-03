movies = {}
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A num turns into a monster', 'A haunted yarn shop']

for title, plot in zip(titles, plots) :
    movies[title] = plot

print(movies)