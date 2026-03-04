---
name: brand-identity-amtfar
version: 1.0.0
description: Mantiene una identidad visual sobria y profesional para cualquier sección nueva del sistema, aplicando la paleta de colores y el estilo minimalista de AMTFAR.
tags: [diseño, ui, frontend, estilo]
---

# Brand Identity AMTFAR

## Cuándo usar este skill
- Cuando se cree o modifique una nueva sección, como un comunicado, una tabla de beneficios o un componente de UI.
- Cuando el usuario solicite mantener la identidad visual del proyecto.

## Inputs requeridos
- `contexto_ui`: El contenido o la sección a la que se aplicarán los estilos.
- `elemento_objetivo`: Detalles sobre qué tipo de elemento se está modificando (ej. botón, contenedor, tabla).

## Workflow de Aplicación
1. **Análisis de Colores:** 
   - Verificar que el fondo de las secciones o contenedores sea blanco puro (`#ffffff` o clases equivalentes).
   - Confirmar que los textos principales usen un gris oscuro (`#333333` o similar) para asegurar un contraste sobrio y profesional.
   - Restringir el uso del verde institucional de AMTFAR **única y exclusivamente** para llamadas a la acción (botones/enlaces) y encabezados (headers).
2. **Validación de Estilo:**
   - Aplicar un estilo general minimalista e institucional.
   - Definir bordes claros (uso sutil de bordes definidos) en lugar de estilos excesivamente redondeados o con sombras pesadas.
   - Incorporar íconos lineales o contorneados para soportar visualmente las secciones.
3. **Revisión Tipográfica:**
   - Asegurar el uso de una fuente Sans-serif limpia (como Inter, Arial, Helvetica o la tipografía principal de sistema).
4. **Respuesta y Aplicación:**
   - Proponer o generar el código (HTML/CSS, Tailwind, etc.) respetando estrictamente todas estas directrices corporativas.

## Formato de Salida
- El skill entregará sugerencias de diseño, código CSS, HTML o Markdown que cumplan exactamente con esta guía visual, documentando qué colores o reglas se aplicaron.
