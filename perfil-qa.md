# Perfil de QA

> Para ver qué me falta y en qué orden aprenderlo:
> [`plan-de-formación.md`](plan-de-formación.md).

---

## Sobre este portafolio

**Mi trabajo y el uso de IA**

Las pruebas y los hallazgos **son míos**. Probé la aplicacion, la usé como
distintas personas, en celular y en escritorio, y los errores que aparecen en
[`reportes-de-bug.md`](reportes-de-bug.md) existen y se reproducen.

La **redacción y la organización** de estos documentos se hicieron con asistencia
de inteligencia artificial. Lo digo explícitamente para no dejar dudas.

Lo que la IA hizo fue ordenar y estructurar lo que ya estaba encontrado. **El
trabajo de prueba —qué mirar, cómo compararlo, cuando algo es un problema- es
mio**, y está explicado en [`metodologia.md`](metodologia.md).

**Relación con el otro portafolio**

Este es mi **segundo** proyecto de pruebas. El primero es
[Portfolio QA - String](https://github.com/nicodelos24/portfolio-qa-string), una
aplicacion para practicar guitarra, con 177 casos, 42 reportes de error y
matrices de trazabilidad. Ahí está el detalle fino de los registros y la
convencion de distinguir que ejecuté yo y que ejecutó el asistente.

---

## Qué probé

**Traza**, una aplicación propia de control de costos y rentabilidad para
restaurantes y comercios de alimentación. 11 pantallas, funciona en celular y
escritorio, calcula costos, márgenes, merma y food cost.

| | |
| --- | ---: |
| Casos de prueba ejecutados a mano | 93 |
| Errores encontrados y documentados | 43 |
| De ellos, severidad critica | 10 |
| Commits del proyecto | 52 |

---

## Qué sé hacer

### Diseño y ejecución de pruebas

- **Casos de prueba** con pasos, resultado esperado y resultado obtenido
- **Matriz de cobertura**, incluida la parte de lo que **no** esta probado
- **Pruebas funcionales, de regresión y de extremo a extremo**
- **Historias de usuario y criterios de aceptacion**
- Pruebas de **aplicacion web y aplicación móvil**

### Gestión de defectos

- Reportes con **severidad, pasos para reproducir, ca raíz y corrección**
- **Pruebas de regresión** que fallan antes del arreglo y pasan despues
- Seguimiento de un error hasta que no vuelve

### El área donde más aporto: **permisos y privacidad**

Casi la mitad de los errores críticos de este proyecto eran del mismo tipo:
**datos que veían sin tener permiso**.

Eso exige una forma de probar que no es la de siempre:

1. Abrir la misma pantalla **como cada rol** y compararlas
2. Escribir la dirección de la pantalla **a mano**, sin pasar por el menú
3. Intentar salir de cada pantalla en cada rol, buscando quedarme encerrado

Ninguna de las tres se hace probando una sola vez, con un solo usuario.

---


