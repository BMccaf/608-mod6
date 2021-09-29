In [1]: import sqlite3

In [2]: connection = sqlite3.connect('books.db')

In [3]: import pandas as pd

In [4]: pd.options.display.max_columns = 10

In [5]: pd.read_sql('SELECT * FROM authors', connection,
   ...:             index_col=['id'])
Out[5]:
        first    last
id
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel
4         Dan   Quirk
5   Alexander    Wald

In [6]:

In [6]: pd.read_sql('SELECT * FROM titles', connection)
Out[6]:
         isbn                             title  edition copyright
0  0135404673     Intro to Python for CS and DS        1      2020
1  0132151006     Internet & WWW How to Program        5      2012
2  0134743350               Java How to Program       11      2018
3  0133976890                  C How to Program        8      2016
4  0133406954  Visual Basic 2012 How to Program        6      2014
5  0134601548          Visual C# How to Program        6      2017
6  0136151574         Visual C++ How to Program        2      2008
7  0134448235                C++ How to Program       10      2017
8  0134444302            Android How to Program        3      2017
9  0134289366         Android 6 for Programmers        3      2016

In [7]: df = pd.read_sql('SELECT * FROM author_ISBN', connection)

In [8]: df.head()
Out[8]:
   id        isbn
0   1  0134289366
1   2  0134289366
2   5  0134289366
3   1  0135404673
4   2  0135404673

In [9]: pd.read_sql('SELECT first, last FROM authors', connection)
Out[9]:
       first    last
0       Paul  Deitel
1     Harvey  Deitel
2      Abbey  Deitel
3        Dan   Quirk
4  Alexander    Wald

In [10]: pd.read_sql("""SELECT title, edition, copyright
    ...:                FROM titles
    ...:                WHERE copyright > '2016'""", connection)
Out[10]:
                           title  edition copyright
0  Intro to Python for CS and DS        1      2020
1            Java How to Program       11      2018
2       Visual C# How to Program        6      2017
3             C++ How to Program       10      2017
4         Android How to Program        3      2017

In [11]: pd.read_sql("""SELECT id, first, last
    ...:                FROM authors
    ...:                WHERE last LIKE 'D%'""",
    ...:                connection, index_col=['id'])
Out[11]:
     first    last
id
1     Paul  Deitel
2   Harvey  Deitel
3    Abbey  Deitel

In [12]: pd.read_sql("""SELECT id, first, last
    ...:                FROM authors
    ...:                WHERE first LIKE '_b%'""",
    ...:             connection, index_col=['id'])
Out[12]:
    first    last
id
3   Abbey  Deitel

In [13]: pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
Out[13]:
                              title
0         Android 6 for Programmers
1            Android How to Program
2                  C How to Program
3                C++ How to Program
4     Internet & WWW How to Program
5     Intro to Python for CS and DS
6               Java How to Program
7  Visual Basic 2012 How to Program
8          Visual C# How to Program
9         Visual C++ How to Program

In [14]: pd.read_sql("""SELECT id, first, last
    ...:                FROM authors
    ...:                ORDER BY last, first""",
    ...:             connection, index_col=['id'])
Out[14]:
        first    last
id
3       Abbey  Deitel
2      Harvey  Deitel
1        Paul  Deitel
4         Dan   Quirk
5   Alexander    Wald

In [15]: pd.read_sql("""SELECT id, first, last
    ...:                FROM authors
    ...:                ORDER BY last DESC, first ASC""",
    ...:             connection, index_col=['id'])
Out[15]:
        first    last
id
5   Alexander    Wald
4         Dan   Quirk
3       Abbey  Deitel
2      Harvey  Deitel
1        Paul  Deitel

In [16]: pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection)
Out[16]:
         isbn                             title  edition copyright
0  0134444302            Android How to Program        3      2017
1  0133976890                  C How to Program        8      2016
2  0134448235                C++ How to Program       10      2017
3  0132151006     Internet & WWW How to Program        5      2012
4  0134743350               Java How to Program       11      2018
5  0133406954  Visual Basic 2012 How to Program        6      2014
6  0134601548          Visual C# How to Program        6      2017
7  0136151574         Visual C++ How to Program        2      2008
