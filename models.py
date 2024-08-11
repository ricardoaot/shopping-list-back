items = []

def get_items():
    return items

def add_item(name):
    item = {"id": len(items) + 1, "name": name, "purchased": False}
    # item = {"id": len(items) + 1, "name": name}
    items.append(item)
    return item

def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None

def update_item(item_id, purchased):
# def update_item(item_id, name):
    item = get_item(item_id)
    if item:
        # item["name"] = name
        item["purchased"] = purchased
        return item
    return None

def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return items
