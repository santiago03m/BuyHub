# Visión y Alcance del MVP

## 1. Problema
Buscar un producto específico por marca y referencia exacta en comercios de Colombia implica revisar múltiples tiendas manualmente, lidiar con títulos mal estructurados y comparar resultados que mezclan el producto principal con repuestos o accesorios.

## 2. Propuesta de Valor
Un buscador capaz de consultar múltiples fuentes locales a partir de una referencia comercial (ej. `LS2 FF808`), distinguiendo coincidencias exactas de resultados aproximados o accesorios.

## 3. Alcance del MVP (Qué SÍ entra en la primera versión)
- Búsqueda por texto libre enfocada en `[Marca] + [Referencia]`.
- Integración inicial con [2 a 3] fuentes/tiendas validadas en la fase de investigación.
- Normalización básica de resultados: Título, Precio, Tienda de origen, Disponibilidad y Enlace directo.
- Separación visual o lógica entre coincidencia exacta y coincidencia parcial.

## 4. Fuera del Alcance del MVP (Qué NO entra todavía)
- Cuentas de usuario, alertas por correo o historial personalizado.
- Integración con pasarelas de pago (el buscador redirige a la tienda original).
- Extracción de tiendas que requieran evasión compleja de captchas en tiempo real.

## 5. Métricas de Éxito del MVP
- **Precisión de coincidencia:** Al buscar 10 referencias conocidas, al menos el 80% de los resultados marcados como "exactos" corresponden realmente al modelo buscado (y no a un repuesto o accesorio suelto).
- **Tiempo de respuesta / actualización:** Capacidad de obtener u ofrecer datos actualizados sin bloqueo de IP en las fuentes seleccionadas.