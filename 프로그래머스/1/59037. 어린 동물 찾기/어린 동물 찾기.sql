-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME from ANIMAL_INS 
WHERE INTAKE_CONDITION NOT IN ('Aged') 
ORDER BY ANIMAL_ID;