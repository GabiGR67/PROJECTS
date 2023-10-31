/* 1: */

SELECT u.nombre
FROM universidad u
WHERE u.id NOT IN (SELECT DISTINCT c.universidad FROM concurso c);

/* 2: */

SELECT p.nombre, p.apellidos
FROM participantes p
GROUP BY p.nombre, p.apellidos
HAVING COUNT(DISTINCT (SELECT c.universidad FROM concurso c WHERE c.participante = p.id)) > 1;

/* 3: */

SELECT año
FROM concurso
GROUP BY año
ORDER BY COUNT(DISTINCT participante) DESC
LIMIT 1;

/* 5: */

SELECT p.nombre, p.apellidos
FROM participantes p
INNER JOIN concurso c ON p.id = c.participante
WHERE c.puesto = 1
ORDER BY p.fnac
LIMIT 1;

/* 6: */

SELECT u.nombre
FROM universidad u
WHERE u.id NOT IN (
    SELECT c.universidad
    FROM concurso c
    WHERE c.puesto < 5
);
