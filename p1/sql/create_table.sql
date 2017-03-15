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
