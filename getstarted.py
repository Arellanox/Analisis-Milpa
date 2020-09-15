import pandas as pd

DATAFRAME = "data/febrero.csv"

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
        new_list.append({"cliente": cliente, "ticket_medio": data[cliente].median()})

    # creamos una lista vacia para guardar los nombre de los clientes
    c = list()
    # creamos una lista vacia para guardar los tickets medios
    t = list()

    # llenamos la lista de los clientes
    for x in new_list:
        c.append(x["cliente"])

    # llenamos la lista con los tickets medios de compra
    for x in new_list:
        t.append(x["ticket_medio"])

    # creamos un nuevo dataframe con los datos de las listas c y t 
    ticket_medio = pd.DataFrame({
        "cliente": c,
        "tm": t
    })

    # imprimimos el ticket medio de mayor a menor
    return ticket_medio.sort_values("tm", ascending=False)


def get_kilos_vendidos():
    filtrar_kilos = ventas[ventas["Cat"]=="KG"]
    kilos_vendidos = filtrar_kilos["Kilos/pza"].sum()
    
    return kilos_vendidos


def get_pzas_vendidas():
    filtrar_pza = ventas[ventas["Cat"]=="PZA"]
    pzas_vendidas = filtrar_pza["Kilos/pza"].sum()
    
    return pzas_vendidas


def get_cantidad_acumulada_por_producto():
    productos = ventas.groupby(["Productos"])["Precio neto"].sum()

    return productos.sort_values(ascending=False)


def get_ventas_dias():
    dias = ventas.groupby(["Fecha"])["Precio neto"].sum()

    return dias.sort_values(ascending=False)


def get_dias_semana_mas_ventas():
    dia_semana = ventas.groupby(["semana"])["Precio neto"].sum()

    return dia_semana.sort_values(ascending=False)


# Impresion de ticket medio
tm = get_ticket_medio()
print("TICKET MEDIO POR CLIENTE-------------------")
print(tm)
print("TERMINA EL TICKET MEDIO--------------------")

# Kilos vendidos
kv = get_kilos_vendidos()
print("KILOS VENDIDOS----------------------------")
print(f'Kilos vendidos: {kv}')
print("TERMINA KILOS VENDIDOS----------------------------")

# Pzas vendidas
pv = get_pzas_vendidas()
print("PIEZAS VENDIDAS----------------------------")
print(f'Piezas vendidas: {pv}')
print("TERMINA PIEZAS VENDIDAS----------------------------")

# Cantidad acumulada por productos
productos = get_cantidad_acumulada_por_producto()
print("INGRESOS POR PRODUCTO----------------------------")
print(productos)
print("TERMINA INGRESOS POR PRODUCTO----------------------------")

# días con mayor venta
dias = get_ventas_dias()
print("VENTAS POR FECHA----------------------------")
print(dias)
print("TERMINA VENTAS POR FECHA----------------------------")

# Dia de la semana que más se vende
dia_semana = get_dias_semana_mas_ventas()
print("VENTAS POR DIA ----------------------------")
print(dia_semana)
print("TERMINA VENTAS POR DIA ----------------------------")