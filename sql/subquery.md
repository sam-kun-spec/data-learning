
## Subquery

Subquery = a query inside another query.
Think of it like this — instead of doing two separate queries, you nest one inside the other.

---

### Example — two separate queries:

```sql
-- step 1: find average marks
SELECT AVG(marks) FROM students;
-- result: 83.17

-- step 2: find students above average
SELECT * FROM students WHERE marks > 83.17;
```

### Same thing as one query using subquery:

```sql
SELECT * FROM students
WHERE marks > (SELECT AVG(marks) FROM students);
```

imp. The inner query `(SELECT AVG(marks) FROM students)` runs first, returns 83.17, then the outer query uses that value.

---

## Subquery in FROM

Inner query returns a full table → you give it a temp name → outer query treats it like a normal table and filters it.

```sql
SELECT * FROM (
    SELECT gender, math_score,
    RANK() OVER (PARTITION BY gender ORDER BY math_score DESC) AS row_rank
    FROM student_performance
) AS ranked
WHERE row_rank = 1;
```

**Simple analogy:**
```sql
-- Normal FROM:
SELECT * FROM students              ← real table

-- Subquery in FROM:
SELECT * FROM (SELECT ...) AS temp  ← temporary table created on the fly
```

imp. The `AS ranked` part is mandatory — you must give the temp table a name, otherwise SQL throws an error.

---

## Why use subquery in FROM?

Because sometimes you need to filter on a calculated column that doesn't exist in the original table.

`row_rank` doesn't exist in `student_performance` — you created it using a window function. So you can't do this:

```sql
SELECT gender, math_score,
RANK() OVER (...) AS row_rank
FROM student_performance
WHERE row_rank = 1;  -- ERROR: row_rank doesn't exist yet
```

**SQL execution order:**
```
1. FROM
2. WHERE
3. SELECT  ← window functions run here
```

WHERE runs before SELECT — so `row_rank` doesn't exist yet when WHERE tries to use it.

Solution — wrap it in a subquery, make `row_rank` exist first, then filter.

imp. This is one of the most common patterns in real SQL work. You'll use it a lot.
