from app import mysql

items = []

def get_items():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shopping_list")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    
    result = []
    for row in rows:
        item_dict = dict(zip(columns, row))
        
        # Modificar el campo booleano
        if 'purchased' in item_dict:
            item_dict['purchased'] = True if item_dict['purchased'] else False
        
        result.append(item_dict)

    return result


def add_item(name):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `shopping_list` (`name`, `purchased`) VALUES (%s, %s)", (name, 0))
    conn.commit()
    cursor.close()
    return True

def get_item(item_id):    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shopping_list WHERE id = %s", (item_id))
    row = cursor.fetchone()

    if row:
        columns = [desc[0] for desc in cursor.description]
    

        item_dict = dict(zip(columns, row))
        
        if 'purchased' in item_dict:
            #item_dict['purchased'] = True if item_dict['purchased'] else False
            item_dict['purchased'] = bool(item_dict['purchased'])

    else:
        item_dict = None
    
    cursor.close()
    conn.close()

    return item_dict


def update_item(item_id, purchased):
    purchasedInt = 1 if purchased else 0
    
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        
        # Ejecutar la actualización
        cursor.execute("UPDATE shopping_list SET purchased = %s WHERE id = %s", (purchasedInt, item_id))
        
        # Confirmar la transacción
        conn.commit()
        
    except mysql.OperationalError as e:
        print("Error al ejecutar la actualización:", e)
        return "Error en la actualización"
    
    finally:
        cursor.close()
        conn.close()
    
    return True

def delete_item(item_id):
    conn = mysql.connection

    cursor = conn.cursor()

    cursor.execute("DELETE FROM shopping_list WHERE id = %s", (item_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return True
    #global items
    #items = [item for item in items if item["id"] != item_id]
    #return items
