### Topic 1: SELECT + FROM

This is how you fetch data from a table.
sql

\\ SELECT * FROM students; - print the whole student table \\

(for specific name and marks )

SELECT name, marks FROM students; 

# What just happened:

SELECT * → fetch all columns , SELECT name, marks - fetch all name and marks cloumn
FROM students → from this table


### Topic 2: Where

Filters rows based on a condition. Like df[df['marks'] > 80] in pandas.

\\ SELECT * FROM students
WHERE marks > 80; \\

 output;- 
"id"	"name"	"age"	"city"	"marks"
1	"Rahul"	20	"Delhi"	85
2	"Priya"	21	"Mumbai"	92
4	"Sneha"	22	"Bangalore"	95
6	"Ananya"	21	"Delhi"	88

# WHERE supports these operators:

= → equal
!= or <> → not equal
> < >= <= → comparison
AND OR → multiple conditions


### Topic 3: ORDER BY

Sorts your results. Like df.sort_values() in pandas.

\\ SELECT * FROM students
ORDER BY marks DESC; \\

DESC = highest first
ASC = lowest first (default)

 output;-
"id"	"name"	"age"	"city"	"marks"
4	"Sneha"	22	"Bangalore"	95
2	"Priya"	21	"Mumbai"	92
6	"Ananya"	21	"Delhi"	88
1	"Rahul"	20	"Delhi"	85
5	"Vikram"	23	"Chennai"	78
3	"Arjun"	19	"Kolkata"	72


### Topic 4: LIMIT

Fetches only top N rows. Useful when tables have millions of rows.

\\ SELECT * FROM students
ORDER BY marks DESC
LIMIT 3; \\

 output;-
"id"	"name"	"age"	"city"	"marks"
4	"Sneha"	22	"Bangalore"	95
2	"Priya"	21	"Mumbai"	92
6	"Ananya"	21	"Delhi"	88


### Topic 5: DISTINCT

Removes duplicate values. Like df['city'].unique() in pandas.

\\ SELECT DISTINCT city FROM students; \\

 output;-
"city"
"Delhi"
"Mumbai"
"Bangalore"
"Kolkata"
"Chennai"

# Note:
DISTINCT applies to the whole row, not just one column.
So SELECT DISTINCT city, name gives unique (city + name) combinations, not just unique cities.


### Topic 6: Aggregate Functions

These calculate something across rows.

COUNT → total rows
SUM → total of a column
AVG → average
MIN → lowest value
MAX → highest value

\\ SELECT COUNT(*) FROM students;
SELECT AVG(marks) FROM students; \\

 output;-
COUNT(*) → 6
AVG(marks) → 85.00

# All at once:
\\ SELECT COUNT(*), SUM(marks), AVG(marks), MIN(marks), MAX(marks) FROM students; \\

COUNT(*)	SUM(marks)	AVG(marks)	MIN(marks)	MAX(marks)
6		510		85.00		72		95

# Note:
COUNT(*) counts all rows. COUNT(column) skips NULL values in that column.
Always remember that — it's a common bug source.


### Topic 7: GROUP BY

Groups rows and applies aggregate per group. Like df.groupby() in pandas.

\\ SELECT city, COUNT(*) 
FROM students
GROUP BY city; \\

 output;-
"city"		"COUNT(*)"
"Delhi"		2
"Mumbai"	1
"Bangalore"	1
"Kolkata"	1
"Chennai"	1

# Another example — avg marks per city:
\\ SELECT city, AVG(marks)
FROM students
GROUP BY city; \\

"city"		"AVG(marks)"
"Delhi"		86.50
"Mumbai"	92.00
"Bangalore"	95.00
"Kolkata"	72.00
"Chennai"	78.00

# Note:
Every column in SELECT must either be in GROUP BY or inside an aggregate function.
Writing SELECT name, city ... GROUP BY city will throw an error.

# Tip:
AVG often gives long decimals. Wrap it with ROUND() to clean it up.
\\ SELECT city, ROUND(AVG(marks), 2)
FROM students
GROUP BY city; \\
The 2 means 2 decimal places.


### Topic 8: HAVING

Filters groups after GROUP BY. WHERE filters rows, HAVING filters groups.

WHERE → filters rows before grouping
HAVING → filters groups after grouping

\\ SELECT city, COUNT(*)
FROM students
GROUP BY city
HAVING COUNT(*) > 1; \\

 output;-
"city"		"COUNT(*)"
"Delhi"		2

# Note:
You can't use WHERE to filter on aggregate results like COUNT or AVG.
That's exactly what HAVING is for.

When you use GROUP BY — you can only SELECT:

the column you grouped by (city)
aggregate functions (AVG, COUNT, MAX etc.)

\\ -- Wrong ✗
SELECT city, COUNT(*) FROM students
WHERE COUNT(*) > 1
GROUP BY city;

-- Correct ✓
SELECT city, COUNT(*) FROM students
GROUP BY city
HAVING COUNT(*) > 1; \\


### Topic 9: LIKE

Pattern matching on text columns.

% → any number of characters
_ → exactly one character

\\ SELECT * FROM students
WHERE name LIKE 'A%'; \\

 output;-
"id"	"name"	"age"	"city"	"marks"
6	"Ananya"	21	"Delhi"	88
3	"Arjun"	19	"Kolkata"	72

# More patterns:
LIKE 'A%'   → starts with A
LIKE '%a'   → ends with a
LIKE '%an%' → contains "an" anywhere
LIKE '_r%'  → second letter is r  (Priya, Arjun)

# Note:
LIKE is case-insensitive in most databases (PostgreSQL is strict — use ILIKE there instead).


### Topic 10: IN and BETWEEN

IN — match multiple values, cleaner than multiple OR conditions

\\ SELECT * FROM students
WHERE city IN ('Delhi', 'Mumbai'); \\

 output;-
"id"	"name"	"age"	"city"	"marks"
1	"Rahul"	20	"Delhi"	85
2	"Priya"	21	"Mumbai"	92
6	"Ananya"	21	"Delhi"	88

BETWEEN — range filter (inclusive on both ends)

\\ SELECT * FROM students
WHERE marks BETWEEN 80 AND 90; \\

 output;-
"id"	"name"	"age"	"city"	"marks"
1	"Rahul"	20	"Delhi"	85
6	"Ananya"	21	"Delhi"	88

# Note:
IN is just a cleaner way to write multiple OR conditions.
WHERE city IN ('Delhi', 'Mumbai') = WHERE city = 'Delhi' OR city = 'Mumbai'

BETWEEN 80 AND 90 includes both 80 and 90. Not like Python's range() which excludes the end.
You can also use NOT IN and NOT BETWEEN to exclude ranges.


##### --------------------- #####

imp. 

1 - Use AND to combine two conditions: `WHERE marks BETWEEN 85 AND 95 AND city IN ('Delhi', 'Bangalore')`

