# Viabilidad Técnica de Fuentes de Datos — BuyHub

Documento de resultados obtenidos mediante el script de auditoría `spikes/spike_001_audit.py` con la referencia de prueba `G203` (Logitech G203).

## 1. Matriz de Evaluación de Tiendas (Resultados SPIKE-001)

| Tienda / Fuente | URL Auditada | Respuesta Obtenida | Método de Extracción Viable | ¿Expone Referencia/SKU? | Nivel de Dificultad | ¿Entra al MVP? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Almacenes Éxito** | `exito.com` | `206 Partial Content` (JSON directo con 10 productos) | API pública VTEX (`/api/catalog_system/pub/products/search`) | **Sí** (`productReference`, `brand`, `items.ean`) | **Nivel 1 (Bajo)** | **SÍ (Fuente #1)** |
| **Alkosto** | `alkosto.com` | `200 OK` (`SearchBox` devuelve `products: null`; Web devuelve `1.76 MB` de HTML SSR) | Parsing de HTML SSR (`BeautifulSoup`) o consulta a API Algolia | **Parcial** (Código interno y referencia en el título) | **Nivel 1-2 (Bajo/Medio)** | **SÍ (Fuente #2)** |
| **Mercado Libre CO** | `mercadolibre.com.co` | API sin token: `403 Forbidden`. Web: `200 OK` pero devuelve reto WAF de `25 KB` (0 tarjetas) | Requiere **API Oficial con OAuth Token** o cliente con huella TLS (`curl_cffi`) | **Sí** (En atributos de API oficial) | **Nivel 2 (Medio)** | **SÍ (Con Token API / Fase 1.2)** |
| **Amazon** | `amazon.com` | Descartado en pre-auditoría (PA-API exige ventas previas y bloqueo TLS estricto) | Posponer hasta contar con credenciales PA-API | **Sí** (ASIN) | **Nivel 3 (Alto)** | **NO (Fase 2)** |

## 2. Conclusiones y Decisiones para el Desarrollo
1. **Primera integración del MVP:** Comenzar el desarrollo con **Almacenes Éxito** (JSON VTEX directo) y **Alkosto** (HTML SSR), ya que no presentan bloqueos anti-bot ante peticiones HTTP estándar.
2. **Estrategia para Mercado Libre:** No usar `requests` plano contra el HTML de `listado.mercadolibre.com.co` debido al bloqueo silencioso (página de 25 KB). Se implementará en un adaptador separado usando `curl_cffi` o credenciales de Mercado Libre Developers.