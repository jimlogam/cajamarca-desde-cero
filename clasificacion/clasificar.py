# -*- coding: utf-8 -*-
"""Clasifica negocios de Maps usando INDICE_TAXONOMIA.md (16 macro / 54 rubros / 160 subrubros).
Reglas mecanicas por categoria de Maps + nombre. Un solo subrubro por negocio."""
import csv, re, unicodedata, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

BASE = "/home/hatch/workspace/user/files/"
FILES = ["maps-scraper-1795360118662.csv","maps-scraper-1795360101480.csv",
         "maps-scraper-1795359134163.csv","maps-scraper-1795358120669.csv",
         "maps-scraper-1795358118154.csv"]
OUT = "/home/hatch/workspace/cajamarca-desde-cero/clasificacion/NEGOCIOS-CLASIFICADOS-CAJAMARCA.xlsx"

GASTRO = "01_Gastronomia_y_Cafeterias"
ALIM   = "02_Alimentacion_y_Abastecimiento"
CONST  = "08_Construccion_Ferreteria_y_Hogar"
MODA   = "06_Comercio_Moda_y_Regalos"
TUR    = "12_Turismo_Hoteleria_y_Viajes"
ENTR   = "14_Entretenimiento_y_Eventos"

def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    return "".join(c for c in s if not unicodedata.combining(c))

def has(txt, *words):
    return any(w in txt for w in words)

def classify(name, cats_list):
    """Devuelve (macro, rubro, subrubro, nota)"""
    n = norm(name)
    cats = [norm(c) for c in cats_list if c]
    cat_all = " | ".join(cats)
    first = cats[0] if cats else ""
    nota = ""

    # --- Cadenas / nombres especificos verificables ---
    if n.startswith("gran cajamarca") or has(n, "quesos los andes", "fabrica queso", "queso huacariz"):
        return (ALIM, "Lacteos_y_Tradicion", "Quesos_y_Lacteos_Cajamarquinos", nota)
    if has(n, "cajamarca artesanal", "manjar artesanal"):
        return (ALIM, "Lacteos_y_Tradicion", "Quesos_y_Lacteos_Cajamarquinos", nota)
    if has(n, "lacteos & embutidos", "lacteos y embutidos"):
        return (ALIM, "Lacteos_y_Tradicion", "Embutidos_y_Chacinados", nota)
    if has(n, "sodimac", "promart"):
        return (CONST, "Materiales_y_Ferreteria", "Ferreterias_Generales", nota)

    # --- No gastronomicos por categoria principal ---
    if first.startswith("hotel") or first.startswith("posada") or first == "hotel":
        sub = "Hostales_y_Residenciales" if has(first, "posada", "hostal") else "Hoteles"
        return (TUR, "Alojamiento", sub, nota)
    if first.startswith("supermercado"):
        return (ALIM, "Supermercados_y_Mercados", "Supermercados", nota)
    if first == "mercado":
        return (ALIM, "Supermercados_y_Mercados", "Puestos_de_Mercado_de_Abastos", nota)
    if has(first, "empresa de construccion"):
        return (CONST, "Obras_y_Estructuras", "Constructoras_y_Contratistas", nota)
    if has(first, "tienda de articulos para el hogar", "ferreteria"):
        return (CONST, "Materiales_y_Ferreteria", "Ferreterias_Generales", nota)
    if has(first, "tienda de muebles"):
        return (CONST, "Muebles_y_Decoracion", "Mueblerias", nota)
    if has(first, "tienda de ropa"):
        return (MODA, "Moda_y_Textil", "Ropa_Damas_Caballeros_Ninos", nota)
    if has(first, "tienda de regalos"):
        return (MODA, "Joyerias_y_Detalles", "Regalos_Personalizados_y_Detalles", nota)
    if has(first, "centro comercial"):
        return (MODA, "Moda_y_Textil", "Ropa_Damas_Caballeros_Ninos", "Centro comercial (no es una tienda individual)")
    if first in ("discoteca",) or has(first, "club nocturno"):
        return (ENTR, "Vida_Nocturna", "Discotecas_y_Clubs", nota)
    if has(first, "parque infantil"):
        return (ENTR, "Recreacion_y_Deportes", "Centros_Recreacionales_y_Piscinas", nota)
    if has(first, "atraccion turistica") or first.startswith("parque"):
        return (TUR, "Agencias_y_Operadores", "Turismo_Vivencial_y_Aventura", "Atraccion turistica, no es un negocio")
    if has(first, "tienda de alimentos naturales", "tienda de productos naturales"):
        return (ALIM, "Salud_Alimentaria", "Productos_Naturales_y_Organicos", nota)
    if has(first, "queseria", "tienda de productos lacteos", "fabrica de queso"):
        return (ALIM, "Lacteos_y_Tradicion", "Quesos_y_Lacteos_Cajamarquinos", nota)
    if has(first, "charcuteria"):
        return (ALIM, "Lacteos_y_Tradicion", "Embutidos_y_Chacinados", nota)
    if first == "bodega":
        return (ALIM, "Comercio_Minorista", "Bodegas", nota)
    if has(first, "tienda de alimentacion") and not has(n, "restauran", "polleria", "restaurant"):
        return (ALIM, "Comercio_Minorista", "Minimarkets", nota)
    if first == "comercio" and not has(n, "poll", "restaurant", "restauran"):
        return (ALIM, "Comercio_Minorista", "Minimarkets", nota)

    # ============ GASTRONOMIA ============
    t = n + " | " + cat_all  # texto total nombre+categorias

    # Chifas y comida oriental (sushi/coreano van a restaurante general: la taxonomia no tiene subrubro propio)
    if has(t, "chifa", "restaurante chino", "comida oriental", "java oriental", "wok") or has(n, "chinito", "chino"):
        return (GASTRO, "Restaurantes", "Chifas", nota)
    if has(t, "restaurante asiatico", "fusion asiatica"):
        return (GASTRO, "Restaurantes", "Chifas", nota)

    # Cevicherias y mariscos
    if has(cat_all, "marisqueria") or has(n, "cevicheria", "ceviche", "picanteria", "barra cevichera", "marisqueria"):
        return (GASTRO, "Restaurantes", "Cevicherias_y_Mariscos", nota)

    # Pollerias y parrillas (incluye anticuchos, cilindro, grill, casqueria)
    if has(t, "polleria", "pollo", "chicken", "broaster", "aves de corral"):
        return (GASTRO, "Restaurantes", "Pollerias_y_Parrillas", nota)
    if has(t, "parrilla", "grill", "barbacoa", "anticuch", "cilindro", "chuleta", "filete", "steak",
             "carnes", "churrasq", "casqueria", "asadas", "brasera", "chancho"):
        return (GASTRO, "Restaurantes", "Pollerias_y_Parrillas", nota)

    # Pizzerias y pastas
    if has(t, "pizzeria", "pizza", "pastas", "restaurante italiano", "trattoria", "tienda de pasta"):
        return (GASTRO, "Restaurantes", "Pizzerias_y_Pastas", nota)

    # Juguerias y fuentes de soda (antes que cafeteria/comida rapida)
    if has(t, "jugueria", "jugos", "zumos", "emolient", "fuente de soda", "batipio") or has(n, "jugueria", "frutados"):
        return (GASTRO, "Cafeterias_y_Bebidas", "Juguerias_y_Fuentes_de_Soda", nota)

    # Panaderias y pastelerias
    if has(cat_all, "panaderia") or has(n, "panaderia", "masa madre"):
        return (GASTRO, "Panaderias_y_Pastelerias", "Panaderia_Artesanal", nota)
    if has(t, "pasteleria", "tortas", "postres", "creperia", "heladeria", "gelateria"):
        return (GASTRO, "Panaderias_y_Pastelerias", "Pasteleria_y_Tortas", nota)

    # Cafeterias
    if has(cat_all, "cafeteria") or has(n, "cafe", "coffee"):
        return (GASTRO, "Cafeterias_y_Bebidas", "Cafeterias_de_Especialidad", nota)

    # Vida nocturna (pub / restobar / bar puro / discoteca dentro de categorias de restaurante)
    if has(n, "restobar", "resto-bar", "resto bar") or has(cat_all, "pub restaurante") or has(cat_all, "discoteca", "karaoke"):
        return (ENTR, "Vida_Nocturna", "Restobares_y_Karaokes", nota)
    if first == "bar":
        return (ENTR, "Vida_Nocturna", "Bares_y_Pubs", nota)

    # Hamburguesas y sandwiches
    if has(t, "hamburgues", "burger", "bocateria", "sanguch", "sandwich", "shawarma", "wraps",
             "alas de pollo", "alitas", "banderillas"):
        return (GASTRO, "Comida_Rapida_y_Snacks", "Hamburguesas_y_Sandwiches", nota)

    # Food trucks / food park
    if has(t, "food truck", "food park"):
        return (GASTRO, "Comida_Rapida_y_Snacks", "Food_Trucks", nota)

    # Comida rapida generica -> snacks
    if has(cat_all, "comida rapida", "snack bar"):
        return (GASTRO, "Comida_Rapida_y_Snacks", "Snacks_y_Piques", nota)

    # Menu y comida casera: caldos, sopas, desayunos, brunch, comedor, catering, delivery de comida
    if has(t, "caldo", "sopas", "soperos", "desayunos", "brunch", "comedor", "comida casera",
             "catering", "comida a domicilio", "menu"):
        return (GASTRO, "Restaurantes", "Menu_y_Comida_Casera", nota)

    # Carniceria que en realidad es restaurante/polleria (nombre manda)
    if has(first, "carniceria"):
        return (GASTRO, "Restaurantes", "Tradicional_y_Campestre", nota)

    # Restaurante general: peruano, criollo, campestre, familiar, internacional, fusion, vegetariano, etc.
    if has(cat_all, "restaurante") or has(n, "restaurante", "restaurant", "recreo", "campestre", "cocina"):
        return (GASTRO, "Restaurantes", "Tradicional_y_Campestre", nota)

    # Tienda de bebidas alcoholicas sin otra pista -> bares
    if has(first, "tienda de bebidas alcoholicas"):
        return (ENTR, "Vida_Nocturna", "Bares_y_Pubs", "Categoria Maps: tienda de bebidas alcoholicas")

    return (GASTRO, "Restaurantes", "Tradicional_y_Campestre", "Sin categoria clara en Maps; clasificado como restaurante general")

# ---------- Leer y fusionar duplicados por Place Id ----------
seen = {}
raw = 0
for f in FILES:
    with open(BASE + f, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            raw += 1
            key = (row.get("Place Id") or "").strip() or (norm(row["Name"]) + "|" + norm(row["Fulladdress"]))
            if key in seen:
                seen[key]["_count"] += 1
                for c in (row.get("Categories") or "").split(","):
                    c = c.strip()
                    if c and c not in seen[key]["_cats"]:
                        seen[key]["_cats"].append(c)
                if not seen[key].get("Phone") and row.get("Phone"):
                    seen[key]["Phone"] = row["Phone"]
            else:
                row["_cats"] = [c.strip() for c in (row.get("Categories") or "").split(",") if c.strip()]
                row["_count"] = 1
                seen[key] = row

rows = []
for row in seen.values():
    macro, rubro, sub, nota = classify(row["Name"], row["_cats"])
    if row["_count"] > 1:
        nota = (nota + " " if nota else "") + f"Aparecia {row['_count']} veces en los 5 archivos; fusionado en uno."
    if not row["_cats"]:
        nota = (nota + " " if nota else "") + "Sin categoria en Maps; clasificado por el nombre."
    rows.append({
        "Nombre": row["Name"], "Macro": macro, "Rubro": rubro, "Subrubro": sub,
        "CategoriaMaps": ", ".join(row["_cats"]), "Direccion": row.get("Fulladdress", ""),
        "Telefono": row.get("Phone", ""), "Rating": row.get("Average Rating", ""),
        "Resenas": row.get("Review Count", ""), "Web": row.get("Website", ""),
        "Lat": row.get("Latitude", ""), "Lng": row.get("Longitude", ""),
        "Maps": row.get("Google Maps URL", ""), "PlaceId": row.get("Place Id", ""), "Nota": nota.strip(),
    })

rows.sort(key=lambda r: (r["Macro"], r["Rubro"], r["Subrubro"], norm(r["Nombre"])))

# ---------- XLSX ----------
wb = Workbook()
ws = wb.active
ws.title = "Negocios clasificados"
headers = ["N°", "Nombre", "Macro-Sector", "Rubro", "Subrubro", "Categoria Maps", "Direccion",
           "Telefono", "Rating", "Resenas", "Sitio web", "Latitud", "Longitud", "Google Maps", "Place Id", "Nota"]
ws.append(headers)
hdr_fill = PatternFill("solid", fgColor="0B3D91")
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr_fill
for i, r in enumerate(rows, 1):
    ws.append([i, r["Nombre"], r["Macro"], r["Rubro"], r["Subrubro"], r["CategoriaMaps"], r["Direccion"],
               r["Telefono"], r["Rating"], r["Resenas"], r["Web"], r["Lat"], r["Lng"], r["Maps"], r["PlaceId"], r["Nota"]])
widths = [5, 42, 30, 26, 30, 30, 46, 15, 8, 9, 30, 11, 11, 30, 24, 40]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions

ws2 = wb.create_sheet("Resumen")
ws2.append(["Clasificacion de negocios de Cajamarca — desde cero"])
ws2["A1"].font = Font(bold=True, size=13)
ws2.append(["Archivos recibidos", 5])
ws2.append(["Filas totales en los 5 CSV", raw])
ws2.append(["Negocios unicos (fusionados por Place Id)", len(rows)])
ws2.append(["Duplicados fusionados", raw - len(rows)])
ws2.append([])
ws2.append(["Macro-Sector", "Rubro", "Subrubro", "Negocios"])
for c in ws2[6]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr_fill
cnt = collections.Counter((r["Macro"], r["Rubro"], r["Subrubro"]) for r in rows)
for (m, ru, s), n in sorted(cnt.items()):
    ws2.append([m, ru, s, n])
for i, w in enumerate([32, 28, 34, 10], 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

cnt_macro = collections.Counter(r["Macro"] for r in rows)
wb.save(OUT)
print("RAW", raw, "UNICOS", len(rows), "DUPLICADOS", raw - len(rows))
print("POR MACRO:")
for m, n in cnt_macro.most_common():
    print(" ", n, m)
print("POR SUBRUBRO:")
for (m, ru, s), n in cnt.most_common():
    print(" ", n, m, "/", ru, "/", s)
print("OUT", OUT)
