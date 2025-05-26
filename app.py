# --- User Management ---
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def manage_users():
    if request.method == 'GET':
        return jsonify(list(users.values()))
    elif request.method == 'POST':
        data = request.json
        name = data.get('name', '').strip()
        if not name:
            return jsonify({'error':'Name required'}), 400
        user_id = str(uuid.uuid4()) #generates unique uuid
        users[user_id] = {'id': user_id, 'name': name}
        return jsonify(users[user_id]), 201
    elif request.method == 'DELETE':
        user_id = request.args.get('id')
        if user_id in users:
            del users[user_id]
            # Remove user's borrowed books
            for tx in list(transactions):
                if tx['user_id'] == user_id:
                    transactions.remove(tx)
            return '', 204
        return 'User not found', 404
