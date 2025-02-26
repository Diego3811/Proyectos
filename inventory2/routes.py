from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import Product, User
from extensions import db
import functools

bp = Blueprint('main', __name__)

def role_required(role):
    def decorator(func):
        @functools.wraps(func)
        @login_required
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                flash('Acceso no autorizado', 'danger')
                return redirect(url_for('main.dashboard'))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@bp.route('/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
        flash('Credenciales incorrectas', 'danger')
        return redirect(url_for('main.login'))
    
    login_user(user)
    return redirect(url_for('main.dashboard'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/dashboard')
@login_required
def dashboard():
    inventory_summary = {
        'total_products': Product.query.count(),
        'low_stock': Product.query.filter(Product.quantity < Product.minimum_stock).count(),
        'total_categories': db.session.query(Product.category.distinct()).count(),
        'out_of_stock': Product.query.filter_by(quantity=0).count()
    }
    
    recent_activity = Product.query.order_by(Product.updated_at.desc()).limit(5).all()
    all_products = Product.query.order_by(Product.name).all()
    
    return render_template('dashboard.html', 
                         summary=inventory_summary,
                         activity=recent_activity,
                         products=all_products)

@bp.route('/add-product', methods=['GET', 'POST'])
@role_required('superadmin')
def add_product():
    if request.method == 'POST':
        try:
            new_product = Product(
                name=request.form.get('name'),
                category=request.form.get('category'),
                quantity=int(request.form.get('quantity')),
                price=float(request.form.get('price')),
                minimum_stock=int(request.form.get('minimum_stock')),
                description=request.form.get('description')
            )
            db.session.add(new_product)
            db.session.commit()
            flash('Producto agregado exitosamente', 'success')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar el producto: {str(e)}', 'danger')
    
    return render_template('add_product.html')

@bp.route('/manage-users')
@role_required('superadmin')
def manage_users():
    users = User.query.all()
    return render_template('users.html', users=users)