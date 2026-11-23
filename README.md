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

## Lote RUBROOK — 30 fichas de negocios de Cajamarca (2026-11-23)

Segundo lote, en la misma carpeta de Drive. Los 30 originales fueron verificados contra `INDICE_TAXONOMIA.md`, `clasificacion/BASE-COMPLETA-4693.csv` y las fichas locales de `TIENDAS/`: se confirmó o corrigió macro-sector/rubro/subrubro, se regeneró el cuerpo completo (20 preguntas y respuestas, sin residuos de otro rubro) y se renombraron a `*-RUBROOK.TXT` sobre el mismo archivo, ya que la cuenta dueña de los originales no permite borrar.

| Negocio | Subrubro asignado | Bytes |
|---|---|---|
| DELICIA EXPRESS LEIVA | 02_Alimentacion/Productos_Naturales_y_Organicos | 12.922 |
| Complejo Turístico Sierra Verde | 12_Turismo/Alojamiento/Alojamientos_Campestres | 8.812 |
| Cochera La Hacienda | 15_Logistica/Estacionamientos_y_Cocheras | 9.369 |
| Califa Motors | 03_Automotriz/Venta_de_Vehiculos_Nuevos_y_Usados | 9.566 |
| Brasero Chicken Bar | 01_Gastronomia/Pollerias_y_Parrillas | 19.998 |
| BORDADOS COMPUTARIZADOS - CAJATEX | 07_ServTecnicos/Sastres_y_Modistas | 9.200 |
| Grupo Sierra Verde | 12_Turismo/Agencias_de_Viajes_y_Tours | 8.699 |
| DOÑA VIVI distribuciones avícolas | 02_Alimentacion/Distribuidoras_Mayoristas | 9.008 |
| CIVA - Transporte y Turismo Terminal Cajamarca | 15_Logistica/Terminales_y_Empresas_Interprovinciales | 10.939 |
| Etwonailsbeautycamajarcabyeve | 05_Belleza/Manicure_y_Pedicure | 8.893 |
| Energia y minas | 10_ServProf/Tramites_y_Asesoria_Legal | 9.192 |
| Empresa de Transportes Namora S.R.L | 15_Logistica/Terminales_y_Empresas_Interprovinciales | 9.301 |
| EMPRESA DE TRANSPORTES AVE FENIX | 15_Logistica/Couriers_y_Envio_de_Encomiendas | 19.942 |
| FOGÓN DORADO 3 | 01_Gastronomia/Pollerias_y_Parrillas | 19.956 |
| Empresa de Transportes Corazón Celendino | 15_Logistica/Couriers_y_Envio_de_Encomiendas | 9.438 |
| Fotocopiadora y Librería Lectores | 06_Comercio/Librerias_y_Papelerias | 8.593 |
| Galerías Arcángel - JAGUILAR | 06_Comercio/Calzado_y_Zapaterias | 20.983 |
| Grifo Las Vegas - La Paz - Miraflores | 15_Logistica/Estaciones_de_Servicio_Grifos | 10.091 |
| Golf Chicken | 01_Gastronomia/Pollerias_y_Parrillas | 19.845 |
| Hermes Transportes Blindados, Cajamarca | 10_ServProf/Seguridad_Privada_y_Custodia | 9.047 |
| I. E. P. Pequeñas Travesuras | 13_Educacion/Nidos_y_Guarderias | 19.316 |
| H y M Almacenes Generales Srl | 06_Comercio/Librerias_y_Papelerias | 8.422 |
| Hacienda Meléndez | 14_Entretenimiento/Salones_de_Recepciones_y_Eventos | 8.908 |
| Fotocopias Strong | 08_Tecnologia/Cabinas_e_Impresion_Digital | 8.506 |
| Dulce Fiesta Cajamarca | 01_Gastronomia/Pasteleria_y_Tortas | 9.706 |
| Concesionario SAC | 03_Automotriz/Venta_de_Vehiculos_Nuevos_y_Usados | 8.902 |
| Complejo Deportivo Perú Bicolor | 14_Entretenimiento/Canchas_Sinteticas_y_Complejos | 8.535 |
| Hotel La Hispana | 12_Turismo/Hoteles | 12.291 |
| Hiper Asia | 02_Alimentacion/Supermercados | 12.870 |
| Hotel & Spa Laguna Seca | 12_Turismo/Hoteles | 14.298 |

Reclasificaciones: Hiper Asia (Bazares_y_Regalos → Supermercados), Dulce Fiesta y Hacienda Meléndez (Salones → Pastelería / Salones de eventos de Trujillo), Galerías Arcángel (Cines y centros culturales → Calzado), Cochera La Hacienda (Energía → Estacionamientos), AVE FENIX y Corazón Celendino (Pasajeros → Couriers), Namora y CIVA (Carga → Terminales), CAJATEX (Bordados → Sastres), Energia y minas (Legal por trámites mineros), DOÑA VIVI (Distribuidoras mayoristas avícolas), Fotocopias Strong (Cabinas e impresión digital), Etwonails (Manicure), Complejo Deportivo Perú Bicolor (Canchas sintéticas), Pequeñas Travesuras (Nidos y guarderías).

Verificación: cada archivo se descargó desde Drive y se comparó byte a byte contra `.work/out30/` → **30/30 idénticos**. Los 30 pasan la validación de formato: UTF-8, LF, bienvenida de 50 a 80 palabras, exactamente 20 preguntas y respuestas, cierre con la regla `=` de 80 caracteres, y sin tildes fuera de `¡¿` en las respuestas. Las distancias a Plaza de Armas, Mercado Central, Mercado Modelo, Real Plaza, MegaPlaza, Terminal y Aeropuerto se calcularon por haversine desde las coordenadas de `BASE-COMPLETA-4693.csv`; no se inventaron teléfonos ni distancias.

Duplicados ajenos no borrables: `Empresa de Transportes Namora` (`1O36vuCKPioj5IBLHWAgJYdecBPOyVnVS`) y `Energia y minas` (`1Re62wERGBOHFGSBW5wKX4QqziN61k7P7`) siguen en la carpeta, con una copia de 21 KB y 20 KB respectivamente, fuera de este lote.
