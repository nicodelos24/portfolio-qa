# Revisión documental · 9 de octubre de 2026

## Alcance y fuentes

Revisión del contenido y del historial del portafolio central hasta `0772d44`, incluidos los cambios locales previos en README y textos de perfiles. Se contrastaron los registros de Traza (`e2d0d24`) y String (`d4e0c47`), sus historiales y documentación relevante de los productos. No se ejecutaron nuevamente las aplicaciones ni se realizaron pruebas manuales del producto en esta revisión.

También se consultaron el CV original aportado en DOCX y el informe de desempeño con certificado de Jóvenes a Programar. El CV original y el informe se conservan localmente en `privado/fuentes/`, excluido de Git; la versión de postulación se redactó de nuevo. No se publican la cédula, fecha de nacimiento ni el teléfono de la referencia laboral incluidos en los adjuntos.

## Correcciones principales

| Afirmación anterior | Evidencia y decisión |
| --- | --- |
| Dos años de garantía de calidad industrial | El autor confirma tareas de ensamblaje y encintado. Se presenta el puesto real, sin convertirlo en experiencia de inspección o QA. |
| Yazaki: producción de alimentos | Incorrecto. Se corrige a ensamblaje de arneses eléctricos. |
| Traza: 93 casos ejecutados | `casos-de-prueba.md` contiene 59 filas de casos con ID único; el último ID es CP-93. El número final del identificador no es un conteo. No se descarta trabajo adicional, pero no está representado por 93 registros individuales. |
| Traza: 43 defectos documentados | `reportes-de-bug.md` desarrolla B-001 a B-010: 10 reportes. Hay referencias a otros IDs en los casos, pero no sus reportes individuales en ese archivo. |
| Traza: 9 o 10 críticos | El README dice 9; los resúmenes dicen 10; 8 de los 10 reportes desarrollados llevan severidad CRÍTICO. Se omite el total de críticos en el CV. |
| Traza: cada caso con pasos, esperado y obtenido | La tabla publicada contiene ID, descripción y resultado resumido. Hace falta ampliar los registros para sostener esa afirmación en todos los casos. |
| Traza: 11 de 11 pantallas | La matriz enumera 11 y el README describe un producto con 13. No se anuncia cobertura total. |
| Traza: teléfono demostrado por 390 px | Un ancho de pantalla no identifica dispositivo físico. La prueba en teléfono es declarada por el autor; faltan detalles de entorno por ejecución. |
| String: 177 pruebas manuales o todas aprobadas | Son 177 casos: 114 automatizados y 63 manuales. La línea base registra 4 aprobaciones manuales individuales, 43 casos sin ejecución individual, 14 bloqueados y 2 retirados. |
| String: 42 defectos únicos | Son 42 reportes, incluidos duplicados, reversiones y una aclaración de requisitos. Se mantiene esa distinción. |
| Todos los hallazgos son exclusivamente manuales | String también documenta diagnóstico y hallazgos asistidos. Se atribuyen las pruebas manuales al autor y se distingue el trabajo automático o asistido. |
| Técnico en Desarrollo Web como título | El certificado acredita aprobar el curso Desarrollo Web en 2025, emitido por Ceibal. El encabezado técnico de la rúbrica no demuestra un título terciario. |
| Inglés B1 y lectura técnica consolidada | El informe no indica B1. Registra Low Intermediate general, Intermediate oral y High Beginner en lectura. No se extrapola un nivel actual. |
| Experiencia profesional en automatización / Excel | No respaldada por tener scripts o planillas generados. Se respeta el uso de GitHub Desktop y la experiencia puntual declarada. |
| Fechas laborales 2023–2025 | No figuran en el CV original. El autor confirmó abril de 2021–enero de 2024 en Yazaki y setiembre de 2024–octubre de 2026 en El Otro Portón. Se quita «trabajo actual» porque el autor confirma que está desempleado. |

## Estado de los repositorios relacionados

Las discrepancias de Traza se describen aquí y se corrigen en los textos del portafolio central. Sus tablas y evidencias de origen se mantienen: completar reportes faltantes requiere recuperar registros reales, no inventar resultados para hacer coincidir un resumen.

String distingue exploración continua declarada (EXP-01) de ejecuciones individuales. La cantidad de aprobaciones documentadas no representa todo el tiempo dedicado a probar manualmente. Tampoco permite asumir que todas las funciones ya fueron aceptadas.

Se comprobó además que la rama predeterminada remota de `qa-traza` es `master`, cuyo commit `9860f11` no contiene el README de QA. La documentación está publicada en `main` (`e2d0d24`). Los enlaces del portafolio llevan explícitamente a esa rama; no se cambió la configuración del repositorio relacionado.

## Criterio editorial

Español neutro, ejemplos concretos y foco en QA manual inicial. Se eliminan comparaciones despectivas con otros candidatos, promesas sobre contratación, frases defensivas, repeticiones, enlaces locales inexistentes y conclusiones absolutas sobre cobertura o seguridad. El uso de IA se declara sin atribuir dominio de automatización.

## Pendientes para completar los perfiles

Confirmar las fechas de los demás empleos y el curso de testing de Udemy. Las fechas de Yazaki y El Otro Portón, el curso actual de UTEC y la matrícula de CTC para 2027 fueron confirmados por el autor durante esta revisión. La formación y experiencia omitidas del CV abreviado siguen referenciadas en el [plan personal](plan-de-formacion.md). No se modificaron perfiles en plataformas de empleo ni se enviaron postulaciones.

## Cierre: CV elegido y organización

El autor eligió `CV-Nicolas-.pdf`: primera foto mejorada con IA, ampliada a 3,6 cm. Ese PDF se incorpora sin alterar sus bytes como `cv/CV-Nicolas-De-Los-Santos-QA.pdf`, junto al HTML correspondiente, la fotografía elegida y su prompt. El [registro del CV](cv/README.md) documenta la selección y su hash.

Se centralizan en este repositorio los archivos útiles de la revisión. Los adjuntos personales originales, los respaldos de documentación y los scripts históricos de preparación quedan en `privado/`, ignorado por Git. Los scripts históricos se conservan como registro, no como instrucciones de mantenimiento: contienen rutas y estados de trabajo anteriores.

Las variantes de foto y CV descartadas se eliminan de las carpetas de comparación y temporales de esta sesión. No se alteran los repositorios de Traza o String ni el historial Git del portafolio. Las discrepancias de evidencia de Traza siguen pendientes en su repositorio de origen; no se inventaron registros para completarlas.

La comprobación final cubre enlaces internos, presencia de la foto elegida en el HTML y el PDF, una página A4, correspondencia del texto entre Markdown, HTML y PDF, y exclusión de materiales privados de Git. No constituye una nueva ejecución de pruebas de las aplicaciones.
