import random, time

address = [
    "350 Diamond Ave. Greenville, NC 27834",
    "79 Queen St. The Villages, FL 32162",
    "9051 Anderson St. Saint Cloud, MN 56301",
    "393 Jade Drive Lakeland, FL 33801",
    "312 Purple Finch Dr. Port Charlotte, FL 33952",
    "262 Andover Road Ottumwa, IA 52501",
    "188 Amerige Road Vicksburg, MS 39180",
    "639 Grime St. Bemidji, MN 56601",
    "161 Judge Dr. Ridgefield, CT 06877",
    "8214 East Windsor St. San Carlos, CA 94070",
    "9233 Hill Field Ave. Moses Lake, WA 98837",
    "8839 Hill Field Ave. Lawrenceville, GA 30043",
    "22 Amherst Street Lynn, MA 01902",
    "7913 Tallwood Street Brunswick, GA 31525",
    "18 Devonshire Lane Stamford, CT 06902",
    "128 Jefferson St. Brookline, MA 02446",
    "7027 Rock Maple St. Bemidji, MN 56601",
    "9623 Ocean Dr. Woodbridge, VA 22191",
    "40 N. Summit Dr. Hightstown, NJ 08520",
    "7957 Crown Drive Syosset, NY 11791",
]
starName = [
    "Dewey Rodgers",
    "Erick Adams",
    "Margaret Fernandez",
    "Angelo Mcdaniel",
    "Christy Munoz",
    "Paul Fletcher",
    "Lee Figueroa",
    "Jacob Harvey",
    "Jose Warren",
    "Adam Farmer",
    "Jeannie Ortiz",
    "Valerie Ballard",
    "Jimmie Walters",
    "Katie Stephens",
    "Marc Norris",
    "Eloise Copeland",
    "Perry Cortez",
    "Fredrick Webb",
    "Robyn Armstrong",
    "Noel Stevenson",
    "Brad Simmons",
    "Molly Steele",
    "Dexter Abbott",
    "Gordon Townsend",
    "Meryl Streep",
]
studioName = [
    "conefind",
    "Overkix",
    "Doubletechi",
    "retrans",
    "Duolab",
    "MGM",
    "Volttechi",
    "Lain",
    "lanetrans",
    "Namstrip",
]
movieName = [
    "Foe Of The South",
    "Woman Of The East",
    "Rat Of Wood",
    "Stranger Without A Home",
    "Strangers Of The West",
    "Descendants Of The Sea",
    "Snakes And Gangsters",
    "Men And Spies",
    "Castle Of Gold",
    "Future Of Time",
    "Scared At The Mist",
    "Prepare For The Ships",
    "Bat Looking At Me",
    "Monster With A Smile",
    "Guests Behind The Door",
    "Visitors During Full Moon",
    "Strangers And Horses",
    "Hunters And Rats",
    "Hidden In My Street",
    "Lost In My Dreams",
    "Surviving The Sea",
    "Somber Until The Maze",
    "Martian Of The Dead",
    "Enemy Of The Fallen",
    "Mercenaries With A Spaceship",
    "Armies Of Darkness",
    "Rebels And Figures",
    "Friends And Rebels",
    "Demise Of Moondust",
    "Obliteration Of Time",
    "Caution Of My Android Servant",
    "Colors Of Time Travel",
]

movieExecName = [
    "Andrew Daniel",
    "Clifton Clark",
    "Virgil Lynch",
    "Theodore Roberts",
    "Joe Fox",
    "Franklin Greene",
    "Corey Chapman",
    "Erik Spears",
    "Justin Osborne",
    "Nicolas Lowe",
    "Bernice Holt",
    "Daisy Hess",
    "Naomi Gentry",
    "Kathryn McPherson",
    "Doris Osborn",
    "Arlene Moses",
    "Alicia Lindsay",
    "Paula Gamble",
    "Christina Patterson",
    "Hailey Bridges",
]

certNumbers = [
    "wrs8dCeSUrRMy",
    "SQkhJHphSLFzy",
    "Q5Dv5SCX8eTmq",
    "Za2dABbwLZm9c",
    "ESnpmwrcdpZjF",
    "Xcvzde37QNrtv",
    "RVa5PF5dVxCV9",
    "pySugX9zMrFBm",
    "3GYhUkDymkGHN",
    "AAPsELVeY27C6",
    "hLqCjfkZPs9SR",
    "VxwcmdwxPgHrW",
    "J4qdjcc9mNLMr",
    "dD7Dtpa4pX8jE",
    "tkkvNfhvWU3Uf",
    "qx5hPbNZBFg4A",
    "fQyjTYbzSKLpz",
    "xWZekGFaEfZCV",
    "qvK6gmKJKWRzq",
    "G3YYDaYRARexT",
]

movieGenre = [
    "Romance",
    "Criminal",
    "Sci-fi",
    "Western",
    "Thriller",
    "Animation",
    "War",
    "Action",
    "Adventure",
    "Drama",
    "Disaster",
]

def random_year():
    return str(random.choice(range(1950, 2017)))

def random_networth():
    return random.choice(range(1, 100)) * 100000

def random_date(start, end, format = '%m/%d/%Y'):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    prop = random.random()

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))