from data import address, starName, studioName, movieExecName
from data import certNumbers, movieName, movieGenre
from data import random_year, random_networth, random_date
import sqlite3
import random
import itertools


def generate_data():
    with sqlite3.connect("mss.sqlite3") as con:
        print("Connection successful.")
        c = con.cursor()

        # Populate movie executive
        name_cert = dict(zip(movieExecName, certNumbers))
        for name, cert in name_cert.items():
            add = random.choice(address)
            worth = random_networth()
            c.execute('INSERT INTO MovieExec(name, address, networth, certn) VALUES (?, ?, ?, ?)',
                      (name, add, worth, cert))

        # Populate movie stars
        for name in starName:
            add = random.choice(address)
            gender = random.choice(('Female', 'Male'))
            birthdate = random_date('1/1/1985', '1/1/2007')
            c.execute('INSERT INTO MovieStar(starName, address, gender, birthdate) VALUES (?, ?, ?, ?)',
                      (name, add, gender, birthdate))

        # Populate Stud
        for name, cert in dict(zip(studioName, random.sample(certNumbers, 10))).items():
            add = random.choice(address)
            c.execute('INSERT INTO Stud(studioName, address, presCN) VALUES (?, ?, ?)',
                      (name, add, cert))

        # Populate Movies
        mname = itertools.product(movieName, [' I', '  II', '  III'])
        movie = []
        for title, ver in mname:
            t = title + ver
            year = random_year()
            movie.append((t, year))
            length = random.randint(45, 120) * 60
            genre = random.choice(movieGenre)
            stud = random.choice(studioName)
            producer = random.choice(certNumbers)
            c.execute('INSERT INTO Movies(movieTitle, movieYear, length, genre, studioName, pruducerCN)'
                      'VALUES (?, ?, ?, ?, ?, ?)',
                      (t, year, length, genre, stud, producer))

        # Populate Stars
        for title, year in movie:
            num_of_star = random.randint(1, 4)
            stars = random.sample(starName, num_of_star)
            for star in stars:
                c.execute('INSERT INTO Stars(movieTitle, movieYear, starName)'
                          'VALUES (?, ?, ?)',
                          (title, year, star))

generate_data()



