-- 코드를 입력하세요
-- PRODUCT_CODE 앞 2자리 별
-- 상품개수
-- 상품 카테고리 코드 기준 오름차순

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC