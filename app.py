# --- User Management ---
@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        return jsonify(list(users.values()))
    elif request.method == 'POST':
        data = request.json
        name = data.get('name', '').strip()
        if not name:
            return jsonify({'error':'Name required'}), 400
        user_id = str(len(users) + 1)
        users[user_id] = {'id': user_id, 'name': name}
        return jsonify(users[user_id]), 201
