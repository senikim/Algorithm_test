-- 코드를 입력하세요
--  주문 ID, 제품 ID, 출고일자, 출고여부를 조회
-- 출고여부 5월 1일까지 출고완료 / 이후 날짜 : 출고 대기 / 미정: 출고미정
-- 결과 : 주문id 기준으로 오름차순

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") AS OUT_DATE,
CASE
    WHEN OUT_DATE <= "2022-05-01" THEN "출고완료"
    WHEN OUT_DATE > "2022-05-01" THEN "출고대기"
    ELSE "출고미정"
END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC

-- TRIAL & ERROR 1
SELECT a.ORDER_ID, a.PRODUCT_ID, DATE_FORMAT(a.OUT_DATE, "%Y-%m-%d") AS OUT_DATE, DATE_FORMAT(b.OUT_DATE, "%Y-%m-%d") AS "출고여부"
CASE
    WHEN b.OUT_DATE <= "2022-05-01" THEN "출고완료"
    WHEN b.OUT_DATE > "2022-05-01" THEN "출고대기"
    ELSE "출고미정"
END AS "출고여부"
FROM FOOD_ORDER AS a
INNER JOIN FOOD_ORDER AS b ON a.OUT_DATE = b.OUT_DATE

-- ERROR : 값 출력 안됨
-- 
