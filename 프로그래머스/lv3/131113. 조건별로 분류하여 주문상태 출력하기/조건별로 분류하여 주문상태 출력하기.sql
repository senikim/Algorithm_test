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
-- SOL1) CASE WHEN - ELSE - END 문법은 FROM절 전에 써야 함
-- SOL2) DATE_FORMAT(컬럼명, '%Y-%m-%d') 이용해서 OUT_DATE 포맷을 "날짜만" 뽑히게 변경
-- SOL2) SELECT절에 있는 b.OUT_DATE 부분 지워야 함
--       처음엔 "출고여부" 칼럼이 OUT_DATE를 복사해서 만들어야 한다고 생각해서 SELF JOIN을 했는데, 데이터가 복제되어서 중복되는 문제 발생. 
--       -> SELF JOIN이 아니었음.. -> 그냥 CASE WHEN절에 끝에 END AS "표시될 변수명"로 변수명을 지정해주면 되는 거였음
