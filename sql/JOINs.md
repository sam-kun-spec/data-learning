
## Topic 1: INNER JOIN

Returns only rows that **match in BOTH tables**.

```sql
SELECT students.name, courses.course, courses.grade
FROM students
INNER JOIN courses ON students.id = courses.student_id;
```

imp. Only matching rows appear — if a student has no course, they won't show up.

---

### Example

**students table**
| id | name   |
|----|--------|
| 1  | Rahul  |
| 2  | Priya  |
| 3  | Arjun  |
| 4  | Sneha  |
| 5  | Rohan  |
| 6  | Ananya |

**courses table**
| student_id | course  |
|------------|---------|
| 1          | Math    |
| 2          | Science |
| 3          | Math    |
| 5          | English |
| 7          | Science |

JOIN connects these two tables using `students.id = courses.student_id`.
Think of it like a pandas merge — `df1.merge(df2, on='id')`.

**Output of INNER JOIN:**
| name  | course  |
|-------|---------|
| Rahul | Math    |
| Priya | Science |
| Arjun | Math    |
| Rohan | English |

imp. Sneha (id=4) and Ananya (id=6) dropped — no matching course. student_id=7 dropped — no matching student.

---

## Topic 2: LEFT JOIN

Returns **ALL rows from the left table** + matching rows from the right table. No match = NULL.

```sql
SELECT students.name, courses.course
FROM students
LEFT JOIN courses ON students.id = courses.student_id;
```

imp. Every student shows up — even those with no course. Missing course = NULL.

**Output of LEFT JOIN (same tables):**
| name   | course  |
|--------|---------|
| Rahul  | Math    |
| Priya  | Science |
| Arjun  | Math    |
| Sneha  | NULL    |
| Rohan  | English |
| Ananya | NULL    |

imp. student_id=7 still doesn't appear — it's not in the left table (students).

---

OK simple explanation.

---

**INNER JOIN** — only students WHO HAVE a course.
Result: 4 rows (Sneha and Ananya dropped)

**LEFT JOIN** — ALL students, course if they have one, NULL if they don't.
Result: all 6 students show up

```
Rahul   → Math      → A
Priya   → Science   → A+
Arjun   → Math      → B
Sneha   → NULL      → NULL   (no course assigned)
Rohan   → English   → C
Ananya  → NULL      → NULL   (no course assigned)
```

Left table = students → everyone shows up no matter what.
Right table = courses → shows data if match exists, NULL if not.

---

## Topic 3: RIGHT JOIN

Opposite of LEFT JOIN. Returns **ALL rows from the right table** + matching rows from the left. No match = NULL.

```sql
SELECT students.name, courses.course
FROM students
RIGHT JOIN courses ON students.id = courses.student_id;
```

In our case right table = courses → every course row shows up, even student_id=7 which has no student.

**Output of RIGHT JOIN (same tables):**
| name  | course  |
|-------|---------|
| Rahul | Math    |
| Priya | Science |
| Arjun | Math    |
| Rohan | English |
| NULL  | Science |

imp. student_id=7 appears with NULL name — no match in students. Sneha and Ananya don't appear — they have no row in courses (right table drives it now).

Right table = courses → every course shows up no matter what.
Left table = students → shows name if match exists, NULL if not.

---

## Topic 4: FULL OUTER JOIN

Returns **ALL rows from BOTH tables**. NULL where no match on either side.

```sql
SELECT students.name, courses.course
FROM students
FULL OUTER JOIN courses ON students.id = courses.student_id;
```

**Output of FULL OUTER JOIN (same tables):**
| name   | course  |
|--------|---------|
| Rahul  | Math    |
| Priya  | Science |
| Arjun  | Math    |
| Sneha  | NULL    |
| Rohan  | English |
| Ananya | NULL    |
| NULL   | Science |

imp. 7 rows total — all 6 students + student_id=7 from courses. Nobody gets dropped. Missing data fills with NULL on whichever side has no match.

---

### imp. FULL OUTER JOIN — table order doesn't matter

`FROM students FULL OUTER JOIN courses` and `FROM courses FULL OUTER JOIN students` give the **same result** — same 7 rows, just row order may differ.

The table name after JOIN is just "which second table to combine with" — not which one dominates.

Only LEFT JOIN and RIGHT JOIN care about order. FULL OUTER JOIN doesn't.

---
