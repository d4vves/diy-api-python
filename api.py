from models import app, Guitar
from flask import jsonify, request
from crud.guitar_crud import get_all_guitars, get_guitar, create_guitar, update_guitar, destroy_guitar

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error(f'Unhandled Exception: {e}')
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])

@app.route('/guitars', methods=['GET', 'POST'])
def guitar_index_create():
    if request.method == 'GET':
        return get_all_guitars()
    else:
        return create_guitar(**request.form)

@app.route('/guitars/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def guitar_show_put_delete(id):
    if request.method == 'GET':
        return get_guitar(id)
    if request.method == 'PUT':
        return(update_guitar(id, **request.form))
    if request.method == 'DELETE':
        return(destroy_guitar(id))