# Definición de Terminado (Definition of Done - DoD)

Una Historia de Usuario o tarea técnica se considera **Terminada (Done)** únicamente cuando cumple todo lo siguiente:

1. **Criterios de aceptación:** Todos los checkboxes definidos en el Issue se cumplen y se comprobaron manualmente o mediante pruebas automatizadas.
2. **Calidad del código:** El código está en la rama principal (`main`) sin errores de ejecución ni credenciales expuestas (uso de `.env`).
3. **Casos de fallo controlados:** Si una fuente externa falla, cambia su estructura o no devuelve resultados, el sistema registra el error de forma limpia sin romperse.
4. **Documentación alineada:** Si la tarea implicó un cambio en las fuentes soportadas o en la arquitectura, el archivo correspondiente en `/docs` fue actualizado en el mismo Pull Request.