from flask import request, jsonify, render_template
from app import app, socketio
from models import get_items, add_item, get_item, update_item, delete_item

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    #return 'Socket.IO server is running'

@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(get_items())

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    item = add_item(name)
    socketio.emit('itemAdded', item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    item = get_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item_view(item_id):
    data = request.json
    purchased = data.get('purchased')
    item = update_item(item_id, purchased)
    if item:
        socketio.emit('itemUpdated', item)
        return jsonify({'message': 'Item updated successfully'}), 204
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item_view(item_id):
    try:
        delete_item(item_id)
        socketio.emit('itemDeleted', item_id)
        response = {'message': 'Item deleted successfully'}
        return jsonify(response), 204
    except Exception as e:
        print("Error during delete process:", e)
        return jsonify({'error': 'An error occurred'}), 500


