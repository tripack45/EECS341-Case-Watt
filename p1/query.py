import sqlite3


dbfile = "mss.sqlite3"

queries = [
    "SELECT movieTitle, movieYear\n"
    "FROM Movies m NATURAL JOIN Stars\n"
    "WHERE starName = ?;",

    "SELECT m.studioName, m.movieTitle, m.movieYear\n"
    "FROM Movies m\n"
    "WHERE m.length = (\n"
    "  SELECT MAX(length)\n"
    "  FROM Movies m2\n"
    "  WHERE m2.studioName = m.studioName\n"
    ");",

    "SELECT me.name\n"
    "FROM MovieExec me\n"
    "WHERE me.networth = (\n"
    "  SELECT MAX(me2.networth)\n"
    "  FROM MovieExec me2, Movies m\n"
    "  WHERE me2.certN = m.pruducerCN\n"
    "  AND m.studioName = ?\n"
    ");",

    "SELECT DISTINCT s.starName\n"
    "FROM Stars s NATURAL JOIN MovieStar ms\n"
    "WHERE NOT EXISTS (\n"
    "  SELECT *\n"
    "  FROM Stars s2 NATURAL JOIN Movies m NATURAL JOIN Stud st\n"
    "  WHERE s2.starName = ms.starName\n"
    "  AND ms.address != st.address\n"
    ");",

    "SELECT DISTINCT s.starName\n"
    "FROM Stars s\n"
    "WHERE NOT EXISTS (\n"
    "  SELECT * FROM Movies m\n"
    "  WHERE m.studioName = 'MGM'\n"
    "  AND NOT EXISTS(\n"
    "    SELECT * FROM Stars s2\n"
    "    WHERE m.movieYear = s2.movieYear\n"
    "    AND m.movieTitle = s2.movieTitle\n"
    "    AND s2.starName = s.starName\n"
    "  )\n"
    ");",
]

def print_table(table):
    col_width = [max(len(x) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i]) for i, x in enumerate(line)) + " |")



with sqlite3.connect("mss.sqlite3") as con:
    c = con.cursor()

    q1_name = 'Meryl Streep'
    q3_studio = 'MGM'

    param = [(q1_name,), (), (q3_studio,), (), ()]

    for i in range(5):
        print("===== Executing Q%d =====:" % (i + 1))
        print('Parameters:')
        print(param[i])
        print('Query:')
        print(queries[i])
        c.execute(queries[i], param[i])
        result = c.fetchall()
        print("===== Suceeded, Results: ====")
        print_table(result)
        print("\n")