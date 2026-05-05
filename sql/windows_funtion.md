
## Window Functions

OK from scratch. Simply.

---

Normal SQL — you get one result per group:
```sql
SELECT gender, AVG(math_score)
FROM student_performance
GROUP BY gender;
-- returns 2 rows only
```

Window function — you get result per row + group calculation side by side:
```sql
SELECT gender, math_score,
AVG(math_score) OVER (PARTITION BY gender) AS gender_avg
FROM student_performance;
-- returns all 1000 rows
```

---

**3 keywords to understand:**

`OVER` → tells SQL "this is a window function"

`PARTITION BY` → divide rows into groups (like GROUP BY but rows don't collapse)

`AS` → just rename the output column (nothing special)

---

**Real analogy:**

You have a class of 1000 students. You want to see each student's mark + their gender's average mark on the same line.

GROUP BY can't do this — it removes individual rows.
Window function keeps every student + adds the group average next to them.

---

imp. `OVER()` = window function. Everything inside OVER = how to calculate.

---

## 1. ROW_NUMBER()

Assigns a unique row number to each row — even if scores are the same.

```sql
SELECT gender, math_score,
ROW_NUMBER() OVER (PARTITION BY gender ORDER BY math_score DESC) AS row_num
FROM student_performance
LIMIT 10;
```

**Output:**
```
female | 100 | 1
female | 100 | 2   ← same score, different number
female | 100 | 3
female | 99  | 4
```

imp. No ties — every row gets its own unique number regardless of duplicate values.

imp. Top 3 from each gender — that's the power of `PARTITION BY`.

---

## 2. RANK()

Same as ROW_NUMBER but ties get the same rank and the next rank skips.

```sql
SELECT gender, math_score,
RANK() OVER (PARTITION BY gender ORDER BY math_score DESC) AS rank
FROM student_performance
LIMIT 10;
```

**See the difference:**
```
ROW_NUMBER → 1, 2, 3, 4    (always unique)
RANK       → 1, 1, 1, 4    (ties get same rank, skips 2 and 3)
```

imp. Three students scored 100 → all get rank 1 → next rank jumps to 4.

---

**Practice — RANK:**
Fetch students where rank is 1 per gender by math score. Use subquery same as before.

```sql
SELECT * FROM (
    SELECT gender, math_score,
    RANK() OVER (PARTITION BY gender ORDER BY math_score DESC) AS rank
    FROM student_performance
) AS ranked
WHERE rank = 1;
```

---

## 3. DENSE_RANK()

Ties get same rank. **No gaps** in ranking.

```sql
SELECT gender, math_score,
DENSE_RANK() OVER (PARTITION BY gender ORDER BY math_score DESC) AS dense_rank
FROM student_performance
LIMIT 10;
```

**Expected output:**
```
female | 100 | 1
female | 100 | 1
female | 100 | 1
female | 99  | 2  ← 2 not 4 (no gap)
female | 99  | 2
female | 98  | 3
```

**Difference from RANK:**
```
RANK       → 1, 1, 1, 4  (gap after tie)
DENSE_RANK → 1, 1, 1, 2  (no gap)
```

imp. Top 2 score levels from each gender — use `WHERE dense_rank <= 2` in a subquery.

---

## 4. LEAD()

Gets the value from the **next row** within the partition.

```sql
SELECT gender, math_score,
LEAD(math_score) OVER (PARTITION BY gender ORDER BY math_score DESC) AS next_score
FROM student_performance
LIMIT 10;
```

**How it works:**
```
Row 1 → score 100, next row score is 100 → LEAD = 100
Row 2 → score 100, next row score is 100 → LEAD = 100
Row 3 → score 100, next row score is 99  → LEAD = 99
Row 4 → score 99,  next row score is 99  → LEAD = 99
Last row → no next row                   → LEAD = NULL
```

**Real use case — compare each student's score with the next, see the gap:**
```
score | next_score | gap
100   | 99         | 1
99    | 98         | 1
98    | 97         | 1
```

imp. Useful in time series — sales this month vs next month, stock price today vs tomorrow.

---

## 5. LAG()

Opposite of LEAD — gets value from the **previous row**.

```
LEAD → looks forward  (next row)
LAG  → looks backward (previous row)
```

```sql
SELECT gender, math_score,
LAG(math_score) OVER (PARTITION BY gender ORDER BY math_score DESC) AS prev_score
FROM student_performance
LIMIT 10;
```

imp. First row will be NULL — no previous row exists.

