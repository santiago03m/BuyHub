# Viabilidad Técnica de Fuentes de Datos — BuyHub

Documento vivo para registrar qué comercios electrónicos en Colombia pueden ser consultados por **BuyHub**, cómo exponen sus datos y qué limitaciones técnicas presentan.

## 1. Criterios de Clasificación
- **Nivel 1 (Ideal - API / JSON público):** La tienda usa plataformas (ej. API pública, VTEX, Shopify `/search/suggest.json`, WooCommerce Store API) que devuelven JSON estructurado con título, precio, SKU/referencia y enlace.
- **Nivel 2 (Medio - HTML Estático / SSR):** El servidor devuelve el HTML completo en la primera petición (`fetch`/`curl`) y se puede extraer con un parser ligero sin ejecutar un navegador completo.
- **Nivel 3 (Complejo - SPA / Anti-bot activo):** Requiere navegador headless (Playwright) o tiene bloqueos agresivos (Cloudflare Turnstile, Captchas). *Quedan fuera del MVP inicial.*

## 2. Matriz de Evaluación de Tiendas

| Tienda / Fuente | URL Base | Tecnología Detectada | Método de Extracción | ¿Expone Referencia/SKU? | Nivel de Dificultad | ¿Entra al MVP? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *Ej. Mercado Libre CO* | `mercadolibre.com.co` | API / Web | API / Scraping | Parcial (en ficha técnica) | Nivel 1 / 2 | Pendiente |
| *Tienda 2 (Por definir)* | `...` | Shopify / VTEX / Woo | ... | Sí / No | ... | Pendiente |
| *Tienda 3 (Por definir)* | `...` | ... | ... | Sí / No | ... | Pendiente |

## 3. Hallazgos de Estructura de Títulos (Muestras Reales)
*(Aquí pegaremos ejemplos reales durante el SPIKE-002 para diseñar el filtro entre producto principal vs. accesorios)*

- **Referencia de prueba:** `[Ej. LS2 FF808]`
  - Muestra Tienda 1: `...`
  - Muestra Tienda 2: `...`
  - Ruido detectado (accesorios/repuestos): `...`