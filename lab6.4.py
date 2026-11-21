champions = {
    "Brazil": [2002, 1970, 1958, 1994, 1962],
    "England": [1966],
    "Italy": [2006, 1934, 1982, 1938],
    "Spain": [2010],
    "Germany": [1990, 1954, 2014, 1974],
    "France": [2018, 1998],
    "Uruguay": [1950, 1930],
    "Argentina": [1986, 1978]
}
for country in champions:
    champions[country].sort()
print(champions)