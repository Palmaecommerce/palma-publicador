# palma-publicador

Robot que publica solo en Instagram (@palma.ecommerce) y en la página de Facebook de Palma Ecommerce.

- `calendario.json`: qué se publica y cuándo. Solo sale lo que tiene `"aprobado": true`.
- `media/`: imágenes y videos (JPG para Instagram).
- `data/estado.json`: lo que ya se publicó. `data/estadisticas.json`: métricas de cada post (se actualiza todos los días).
- `diseno/`: generador de los carruseles.

Secretos en Settings → Secrets and variables → Actions: `IG_TOKEN` (obligatorio), `FB_PAGE_TOKEN` y `FB_PAGE_ID` (Facebook, opcional), token de usuario del sistema de Meta que no vence.
