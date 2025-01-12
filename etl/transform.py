import pandas as pd
import logging

def transform(data):

    carritos = []
    productos = []
    carritos_productos = []

    # Extraer datos de productos de cada carrito
    for cart in data["carts"]:
        cart_id = cart["id"]  # ID del carrito
        carritos.append({
        "cart_id": cart["id"],
        "user_id": cart["userId"],
        "total": cart["total"],
        "discounted_total": cart["discountedTotal"],
        "total_products": cart["totalProducts"],
        "total_quantity": cart["totalQuantity"]
        })
        for product in cart["products"]:
            productos.append({
                "product_id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "thumbnail": product["thumbnail"],
            })
            carritos_productos.append({
            "cart_id": cart_id,
            "product_id": product["id"],
            "quantity": product["quantity"],
            "total": product["total"],
            "discounted_total": product["discountedTotal"]
            })

    # Crear un DataFrame para la tabla carritos
    df_carritos = pd.DataFrame(carritos)

    # Crear un DataFrame para la tabla productos
    df_productos = pd.DataFrame(productos)
    df_productos = df_productos.drop_duplicates(subset="product_id")

    # Crear un DataFrame con los datos de carritos_productos
    df_carritos_productos = pd.DataFrame(carritos_productos)

    # Buscar IDs duplicados
    duplicated_ids = df_carritos[df_carritos.duplicated(subset="cart_id", keep=False)]
    if not duplicated_ids.empty:
        logging.info("IDs duplicados encontrados:")
        logging.info(f"\n{duplicated_ids.to_string(index=False)}")   

        # Eliminar duplicados y dejar solo el primer registro
        df_cleaned = df_carritos.drop_duplicates(subset="cart_id", keep="first")   

    if not df_cleaned.empty:
        df_carritos = df_cleaned

    return df_carritos,df_productos,df_carritos_productos

def SaveCSV(df_transformed,df_productos,transformed_data_Car_Products):
    csv_file = "Files/carritos.csv"
    csv_file_prod = "Files/Productos.csv"
    csv_file_Car_prod = "Files/Carrito_Productos.csv"
    df_transformed.to_csv(csv_file, index=False, header=True)
    df_productos.to_csv(csv_file_prod, index=False, header=True)
    transformed_data_Car_Products.to_csv(csv_file_Car_prod, index=False, header=True)
    return csv_file,csv_file_prod,csv_file_Car_prod

