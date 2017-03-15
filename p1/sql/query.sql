-- Q1
SELECT movieTitle, movieYear
FROM Movies m NATURAL JOIN Stars
WHERE starName = 'Meryl Streep';

-- Q2
SELECT m.studioName, m.movieTitle, m.movieYear
FROM Movies m
WHERE m.length = (
  SELECT MAX(length)
  FROM Movies m2
  WHERE m2.studioName = m.studioName
);

--- Q3
SELECT me.name
FROM MovieExec me
WHERE me.networth = (
  SELECT MAX(me2.networth)
  FROM MovieExec me2, Movies m
  WHERE me2.certN = m.pruducerCN
  AND m.studioName = 'MGM'
);

--- Q4
SELECT DISTINCT s.starName
FROM Stars s NATURAL JOIN MovieStar ms
WHERE NOT EXISTS (
  SELECT *
  FROM Stars s2 NATURAL JOIN Movies m NATURAL JOIN Stud st
  WHERE s2.starName = ms.starName
  AND ms.address != st.address
);

-- Q5
SELECT DISTINCT s.starName
FROM Stars s
WHERE NOT EXISTS (
  SELECT * FROM Movies m
  WHERE m.studioName = "MGM"
  AND NOT EXISTS(
    SELECT * FROM Stars s2
    WHERE m.movieYear = s2.movieYear
    AND m.movieTitle = s2.movieTitle
    AND s2.starName = s.starName
  )
);
