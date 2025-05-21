# --- User Management ---
@app.route('/users', methods=['GET'])
def manage_users():
    if request.method == 'GET':
        return jsonify(list(users.values()))
