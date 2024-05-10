#importacion de librerias
import pandas as pd
import numpy as np
import math 

#carga de archivos csv para procesar
customer_csv = pd.read_csv('recursos para trabajo integrador\datos\ecommerce_customers_dataset.csv')
order_items_csv = pd.read_csv('recursos para trabajo integrador\datos\ecommerce_order_items_dataset.csv')
order_payments_csv = pd.read_csv('recursos para trabajo integrador\datos\ecommerce_order_payments_dataset.csv')
orders_csv = pd.read_csv('recursos para trabajo integrador\datos\ecommerce_orders_dataset.csv')
products_csv = pd.read_csv('recursos para trabajo integrador\datos\ecommerce_products_dataset.csv')

#conversión de csv a dataframe
df_customers = pd.DataFrame(customer_csv)
df_order_items = pd.DataFrame(order_items_csv)
df_order_payments = pd.DataFrame(order_payments_csv)
df_order = pd.DataFrame(orders_csv)
df_products = pd.DataFrame(products_csv)

def informacion_dfs():
    print(df_customers.info())
    print(df_order_items.info())
    print(df_order.info())
    print(df_order_payments.info())
    print(df_products.info())
