-- 코드를 입력하세요
SELECT floor(PRICE/10000)*10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY floor(PRICE/10000)*10000
ORDER BY PRICE_GROUP