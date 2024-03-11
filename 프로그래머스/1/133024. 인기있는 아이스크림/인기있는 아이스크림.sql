-- 코드를 입력하세요
-- 상반기에 판매된 아이스크림 맛
-- 총주문량 기준 내림차순, 출하 번호
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC , SHIPMENT_ID ASC
