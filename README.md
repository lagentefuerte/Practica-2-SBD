# Practica-2-SBD

Este repositorio contiene la solución a una serie de retos prácticos de inyección SQL, diseñados para profundizar en diferentes técnicas de explotación y extracción de información en bases de datos MySQL.

---

## Descripción General

El proyecto está compuesto por 8 retos que abordan distintas técnicas de inyección SQL, desde las más básicas hasta inyecciones ciegas y basadas en tiempo. Cada reto incluye análisis del código fuente, pruebas de payloads, y metodologías para obtener información sensible como usuarios, contraseñas, y flags.

---

## Retos y Técnicas Abordadas

### Reto 1: Inyección clásica con strings
- Uso de payload clásico `' OR 1=1-- ` para obtener un punto de control.
- Extracción de datos con `UNION SELECT` en tablas y columnas comunes (`users`, `password`).

### Reto 2: Inyección numérica sin comillas
- Inyección sin uso de comillas para parámetros numéricos.
- Payload usado: `1 OR 1=1-- `.

### Reto 3: Inyección en strings con cierre de comillas
- Uso del clásico `' OR 1=1-- ` para devolver todas las filas.

### Reto 4: Unión select en tabla legítima
- Consulta con `UNION SELECT bookname, authorname FROM books--`.
- Extracción de datos legítimos para obtener la flag.

### Reto 5: Evitar caracteres restringidos
- Evitar espacios y comillas con comentarios en línea: `1/**/OR/**/CHAR(49)=CHAR(49)--`.
- Uso de `CHAR()` para sustituir valores.

### Reto 6: Inyección Blind SQL basada en booleanos
- Detección de existencia mediante true/false.
- Extracción letra por letra del nombre de la tabla y la contraseña.
- Uso de payloads con `SUBSTRING()` y `LIKE`.

### Reto 7: Inyección Blind SQL basada en tiempo (time-based)
- Uso de `SLEEP()` para inferir datos a partir de la latencia.
- Automatización con script en Python para extraer la contraseña carácter a carácter.

### Reto 8: Descubrimiento de tablas y columnas en esquema
- Enumeración de tablas con `information_schema.tables`.
- Descubrimiento de columnas en tabla sospechosa (`secret_users`).
- Extracción de contraseñas.

---

## Scripts y Herramientas Utilizadas

- Burp Suite Intruder para automatización de payloads en inyección blind.
- Script Python para automatizar la extracción de la flag en retos basados en tiempo.

### Este proyecto demuestra un entendimiento profundo de las técnicas de inyección SQL, incluyendo inyecciones clásicas, blind booleanas y basadas en tiempo, así como la habilidad para eludir filtros y restricciones.


