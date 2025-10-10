# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/movie.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and actors/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

movie_db: List[Tuple[str, str, int, List[str]]] = [
     (
        "tom sawyer",  # title
        "mark twain",  # author
        1876,  # year
        ["tom sawyer", 
         "huckleberry finn", 
         "aunt polly", 
         "becky thatcher"
         ],  # characters
    ),
    (
        "sense and sensibility",
        "jane austen",
        1811,
        ["elinor dashwood", 
         "marianne dashwood", 
         "edward ferrars", 
         "colonel brandon"
         ],
    ),
    (
        "pride and prejudice",
        "jane austen",
        1813,
        ["elizabeth bennet", 
         "mr. darcy", 
         "jane bennet", 
         "mr. bingley"
         ],
    ),
    (
        "moby-dick",
        "herman melville",
        1851,
        ["ishmael", 
         "captain ahab", 
         "queequeg", 
         "starbuck"
         ],
    ),
    (
        "jane eyre",
        "charlotte brontë",
        1847,
        ["jane eyre", 
         "mr. rochester", 
         "st. john rivers", 
         "mrs. reed"
         ],
    ),
    (
        "wuthering heights",
        "emily brontë",
        1847,
        ["heathcliff", 
         "catherine earnshaw", 
         "edgar linton", 
         "nelly dean"
         ],
    ),
    (
        "the picture of dorian gray",
        "oscar wilde",
        1890,
        ["dorian gray", 
         "lord henry wotton", 
         "basil hallward", 
         "sibyl vane"
        ],
    ),
    (
        "the adventures of huckleberry finn",
        "mark twain",
        1884,
        ["huckleberry finn", 
         "jim", 
         "tom sawyer", 
         "pap finn"
         ],
    ),
    (
        "great expectations",
        "charles dickens",
        1861,
        ["pip", 
         "estella", 
         "miss havisham", 
         "joe gargery"
         ],
    ),
    (
        "frankenstein",
        "mary shelley",
        1818,
        ["victor frankenstein", 
         "the creature", 
         "elizabeth lavenza", 
         "henry clerval"
         ],
    ),
    (
        "the call of the wild",
        "jack london",
        1903,
        ["buck", 
         "john thornton", 
         "spitz", 
         "francois", 
         "perrault"
         ],
    ),
    (
        "the wonderful wizard of oz",
        "l. frank baum",
        1900,
        ["dorothy", 
         "toto", 
         "scarecrow", 
         "tin man", 
         "cowardly lion"
         ],
    ),
    (
        "anne of green gables",
        "lucy maud montgomery",
        1908,
        ["anne shirley", 
         "matthew cuthbert", 
         "marilla cuthbert", 
         "diana barry"
         ],
    ),
    (
        "winnie-the-pooh",
        "a. a. milne",
        1926,
        ["winnie-the-pooh", 
         "christopher robin", 
         "piglet", 
         "eyore", 
         "tigger"
         ],
    ),
    (
        "lord of the flies",
        "william golding",
        1954,
        ["ralph", 
         "piggy", 
         "jack merridew", 
         "simon", 
         "roger"
         ],
    ),
    (
        "to kill a mockingbird",
        "harper lee",
        1960,
        ["scout finch",
          "jem finch", 
          "atticus finch", 
          "tom robinson", 
         "bob ewell"
         ],
    ),
    (
        "animal farm",
        "george orwell",
        1945,
        ["napoleon", 
         "snowball", 
         "boxer", 
         "squealer", 
         "old major"
         ],
    ),
    (
        "1984",
        "george orwell",
        1949,
        ["winston smith", 
         "julia", 
         "big brother", 
         "o'Brien", 
         "syme"
         ],
    ),
    (
        "the great gatsby",
        "f. scott fitzgerald",
        1925,
        ["jay gatsby", 
         "nick carraway", 
         "daisy buchanan", 
         "tom buchanan", 
         "jordan baker"
         ],
    ),
    (
        "brave new world",
        "aldous huxley",
        1932,
        ["bernard marx", 
         "lenina crowne", 
         "mustapha mond", 
         "john",
         "the savage", 
         "helmholtz watson"],
    ),
    (
        "ulysses",
        "james joyce",
        1922,
        ["levy bloom", 
         "stephen dedalus", 
         "molloy", 
         "blazes boylan"
         ], 
    ),
    (
        "pride and prejudice",  
        "jane austen",
        1813,  
        ["elizabeth bennet", 
         "mr darcy", 
         "jane bennet", 
         "mrs bennet"
         ],
    ),
    (
        "the catcher in the rye",
        "j. d. salinger",
        1951,
        ["holden caulfield", 
         "phoebe caulfield", 
         "mr antolini", 
         "stradlater", 
         "ackley"],
    ),
    (
        "lord jim",
        "joseph conrad",
        1900,
        ["jim", 
         "marlow", 
         "stevens", 
         "cornelius"],
    ),
    (
        "the sound and the fury",
        "william faulkner",
        1929,
        ["benjy compson", 
         "quentin compson", 
         "caddy compson", 
         "jason compson"
         ],
    ),
    (
        "their eyes were watching god",
        "zora neale hurston",
        1937,
        ["janie crawford", 
         "tea cake woods", 
         "phoeby watson", 
         "logan killicks"
         ],
    ),
    (
        "gone with the wind",
        "margaret mitchell",
        1936,
        ["scarlett o'hara", 
         "rhett butler", 
         "ashley wilkes", 
         "melanie hamilton"
         ],
    ),
    (
        "one hundred years of solitude",
        "gabriel garcía márquez",
        1967,
        ["josé arcadio buendía", 
         "ursula iguarán", 
         "amáranta", 
         "remedios the beauty", 
         "aureliano buendía"
         ],
    ),
    (
        "fahrenheit 451",
        "ray bradbury",
        1953,
        ["guy montag", 
         "mildred montag", 
         "captain beatty", 
         "clarisse mcclellan"
         ],
    ),
    (
        "heart of darkness",
        "joseph conrad",
        1902,
        ["charlie marlow", 
         "kurtz", 
         "the manager", 
         "the helmsman"
         ],
    ),
 
]