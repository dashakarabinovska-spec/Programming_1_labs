mountains = {
    "Turkul": 1933,
    "Hoverla": 2061,
    "Petros": 2020,
    "Pip Ivan Chernogirsky (Chorna gora)": 2028,
    "Rebra": 2001,
    "Brebenescul": 2032,
    "Gutin Tomnatik": 2016,
    "Munchel": 2001,
    "Dantsish": 1850,
    "Smotrych": 1767
}
result = sorted(mountains.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print(result[i][0] + ": " + str(result[i][1]) + " m")