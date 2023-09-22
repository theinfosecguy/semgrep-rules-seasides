def get_user_by_id(input_id):
    return create_query("SELECT * FROM User WHERE id = '" + input_id + "'")

def get_user_by_id_v(input_id):
    query = "SELECT * FROM User WHERE id = ?"
    return create_query(query, input_id)
