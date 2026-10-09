# Plan de formación: qué cubro y qué me falta

> Análisis hecho comparando mi perfil contra los requisitos de cuatro avisos de
> empleo reales de QA (Dynamics 365, QA Analyst remoto, Analista de Soporte y
> Tester, y QA Manual Senior).
>
> Sirve para dos cosas: saber en qué orden aprender, y saber qué responder con
> honestidad en una entrevista.

---

## 1. Lo que ya cubro

Requisitos que aparecen en **cuatro de los cuatro avisos**:

| Requisito | Mi cobertura |
| --- | --- |
| Diseñar, ejecutar y documentar casos de prueba | Sí — 93 casos con pasos y resultado |
| Identificar, registrar y dar seguimiento a defectos | Sí — 43 reportes con causa y severidad |
| Matrices de cobertura y trazabilidad | Sí — con la parte de lo no cubierto |
| Pruebas funcionales en web y móvil | Sí — probé en escritorio y en 390 px |
| Pruebas de regresión y no regresión | Sí — hay pruebas que fallan antes del arreglo |
| Pruebas de extremo a extremo | Sí — el recorrido del día completo |
| Análisis de requerimientos, historias y criterios de aceptación | Sí — reconstruidos de 52 commits |
| Git y GitHub | Sí |
| Rigor y atención al detalle | Sí — es lo que más reporté |

**Ese es el núcleo del QA funcional.** Está cubierto con trabajo real.

---

## 2. Lo que me falta

| Requisito | Lo tengo | Dificultad |
| --- | :-: | --- |
| **Jira** (seguimiento de defectos) | ⚪ Sé el concepto, no lo usé | **Fácil** |
| **SQL** (consultas a bases de datos) | ❌ | **Fácil** |
| **Postman / pruebas de API REST** | ❌ No lo conozco | **Fácil** |
| **Katalon Recorder** | ⚪ Recorridos básicos | — |
| **ISTQB Foundation** (certificación) | ❌ | **Fácil y barata** |
| **Cypress** (automatización) | ⚪ Bases de un curso anterior, sin uso reciente | Media |
| **Herramienta de gestión de pruebas** (Xray, Zephyr, TestRail) | ❌ | Media |
| **Pruebas UAT con usuarios** | ❌ | Depende del puesto |
| **Automatización UI** (Playwright, Cypress) | ⚠️ El proyecto tiene, yo no lo escribí | Media |
| **Programación** (Python, JS) | ❌ | Alta |
| **Years of experience** | ❌ | No se compra |
| **Experiencia en el rubro** (bancario, CRM) | ❌ | Depende del puesto |

---

## 3. El plan, en orden

### Primero — lo barato que aparece en todos los avisos

**1. Jira** — version gratuito. Es el nombre que más se repite en los cuatro
avisos. Se aprende en una tarde: crear un ticket, describir un defecto con
pasos, adjuntar evidencia y pasarlo por estados.

**2. SQL básico** — `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`. Pedido en dos de
los cuatro avisos como deseable y en uno como clave. Es lo que más valor da por
hora de estudio, porque **sirve en cualquier empresa** y permite validar datos
directamente.

**3. Certificación ISTQB Foundation** — es el estándar mundial del QA, y dos
avisos la piden explícitamente. Es barata y es la forma más rápida de que un
reclutador me tome en serio.

> **Con estas tres, cubro casi todos los requisitos "indispensables" que me
> faltan.** Son semanas, no años.

### Después — lo que diferencia

**4. Postman** — para probar API. Requisito en tres de los cuatro avisos.
Mi proyecto no tiene API todavía (no hay base de datos), así que tendría que
usarlo en un entorno de práctica.

**5. Automatizar los casos que hoy ejecuto a mano** — esta es la mejor inversión
a mediano plazo. Tengo 93 casos manuales; si automatizo los 20 más importantes
en Playwright, paso de "hice pruebas" a "hice pruebas automatizadas", que es
justo lo que pide el aviso de Dynamics.

---

## 4. Lo que no voy a tener por ahora

- **Años de experiencia.** Todos los avisos lo piden. No hay atajo.
- **Programación.** Es lo que más me cuesta y lo que más tiempo lleva.
- **Experiencia en un rubro específico** (bancario, CRM, contact center).

**Sobre esto, la estrategia honesta:** me postulo a los avisos donde mi
experiencia en proyecto propio sea el diferencial, no a los que exigen cinco
años en un banco. Puedo ser muy útil en un equipo chico o en un proyecto que
empieza, y ahí compito con gente con la misma falta de experiencia.

---

## 5. Los avisos, uno por uno

| Aviso | Encaje |
| --- | --- |
| **QA Funcional Senior — Dynamics 365** (100% remoto, cualquier lugar) | El que más me sirve: remoto sin restricción y QA funcional. Me falta Jira, Xray, APIs e inglés. Senior y 5 años, es aspiracional |
| **QA Analyst** (remoto, $3.500-4.000 USD, requiere inglés) | El más accesible por la parte de datos: el proyecto es de costos y márgenes. Me faltan pipelines de datos, Postman y dy de **inglés**, que es la barrera grande |
| **Analista de Soporte y Tester N2** (Montevideo, híbrido) | Pide 2 a 3 años excluyente y formación universitaria. Hoy no entra. Es un objetivo a 1-2 años |
| **QA Manual Senior** (Buenos Aires, híbrido, 3 días presenciales) | Pide experiencia en bancos y Sybase/Oracle. Poco encaje ahora |

**Conclusión:** el orden no es "postular a todos". Es **Jira + SQL + ISTQB
primero**, y mientras tanto mirar los avisos que pidan menos años y más
funcionalidad.

---

## 5.bis Lo que agrega este proyecto a lo que ya tenía

Con el proyecto **String** (177 casos, 42 reportes, trazabilidad completa) y
**Traza** (93 casos, 43 reportes), el portafolio ya tiene dos aplicaciones
probadas de punta a punta. Eso es un diferencial real frente a quien solo hizo un
curso.

Y las herramientas quedaron así, con honestidad:

| | Estado |
| --- | --- |
| Git y GitHub | **Usado** en los dos proyectos |
| Excel y Markdown | **Usados** |
| Katalon Recorder | **Recorridos básicos** |
| Jira | Sé el concepto, no lo usé |
| Playwright | Lo vi correr en el proyecto; no lo escribí yo |
| Confluence, Postman, Xray, TestRail | **No los conozco** |
| Cypress | Bases de un curso, sin uso reciente |
| SQL, ISTQB | Pendientes |

**En el perfil no aparecen las herramientas que no conozco.** Preferimos que
falte información antes que sobre, porque un recruitment que descubre una
mentira chica no cree ninguna de las grandes.

---

## 5.ter Lo que cambia el plan: experiencia laboral real

Leyendo el currículum apareció algo que no estaba considerado, y **es lo más
valuoso que tengo hoy**.

Antes de dedicarme a esto trabajé:

| Trabajo | Por qué importa para QA |
| --- | --- |
| **Mozo en restaurante** | Conoce cómo funciona un turno de servicio de verdad |
| **Operario de planta (Yazaki)** | Producción de alimentos: entra materia prima, proceso, sale |
| **Cajero** | Totales, cambios, cuentas por cobrar |
| **Reponedor y encargado de lácteos** | Stock, reposición y conteo en un supermercado |
| **Telecomunicador** | Atención al usuario y soporte |

**Esto no es "cualquiera puede probarlo".** Un tester que nunca entró a un
restaurante puede verificar que una pantalla carga; **no puede decir que el
proceso está mal**, porque no sabe cómo funciona.

Para los avisos de software de restaurants y gestión, eso es un diferencial
directo. Cambia la conversación de "¿tenés experiencia?" a "**mirá lo que
entiendo del negocio**".

**Cómo usarlo:** en cada entrevista, contar un ejemplo concreto desde un trabajo
real. El de los productos que llegan mal es el mejor, y es real.

> Nota: el currículum tiene desactualizado el puesto actual. Hay que revisarlo
> antes de enviarlo a cualquier lado.

---

## 6. La barrera más grande, dicha honesta

No es la falta de herramientas. **Es el inglés.**

Dos de los cuatro avisos lo piden explícitamente, y el mejor-paying lo tiene como
requisito. Mi nivel medido es **Low Intermediate** (B1), con conversación en
**Intermediate**. Se me da para leer documentación técnica y escribir, que es lo
que más se usa en QA, pero el conversacional me cuesta.

Es lo que más rápido separa a candidatos que saben lo mismo. Si hay que elegir
entre aprender SQL o practicar inglés técnico, **el inglés rinde más**: el SQL lo
estudio cuando quiero, y el inglés lleva años.

Si hay que elegir entre aprender SQL y practicar inglés técnico, **el inglés
rinde más**, porque el otro es un requisito que yo controlo studying y este
depende de años.

---

## 7. Cómo voy a mostrar esto en una entrevista

Cuando pregunten por experiencia, respondo con lo que hice y **digo claramente
que fue en proyecto propio y sin usuarios todavía**.

No invento nada. Concreto:

> *"Tengo un proyecto propio, una aplicación de costos para restaurantes. Hice
> 93 casos de prueba y encontré 43 errores, diez de ellos de privacidad: datos que
> se veían sin permiso. El más importante es que el sistema ocultaba el ícono de
> la pantalla de finanzas, pero la pantalla abría igual escribiendo la dirección.
> Lo encontré usando la aplicación como cuatro personas distintas y comparando. Lo
> corregí, escribí la prueba que falla antes del arreglo, y ahora la pantalla no
> existe para quien no tiene permiso."*

Eso es trabajo de QA real. Y es verdad.