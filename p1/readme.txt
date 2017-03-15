This is project part1 for EECS341 database.
This assignment is done by YAO Yue [yxy686]

The code is written in python and should run properly under python 3.5
DBMS is sqlite, since the database is more "portable", easier to grade.

==============================================
======== Files and their contents ============
==============================================

---- p1/
   |---- query.py : Code that executes the queries
   |
   |---- rangen.py : Code that generates fake data and populates the database
   |
   |---- data.py : Code supporting rangen.py
   |
   |---- mss.sqlite3 : The database file
   |
   |---- sql/
       |---- query.sql : SQL file containing the query being executed
       |
       |---- create_table.sql: SQL file contains database schema. It's concent is also paste below

================================================
============== Database Schema =================
================================================
-- Following is content of file sql/create_table.sql
CREATE TABLE MovieExec (
  name  CHAR(20) PRIMARY KEY,
  certN CHAR(20) UNIQUE NOT NULL,
  address TEXT,
  networth INT
);

CREATE TABLE Stud (
  studioName  CHAR(20) PRIMARY KEY,
  address     TEXT,
  presCN      CHAR(20)
);

CREATE TABLE Movies (
  movieTitle  CHAR(30),
  movieYear   CHAR(10),
  length      INT,
  genre       CHAR(15),
  studioName  CHAR(20) REFERENCES Stud(studioName),
  pruducerCN  CHAR(20),
  PRIMARY KEY (movieTitle, movieYear)
);

CREATE TABLE MovieStar (
  starName  CHAR(20) PRIMARY KEY,
  address   TEXT,
  gender    CHAR(10),
  birthdate  CHAR(20)
);

CREATE TABLE Stars (
  movieTitle  CHAR(30) REFERENCES Movies(movieTitle) ON DELETE CASCADE,
  movieYear   CHAR(10) REFERENCES Movies(movieYear) ON DELETE CASCADE,
  starName    CHAR(20) REFERENCES MovieStar(starName) ON DELETE CASCADE,
  PRIMARY KEY (movieTitle, movieYear, starName)
);


================================================
========== Queries and their outputs ===========
================================================
* Following is the output of query.py

===== Executing Q1 =====:
Parameters:
('Meryl Streep',)
Query:
SELECT movieTitle, movieYear
FROM Movies m NATURAL JOIN Stars
WHERE starName = ?;
===== Suceeded, Results: ====
| Foe Of The South  II            | 2011 |
| Rat Of Wood  III                | 1990 |
| Strangers Of The West  II       | 2003 |
| Men And Spies  II               | 1977 |
| Prepare For The Ships  II       | 1978 |
| Bat Looking At Me  II           | 2002 |
| Monster With A Smile I          | 2015 |
| Lost In My Dreams I             | 1995 |
| Lost In My Dreams  III          | 1952 |
| Somber Until The Maze I         | 1984 |
| Friends And Rebels  II          | 1962 |
| Obliteration Of Time I          | 2005 |
| Caution Of My Android Servant I | 2016 |


===== Executing Q2 =====:
Parameters:
()
Query:
SELECT m.studioName, m.movieTitle, m.movieYear
FROM Movies m
WHERE m.length = (
  SELECT MAX(length)
  FROM Movies m2
  WHERE m2.studioName = m.studioName
);
===== Suceeded, Results: ====
| Namstrip    | Foe Of The South  III     | 1950 |
| Duolab      | Snakes And Gangsters  II  | 1968 |
| Lain        | Men And Spies  II         | 1977 |
| Doubletechi | Scared At The Mist I      | 2014 |
| lanetrans   | Monster With A Smile I    | 2015 |
| Volttechi   | Monster With A Smile  III | 1968 |
| retrans     | Hidden In My Street  III  | 2013 |
| conefind    | Surviving The Sea  III    | 2012 |
| MGM         | Armies Of Darkness  II    | 1981 |
| Overkix     | Rebels And Figures  III   | 1995 |


===== Executing Q3 =====:
Parameters:
('MGM',)
Query:
SELECT me.name
FROM MovieExec me
WHERE me.networth = (
  SELECT MAX(me2.networth)
  FROM MovieExec me2, Movies m
  WHERE me2.certN = m.pruducerCN
  AND m.studioName = ?
);
===== Suceeded, Results: ====
| Erik Spears |


===== Executing Q4 =====:
Parameters:
()
Query:
SELECT DISTINCT s.starName
FROM Stars s NATURAL JOIN MovieStar ms
WHERE NOT EXISTS (
  SELECT *
  FROM Stars s2 NATURAL JOIN Movies m NATURAL JOIN Stud st
  WHERE s2.starName = ms.starName
  AND ms.address != st.address
);
===== Suceeded, Results: ====
| Erick Adams   |
| Christy Munoz |


===== Executing Q5 =====:
Parameters:
()
Query:
SELECT DISTINCT s.starName
FROM Stars s
WHERE NOT EXISTS (
  SELECT * FROM Movies m
  WHERE m.studioName = 'MGM'
  AND NOT EXISTS(
    SELECT * FROM Stars s2
    WHERE m.movieYear = s2.movieYear
    AND m.movieTitle = s2.movieTitle
    AND s2.starName = s.starName
  )
);
===== Suceeded, Results: ====
| Perry Cortez   |
| Noel Stevenson |