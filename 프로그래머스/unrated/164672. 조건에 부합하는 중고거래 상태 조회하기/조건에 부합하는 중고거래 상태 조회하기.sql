-- 코드를 입력하세요

-- VER1. REPLACE 중첩문 이용한 풀이
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, REPLACE(REPLACE(REPLACE(STATUS, "SALE", "판매중"),"RESERVED", "예약중"), "DONE", "거래완료") AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE LIKE "2022-10-05"
ORDER BY BOARD_ID DESC

-- VER2. CASE WHEN 문법 이용한 풀이
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
CASE 
    WHEN STATUS = "SALE" THEN "판매중"
    WHEN STATUS = "RESERVED" THEN "예약중"
    ELSE "거래완료"
    END AS STATUS
 -- 다중 변경 V2 : CASE WHEN - ELSE - END AS "표기할 변수명"
 -- sql의 case when : python의 elif 문법 같은 느낌 
FROM USED_GOODS_BOARD
WHERE CREATED_DATE LIKE "2022-10-05"
ORDER BY BOARD_ID DESC
