-- 코드를 작성해주세요
SELECT A.EMP_NO, A.EMP_NAME, B.GRADE,
    CASE
        WHEN B.GRADE = 'S' THEN A.SAL*0.20
        WHEN B.GRADE = 'A' THEN A.SAL*0.15
        WHEN B.GRADE = 'B' THEN A.SAL*0.10
        ELSE 0
    END AS BONUS
FROM (SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
      FROM HR_GRADE
      GROUP BY EMP_NO
     ) AS B
JOIN HR_EMPLOYEES AS A
ON A.EMP_NO = B.EMP_NO