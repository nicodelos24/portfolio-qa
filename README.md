# Portafolio de QA — Nicolás De Los Santos Leal

Analista de QA. Probé **dos aplicaciones propias de punta a punta**: casos de
prueba, reportes de defecto con causa raíz, matrices de cobertura y pruebas de
regresión.

> **En una frase:** dos años bajo filosofía Cero Defecto en línea de ensamblaje,
> más dos aplicaciones propias probadas de punta a punta.

> **Transparencia.** Las pruebas y los hallazgos son míos. El desarrollo y la
> automatización usaron asistencia de inteligencia artificial, y la redacción
> de los documentos también. En cada repositorio está dicho qué hizo cada uno.

---

## Lo que más me diferencia

**Dos años trabajando bajo filosofía "Cero Defecto" en una línea de ensamblaje de
autopiezas.** Eso es trabajo de calidad, con disciplina de calidad, y es lo que
más pesa de todo mi perfil.

| Lo que se aplicaba ahí | Por qué importa para probar software |
| --- | --- |
| **Cero defecto** | Un error aparentemente menor generaba pérdidas enormes y podía poner en riesgo a quien usara el producto. La calidad como barrera, no como sugerencia |
| **Regla de las 3 Ns**: no recibo defectos, no genero defectos, no entrego defectos | Es, literalmente, el ciclo de vida de un defecto |
| **Tiempos cronometrados** | El retraso de una persona paraba toda la línea. Un detalle chico tiene consecuencias grandes en un proceso encadenado |
| **Kanban** | Ver el trabajo por etapas, con trazabilidad de en qué punto está cada cosa |
| **Trazabilidad de defectos** | Lo que hacía mal un operario acarreaba el error hacia atrás, hasta el proveedor. Se buscaba la causa de origen, no el síntoma |

Después, **reposición y encargado del sector de lácteos** en un supermercado:
encargado por compromiso e iniciativa propios, aprendiendo y ayudando en
sectores que no eran mi obligación.

También **dos años como bachero y ayudante de cocina**: toda la cocina dependía
de la eficiencia de quien está en ese puesto. Trabajo bajo presión real y en
equipo, con el resultado dependendo de mí.

---

## Proyectos

### 1. [QA — Traza](https://github.com/TU_USUARIO/qa-traza) · código en [Traza](https://github.com/nicodelos24/traza)

Aplicación de control de costos y rentabilidad para comercios de alimentación:
recetas que se costean solas, stock por libro de movimientos, compras, pedidos,
agenda y control de permisos por rol.

| | |
| --- | ---: |
| Casos de prueba manuales | 93 |
| Defectos documentados | 43 (10 críticos) |
| Commits | 52 |
| Pantallas cubiertas | 11 de 11 |

**El foco fue privacidad de datos.** La mitad de los errores críticos eran del
mismo tipo: información que se veía sin permiso. El más grave: el sistema
ocultaba el ícono de la pantalla de finanzas a quien no debía verlo, pero **la
pantalla abría igual escribiendo la dirección**.

Se detectó probando la aplicación **como cuatro roles distintos y comparando**,
y se corrigió cerrando el acceso, no tapándolo.

→ [Historias, casos, reportes y metodología](https://github.com/TU_USUARIO/qa-traza)

### 2. [QA — String](https://github.com/nicodelos24/portfolio-qa-string) · código en [String](https://github.com/nicodelos24/Proyecto-guitar-IA)

Aplicación para practicar guitarra: pedidos, reproducción de acordes y acordes
guardados.

| | |
| --- | ---: |
| Casos de prueba | 177 (114 automatizados, 63 manuales) |
| Reportes de error | 42 |
| Historias de usuario | 53 |
| Matriz de trazabilidad | Sí |

Incluye el detalle fino de los registros y la convención de distinguir qué
ejecuté yo y qué ejecutó el asistente.

---

## Qué sé hacer

- **Casos de prueba** con pasos, resultado esperado y resultado obtenido
- **Matriz de cobertura**, incluida la parte de lo que **no** está probado
- **Pruebas funcionales, de regresión y de extremo a extremo**
- **Historias de usuario y criterios de aceptación**, reconstruidos del historial
  de commits
- Pruebas de **aplicación web y aplicación móvil**
- Reportes de defecto con **severidad, pasos para reproducir, causa raíz y
  corrección**
- **Pruebas de regresión** que fallan antes del arreglo y pasan después

### Cómo pruebo

Lo que más resultados dio, y está detallado en la metodología de cada proyecto:

1. **Probar como varias personas a la vez.** Un solo rol esconde la mitad de los
   errores.
2. **Rastrear el dato hasta su origen** cuando un número parece raro. A veces
   el cálculo está bien y lo que miente es el rótulo.
3. **Probar las esquinas**, no el camino feliz: cobrar de más, no tener datos
   guardados, volver atrás, cambiar de usuario.
4. **Probar el día completo** en vez de pantalla por pantalla. Los errores
   aparecen en las costuras.
5. **Probar en el teléfono de verdad**, no solo achicando la ventana.

---

## Herramientas

### Las he usado

| Herramienta | Para qué |
| --- | --- |
| **Git y GitHub** | Versionado, historial y comparación entre versiones |
| **Katalon Recorder** | Grabación y reproducción de recorridos |
| **Excel** | Registro de casos, defectos y resultados |

### Lo que sé, con lo que sé

| Herramienta | Estado real |
| --- | --- |
| **Jira** | Sé para qué sirve: registrar y seguir defectos. **No lo he usado** |
| **Playwright** | Está en el proyecto y lo vi correr. **No lo escribí yo** |
| **Confluence, Postman, Xray, TestRail** | **No los conozco.** No los pongo porque no quiero dar a entender algo que no sé |
| **Cypress** | Hice las bases en un curso, sin uso reciente |
| **SQL, ISTQB Foundation** | Pendientes de aprender |

---

## Formación

| | |
| --- | --- |
| **Desarrollo web** | Promedio final **86 %** |
| **Testing — Udemy** | De ahí salen mis nociones de QA: caso de prueba, defecto, regresión |
| **Ciberseguridad — UTEC** | En curso |
| **Jóvenes a Programar — Ceibal/UTEC** | Completado |
| **Bootcamp de Python e IA — Ingelearn** | Completado |
| **Introducción a Java — Encode** | Completado |

Los cursos me dieron las nociones. **La práctica la construí probando estos dos
proyectos**, que es lo que me faltaba.

---

## Inglés

Nivel medido en **Voxy**: **Low Intermediate** en la evaluación general, e
**Intermediate** en conversación.

Se me da para leer documentación técnica y escribir. El conversacional me cuesta
y estoy trabajando en eso. Lo digo de entrada porque varios avisos de QA lo
piden como requisito.

---

## Sobre aprender

No tengo años de experiencia en QA, y no quiero parecer que los tengo.

Tengo **muchas ganas de aprender** y la costumbre de buscar lo que me falta. Lo
que hice en estos proyectos fue ponerlo en práctica: donde no sabía, busqué,
aprendí y lo anoté. Si un equipo necesita que aprenda SQL, Jira o
automatización, es algo que ya demostré que sé hacer: lo hice con herramientas
que no conocía cuando empecé.

---

## Contacto

Nicolás De Los Santos Leal — Colonia del Sacramento, Uruguay
[nicodelos24@gmail.com](mailto:nicodelos24@gmail.com) · [GitHub](https://github.com/nicodelos24)

> Para los proyectos de QA uso el mismo nombre y correo. Si preferís que el
> portafolio tenga una dirección propia, se cambia en un minuto.