import json
import os
import requests
from bs4 import BeautifulSoup

QUERY = "G203"  # Referencia de prueba común en las 3 tiendas (Logitech G203)
OUTPUT_DIR = "spikes/raw_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
}


def save_sample(filename: str, content: str):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"   💾 Muestra guardada en: {path}")


def audit_exito(query: str):
    print("\n" + "=" * 60)
    print(f"🟢 1. AUDITANDO ALMACENES ÉXITO (Query: {query})")
    print("=" * 60)

    url_vtex = f"https://www.exito.com/api/catalog_system/pub/products/search?ft={query}"
    try:
        r = requests.get(url_vtex, headers=HEADERS, timeout=10)
        print(f"[VTEX API] Status: {r.status_code} | Content-Type: {r.headers.get('Content-Type')}")
        if r.status_code in (200, 206) and "application/json" in r.headers.get("Content-Type", ""):
            data = r.json()
            print(f"   ✅ ÉXITO: Devuelve JSON directo con {len(data)} productos.")
            if data:
                sample = data[0]
                print(f"   📌 Ejemplo Título: {sample.get('productName')}")
                print(f"   📌 Ejemplo Marca:  {sample.get('brand')}")
                print(f"   📌 Ejemplo Ref:    {sample.get('productReference')}")
            save_sample("exito_vtex_sample.json", json.dumps(data[:2], indent=2, ensure_ascii=False))
            return
    except Exception as e:
        print(f"   ⚠️ Error en VTEX API: {e}")

    url_web = f"https://www.exito.com/s?q={query}"
    r_web = requests.get(url_web, headers=HEADERS, timeout=10)
    print(f"[WEB SSR]  Status: {r_web.status_code} | Tamaño HTML: {len(r_web.text)} bytes")
    save_sample("exito_web_sample.html", r_web.text[:15000])


def audit_alkosto(query: str):
    print("\n" + "=" * 60)
    print(f"🟠 2. AUDITANDO ALKOSTO (Query: {query})")
    print("=" * 60)

    url_json = f"https://www.alkosto.com/search/autocomplete/SearchBox?term={query}"
    try:
        r = requests.get(url_json, headers=HEADERS, timeout=10)
        print(f"[JSON API] Status: {r.status_code} | Content-Type: {r.headers.get('Content-Type')}")
        if r.status_code == 200 and "json" in r.headers.get("Content-Type", "").lower():
            data = r.json()
            products = data.get("products") or []
            print(f"   ℹ️ Endpoint JSON respondió con {len(products)} productos en 'products'.")
            save_sample("alkosto_json_sample.json", json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"   ⚠️ Error en JSON API: {e}")

    url_html = f"https://www.alkosto.com/search?text={query}"
    try:
        r_html = requests.get(url_html, headers=HEADERS, timeout=10)
        print(f"[WEB HTML] Status: {r_html.status_code} | Tamaño HTML: {len(r_html.text)} bytes")
        if r_html.status_code == 200:
            soup = BeautifulSoup(r_html.text, "html.parser")
            titles = [
                t.get_text(strip=True)
                for t in soup.select("h3.product__item__top__title, h2.product__information__title")[:3]
            ]
            print(f"   ✅ ÉXITO HTML: {len(titles)} muestras extraídas directamente del DOM.")
            for idx, title in enumerate(titles, 1):
                print(f"   📌 Muestra {idx}: {title}")
        save_sample("alkosto_web_sample.html", r_html.text[:15000])
    except Exception as e:
        print(f"   ⚠️ Error en WEB HTML: {e}")


def audit_mercadolibre(query: str):
    print("\n" + "=" * 60)
    print(f"🟡 3. AUDITANDO MERCADO LIBRE CO (Query: {query})")
    print("=" * 60)

    url_api = f"https://api.mercadolibre.com/sites/MCO/search?q={query}"
    r_api = requests.get(url_api, headers=HEADERS, timeout=10)
    print(f"[REST API] Status sin Token: {r_api.status_code}")

    url_web = f"https://listado.mercadolibre.com.co/{query}"
    r_web = requests.get(url_web, headers=HEADERS, timeout=10)
    print(f"[WEB SSR]  Status: {r_web.status_code} | Tamaño HTML: {len(r_web.text)} bytes")

    if r_web.status_code == 200:
        soup = BeautifulSoup(r_web.text, "html.parser")
        items = soup.select("li.ui-search-layout__item, div.poly-card")
        print(f"   ✅ ÉXITO: HTML renderizado en servidor con {len(items)} tarjetas detectadas.")
        titles = [t.get_text(strip=True) for t in soup.select("h2.poly-box, h2.ui-search-item__title")[:3]]
        for idx, title in enumerate(titles, 1):
            print(f"   📌 Muestra {idx}: {title}")
        save_sample("meli_web_sample.html", r_web.text[:20000])


if __name__ == "__main__":
    print("🚀 Iniciando SPIKE-001: Auditoría de Fuentes para BuyHub...")
    audit_exito(QUERY)
    audit_alkosto(QUERY)
    audit_mercadolibre(QUERY)
    print("\n🏁 Auditoría finalizada. Revisa la carpeta 'spikes/raw_output/' para inspeccionar los datos.")