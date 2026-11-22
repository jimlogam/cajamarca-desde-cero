# Cajamarca desde cero

Ventana del dueño para ver el trabajo: todo lo que se construye de Cajamarca vive en este repositorio.

## La estructura (única fuente)

`INDICE_TAXONOMIA.md` — el árbol entregado por el dueño: **16 macro-sectores, 54 rubros, 160 subrubros**. Cada negocio se ubica en un subrubro.

## Lo que ya hay

- `clasificacion/NEGOCIOS-CLASIFICADOS-CAJAMARCA.csv` — **712 negocios únicos** clasificados en macro-sector / rubro / subrubro (de 5 CSV de Maps Scraper: 1.216 filas, 504 duplicados fusionados por Place Id).
- `clasificacion/RESUMEN-POR-SUBRUBRO.csv` — conteo de negocios por subrubro.
- `clasificacion/MAPA-DE-LLENADO-DESDE-CERO.csv` — los 160 subrubros con su estado: 28 con negocios, 132 vacíos por llenar.
- `clasificacion/clasificar.py` — el script que clasifica.

## Cómo trabajamos

- El dueño edita o sube cambios en este repo → Fuertin los clona a su servidor antes de trabajar.
- Fuertin trabaja en su servidor → sube cada avance a este repo.
- El repo es el espejo compartido: lo que se ve aquí es lo que hay.
