-- 코드를 입력하세요
-- 아직 입양을 못간(OUTS) 동물 중
-- 가장 오래 있었던 동물 3마리의(INS 보호 시작일 가장 빠른 순으로)
-- 이름(INS), 보호 시작일
-- 보호 시작일 순

SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NULL
ORDER BY A.DATETIME ASC
LIMIT 3