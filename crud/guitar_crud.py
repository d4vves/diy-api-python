from flask import jsonify, redirect
from models import Guitar

def get_all_guitars():
    all_guitars = Guitar.query.all()
    results = [guitar.as_dict() for guitar in all_guitars]
    return jsonify(results)

def get_guitar(id):
    guitar = Guitar.query.get(id)
    if guitar:
        return jsonify(guitar.as_dict())
    else:
        raise Exception(f'No guitar at id {id}.')

def create_guitar(**form_kwargs):
    new_guitar = Guitar(**form_kwargs)
    db.session.add(new_guitar)
    db.session.commit()
    return jsonify(new_guitar.as_dict())

def update_guitar(id, **update_values):
    guitar = Guitar.query.get(id)
    if guitar:
        for key, value in update_values.items():
            setattr(guitar, key, value)
        db.session.commit()
        return jsonify(guitar.as_dict())
    else:
        raise Exception(f'No guitar at id {id}.')

def destroy_guitar(id):
    guitar = Guitar.query.get(id)
    if guitar:
        db.session.delete(guitar)
        db.session.commit()
        return redirect('/guitars')
    else:
        raise Exception(f'No guitar at id {id}.')