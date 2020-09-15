import pandas as pd
from pandas import ExcelWriter

DATAFRAME = "data/enero.csv"
WRITER = ExcelWriter("analizado/AnalisisEnero2020.xlsx")

ventas = pd.read_csv(DATAFRAME, encoding='latin-1')

new_list = list()
def get_ticket_medio():
    # muestro solo la columna de cliente, fecha y suma el precio neto mostrando el resultado como tercera columna
    data = ventas.groupby(["Cliente","Fecha"])["Precio neto"].sum()
    # quitamos los nombre duplicados del dataframe y los ordenamos alfabeticamente
    eliminar_clientes_duplicados = ventas.drop_duplicates(subset="Cliente").sort_values("Cliente")
    # creamos un subset que solo contenga los nombre de los clientes
    clientes = eliminar_clientes_duplicados["Cliente"]

    for cliente in clientes:
        # llenamos la lista con el nombre del cliente y el promedio de compra
        new_list.append({"cliente": cliente, "ticket_medio": data[cliente].mean(), "compras": data[cliente].count()})

    # creamos una lista vacia para guardar los nombre de los clientes
    c = list()
    # creamos una lista vacia para guardar los tickets medios
    t = list()
    # creamos una lista vacia para guardar le numeor de compras
    compras = list()

    # llenamos la lista de los clientes
    for x in new_list:
        c.append(x["cliente"])

    # llenamos la lista con los tickets medios de compra
    for x in new_list:
        t.append(x["ticket_medio"])

    for x in new_list:
        compras.append(x["compras"])

    # creamos un nuevo dataframe con los datos de las listas c y t 
    ticket_medio = pd.DataFrame({
        "cliente": c,
        "tm": t,
        "compras": compras
    })

    ticket_medio.to_excel(WRITER, "Ticket Medio", index=False)
    #writer.save()

    # imprimimos el ticket medio de mayor a menor
    return ticket_medio.sort_values("tm", ascending=False)


def get_kilos_vendidos():
    filtrar_kilos = ventas[ventas["Cat"]=="KG"]
    kilos_vendidos = filtrar_kilos["Kilos/pza"].sum()

    # kilos = pd.DataFrame({
    #     "kilos vendidos totales": kilos_vendidos[0]
    # })
    
    # kilos.to_excel(WRITER, "Kilos vendidos", index=False)

    return kilos_vendidos


def get_pzas_vendidas():
    filtrar_pza = ventas[ventas["Cat"]=="PZA"]
    pzas_vendidas = filtrar_pza["Kilos/pza"].sum()

    # pzas_vendidas.to_excel(WRITER, "Piezas vendidas", index=False)
    
    return pzas_vendidas


def get_cantidad_acumulada_por_producto():
    productos = ventas.groupby(["Productos"])["Precio neto"].sum()
    eliminar_productos_duplicados = ventas.drop_duplicates(subset="Productos").sort_values("Productos")
    productos_label = eliminar_productos_duplicados["Productos"]
    nueva_lista = list()
    for x in productos_label:
        nueva_lista.append({"productos": x, "ingreso": productos[x]})

    labels = list()
    ingresos = list()

    for x in nueva_lista:
        labels.append(x["productos"])

    for x in nueva_lista:
        ingresos.append(x["ingreso"])

    newdf = pd.DataFrame({
        "Productos": labels,
        "Ingreso ($)": ingresos
    })

    newdf.to_excel(WRITER, "Ingreso por productos", index=False)

    return productos.sort_values(ascending=False)

def get_kilos_pzas_acumulados_por_producto():
    productos = ventas.groupby(["Productos"])["Kilos/pza"].sum()
    eliminar_productos_duplicados = ventas.drop_duplicates(subset="Productos").sort_values("Productos")
    productos_label = eliminar_productos_duplicados["Productos"]
    nueva_lista = list()
    for x in productos_label:
        nueva_lista.append({"productos": x, "kilos/pzas": productos[x]})

    labels = list()
    kilos = list()

    for x in nueva_lista:
        labels.append(x["productos"])

    for x in nueva_lista:
        kilos.append(x["kilos/pzas"])

    newdf = pd.DataFrame({
        "Productos": labels,
        "Kilos/pzas": kilos
    })


    newdf.to_excel(WRITER, "Kilos por productos", index=False)

    return productos.sort_values(ascending=False)


def get_ventas_dias():
    dias = ventas.groupby(["Fecha"])["Precio neto"].sum()
    eliminar_fechas_duplicadas = ventas.drop_duplicates(subset="Fecha").sort_values("Fecha")
    fechas_label = eliminar_fechas_duplicadas["Fecha"]

    nueva_lista = list()

    for fecha in fechas_label:
        nueva_lista.append({"fecha": fecha, "ventas": dias[fecha]})

    dates = list()
    ingresos = list()

    for x in nueva_lista:
        ingresos.append(x['ventas'])

    for x in nueva_lista:
        dates.append(x['fecha'])

    newdf = pd.DataFrame({
        "Fecha": dates,
        "Ventas ($)": ingresos
    })

    newdf.to_excel(WRITER, "Ingreso por fecha", index=False)

    return dias.sort_values(ascending=False)


def get_dias_semana_mas_ventas():
    dia_semana = ventas.groupby(["semana"])["Precio neto"].sum()
    eliminar_dias_duplicados = ventas.drop_duplicates(subset="semana").sort_values("semana")
    dias_label = eliminar_dias_duplicados["semana"]
    nueva_lista = list()

    for dia in dias_label:
        nueva_lista.append({"dia": dia, "venta": dia_semana[dia]})

    days = list()
    venta = list()

    for x in nueva_lista:
        days.append(x["dia"])

    for x in nueva_lista:
        venta.append(x["venta"])

    newdf = pd.DataFrame({
        "Día de la semana": days,
        "Ventas ($)": venta
    })

    newdf.to_excel(WRITER, "Ingreso por dia de la semana", index=False)

    return dia_semana.sort_values(ascending=False)


# Impresion de ticket medio
tm = get_ticket_medio()
# print("TICKET MEDIO POR CLIENTE-------------------")
# print(tm)
# print("TERMINA EL TICKET MEDIO--------------------")

# Kilos vendidos
kv = get_kilos_vendidos()
# print("KILOS VENDIDOS----------------------------")
# print(f'Kilos vendidos: {kv}')
# print("TERMINA KILOS VENDIDOS----------------------------")

# Pzas vendidas
pv = get_pzas_vendidas()
# print("PIEZAS VENDIDAS----------------------------")
# print(f'Piezas vendidas: {pv}')
# print("TERMINA PIEZAS VENDIDAS----------------------------")

# Cantidad acumulada por productos
productos = get_cantidad_acumulada_por_producto()
# print("INGRESOS POR PRODUCTO----------------------------")
# print(productos)
# print("TERMINA INGRESOS POR PRODUCTO----------------------------")

# Kilos/piezas acumuladas por producto
# print("KILOS ACUMULADOS POR PRODUCTO----------------------------")
productos2 = get_kilos_pzas_acumulados_por_producto()
# print(productos2)
# print("FIN KILOS ACUMULADOS POR PRODUCTO----------------------------")

# días con mayor venta
dias = get_ventas_dias()
# print("VENTAS POR FECHA----------------------------")
# print(dias)
# print("TERMINA VENTAS POR FECHA----------------------------")

# Dia de la semana que más se vende
dia_semana = get_dias_semana_mas_ventas()
print("VENTAS POR DIA ----------------------------")
print(dia_semana)
print("TERMINA VENTAS POR DIA ----------------------------")

WRITER.save()