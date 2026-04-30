
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
