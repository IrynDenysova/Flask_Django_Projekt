from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.models import db, Question, Category

from app.schemas.category import CategoryResponse, CategoryCreate

categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/', methods=['GET'])
def get_categories():
    """Получение списка всех категорий."""

    categories = db.session.query(Category).all()

    categories_data = [CategoryResponse.model_validate(cat).model_dump() for cat in categories]

    return jsonify(categories_data), 200


@categories_bp.route('/', methods=['POST'])
def create_category():
    """Создание новой категории."""
    try:
        category_data = CategoryCreate.model_validate_json(request.data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category = Category(name=category_data.name)
    db.session.add(category)
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(category).model_dump()), 201


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Обновление конкретной категории по ее ID."""
    print(id)

    category = db.session.query(Category).filter(Category.id == id).one_or_none()
    if category is None:
        return jsonify({'message': "Категория с таким ID не найдена"}), 404

    data = request.get_json()

    if data and data.get('name'):
        category.name = data['name']
        db.session.commit()
        return jsonify({'message': f"Категория обновлена: {category.name}"}), 200

    return jsonify({'message': "Категория не предоставлена"}), 400


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Удаление конкретной категории по ее ID."""
    category = db.session.query(Category).filter(Category.id == id).one_or_none()
    if category is None:
        return jsonify({'message': "Категория с таким ID не найдена"}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f"Категория с ID {id} удалена"}), 200
