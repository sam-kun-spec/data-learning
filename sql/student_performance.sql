-- Dataset: Students Performance in Exams (Kaggle)
-- Table: student_performance

-- Q1: Average scores by gender
SELECT gender,
       ROUND(AVG(math_score), 2) AS avg_math,
       ROUND(AVG(reading_score), 2) AS avg_reading,
       ROUND(AVG(writing_score), 2) AS avg_writing
FROM student_performance
GROUP BY gender;

-- Q2: Top 5 students by math score
SELECT gender, race_ethnicity, math_score
FROM student_performance
ORDER BY math_score DESC
LIMIT 5;

-- Q3: Test preparation count
SELECT test_preparation, COUNT(*) AS total
FROM student_performance
GROUP BY test_preparation;

-- Q4: Average math score by parental education level
SELECT parental_education, ROUND(AVG(math_score), 2) AS avg_math
FROM student_performance
GROUP BY parental_education
ORDER BY AVG(math_score) DESC;

-- Q5: Students who scored above average in all 3 subjects
SELECT * FROM student_performance
WHERE math_score > (SELECT AVG(math_score) FROM student_performance)
  AND reading_score > (SELECT AVG(reading_score) FROM student_performance)
  AND writing_score > (SELECT AVG(writing_score) FROM student_performance);
