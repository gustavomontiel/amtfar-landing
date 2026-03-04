---
name: skill-factory
version: 1.0.0
description: Genera la estructura completa de nuevos skills siguiendo el estándar de arquitectura de Antigravity.
tags: [meta, desarrollo, arquitectura]
---

# Skill Factory

## Cuándo usar este skill
- Cuando el usuario solicite una nueva funcionalidad o "habilidad".
- Cuando se detecte una tarea repetitiva que deba ser estandarizada.

## Inputs requeridos
- `nombre_skill`: Nombre en minúsculas y con guiones (slug).
- `objetivo`: Descripción clara de qué debe lograr el skill.
- `nivel_libertad`: (1-3) Según la rigidez necesaria del proceso.

## Workflow de Fabricación
1. **Análisis de Requisitos:** Determinar si el skill requiere scripts externos o solo lógica en markdown.
2. **Generación de Metadatos:** Crear el frontmatter YAML con versión 1.0.0.
3. **Redacción de Lógica:** Escribir las secciones de Triggers, Inputs y Workflow del nuevo skill.
4. **Definición de Salida:** Establecer el formato exacto (JSON/Markdown) que entregará el nuevo skill.
5. **Generación de Estructura:** Devolver el código listo para ser guardado en `agent/skills/{nombre_skill}/`.

## Protocolo de Error
- Si el `nombre_skill` ya existe, sugerir un sufijo de versión.
- Si el `objetivo` es ambiguo, detener la generación y pedir aclaraciones.