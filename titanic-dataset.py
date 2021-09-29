In [1]: import pandas as pd

In [2]: titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
   ...:     'Rdatasets/csv/carData/TitanicSurvival.csv')

In [3]: pd.set_option('precision', 2)  # format for floating-point values

In [4]: titanic.head()
Out[4]:
                        Unnamed: 0 survived     sex    age passengerClass
0    Allen, Miss. Elisabeth Walton      yes  female  29.00            1st
1   Allison, Master. Hudson Trevor      yes    male   0.92            1st
2     Allison, Miss. Helen Loraine       no  female   2.00            1st
3  Allison, Mr. Hudson Joshua Crei       no    male  30.00            1st
4  Allison, Mrs. Hudson J C (Bessi       no  female  25.00            1st

In [5]: titanic.tail()
Out[5]:
                     Unnamed: 0 survived     sex   age passengerClass
1304       Zabour, Miss. Hileni       no  female  14.5            3rd
1305      Zabour, Miss. Thamine       no  female   NaN            3rd
1306  Zakarian, Mr. Mapriededer       no    male  26.5            3rd
1307        Zakarian, Mr. Ortin       no    male  27.0            3rd
1308         Zimmerman, Mr. Leo       no    male  29.0            3rd

In [6]: titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

In [7]: titanic.head()
Out[7]:
                              name survived     sex    age class
0    Allen, Miss. Elisabeth Walton      yes  female  29.00   1st
1   Allison, Master. Hudson Trevor      yes    male   0.92   1st
2     Allison, Miss. Helen Loraine       no  female   2.00   1st
3  Allison, Mr. Hudson Joshua Crei       no    male  30.00   1st
4  Allison, Mrs. Hudson J C (Bessi       no  female  25.00   1st

In [8]: titanic.describe()
Out[8]:
           age
count  1046.00
mean     29.88
std      14.41
min       0.17
25%      21.00
50%      28.00
75%      39.00
max      80.00

In [9]: (titanic.survived == 'yes').describe()
Out[9]:
count      1309
unique        2
top       False
freq        809
Name: survived, dtype: object

In [10]: %matplotlib
Using matplotlib backend: Qt5Agg

In [11]: histogram = titanic.hist()
