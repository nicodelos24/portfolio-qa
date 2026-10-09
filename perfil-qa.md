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

## Herramientas

Separo lo que **use** de lo que **conozco**, porque un reclutador lo pregunta y
hay que responder exacto.

### Las he usado

| Herramienta | Para qué |
| --- | --- |
| **Git y GitHub** | Versionado, historial y comparación entre versiones |
| **Katalon Recorder** | Grabación y reproducción de recorridos |
| **Excel** | Registro de casos, defectos y resultados |

### En formación

| | |
| --- | --- |
| **SQL** | Quiero aprenderlo: aparece en casi todos los avisos de QA |
| **ISTQB Foundation** | Certificación que todavía no tengo |

> **No listo herramientas que no conozco.** Preferimos que falte información a
> que sobre: un reclutador que descubre una exageración no cree ninguna de las
> verdaderas.

---

## Ingles

Nivel medido en **Voxy**: **Low Intermediate** en la evaluación general, e
**Intermediate** en conversacion.

Se me da para leer documentación tecnica y escribir. Me cuesta el
conversacional, y estoy trabajando en eso.

Lo digo de entrada porque **dos de los cuatro avisos que revise lo piden como
requisito**. Prefiero que lo sepan antes de la entrevista.

---

## Formación

**Curso de testing en Udemy** — es de ahí donde salen mis nociones de QA: qué
es un caso de prueba, cómo se escribe un defecto, qué es una prueba de
regresión. Las nociones las tengo; la práctica la estoy construyendo con estos
proyectos.

**Desarrollo web**, aprobado con **86 % de promedio**.

Competencias destacadas segun el informe del curso: HTML semántico con buenas
prácticas de accesibilidad, CSS con dominio de especificidad y prioridad,
JavaScript del lado del cliente, diseño responsive, manejo de eventos y
validación de datos ingresados por el usuario.

**Esto me sirve para QA**, no como programador: me permite entender que esta
mirando el usuario en pantalla, distinguir un error de maquetado de uno de
lógica, y escribir un reporte que se entienda.

---

## Como trabajo

Completo en [`metodologia.md`](metodologia.md). Lo esencial:

- **Pruebo como varias personas a la vez**, no solo una
- **Rastreo el dato hasta el origen** cuando un número parece raro
- **Pruebo las esquinas**, no el camino feliz
- **Pruebo el día completo**, no pantalla por pantalla
- **Pruebo en el teléfono de verdad**
- **Documento antes de arreglar**, para no perder el motivo
