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

## Lote RUBROOK — 10 fichas verificadas (2026-11-23)

Los 10 archivos `*-TRAB.TXT` de la carpeta **EDEN DODNE VIVEN LAS TIENDAS** (`1miTUHaViVeT6PSIUCHX1O_11JyPHBHDK`) fueron analizados contra la guía de rubros (`INDICE_TAXONOMIA.md`), corregidos y renombrados a `*-RUBROOK.TXT` **sobre el mismo archivo original**, de modo que no queda ningún archivo antiguo al lado.

| Negocio | Rubro verificado | Bytes |
|---|---|---|
| Farmaexpres | 04_Salud/Farmacia_y_Laboratorio/Farmacias_y_Boticas | 20.160 |
| DJR IMPRESIONES | 10_ServProf/Diseno_e_Impresion/Imprentas_y_Gigantografias | 16.940 |
| DISTRIBUIDORA LAZOS | 06_Comercio/Libreria_y_Juegos/Librerias_y_Papelerias | 15.330 |
| Casa Bonita Hostal Boutique | 12_Turismo/Alojamiento/Hostales_y_Residenciales | 12.101 |
| Casa Hacienda Hotel Boutique | 12_Turismo/Alojamiento/Hoteles | 13.372 |
| Ghinza Hotel, Sauna y Spa | 12_Turismo/Alojamiento/Hoteles | 12.354 |
| Allq'u Pet Barber Shop | 16_Agro/Mascotas_y_Veterinaria/Bano_y_Peluqueria_Canina | 17.024 |
| Consultorio Medico Biológico Y Farmacia Verde | 04_Salud/Farmacia_y_Laboratorio/Farmacias_y_Boticas | 21.491 |
| Abogada Civil y de Familia (Katherine Alfaro) | 10_ServProf/Legal_y_Notarial/Estudios_Juridicos_Abogados | 16.350 |
| Estudio Flores y Asociados | 10_ServProf/Finanzas_y_Tributos/Estudios_Contables_y_Tributarios | 15.929 |

Los 10 pasaron validación byte a byte contra `.work/out/` (copia de control en el repo): taxonomía válida en el árbol de 160 subrubros, 20 preguntas y respuestas, bienvenida de 50 a 80 palabras y cierre con la regla `=`.

Nota técnica: los originales pertenecen a otra cuenta de Drive, por lo que la app puede editar contenido y renombrar, pero **no borrar** (`can_delete`/`can_trash` = false). Por eso se reescribió el contenido dentro del mismo archivo y se renombró, en lugar de subir una copia nueva y eliminar la vieja.
