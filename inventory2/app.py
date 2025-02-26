from flask import Flask
from extensions import db, login_manager
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    
    # Configuración de la base de datos
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(basedir, 'instance')
    
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, "inventory.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    
    # Configurar loader de usuarios
    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    from routes import bp
    app.register_blueprint(bp)
    
    return app

app = create_app()

# Comandos CLI
@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
    print("✅ Base de datos creada exitosamente!")

@app.cli.command("create-superadmin")
def create_superadmin():
    from models import User
    with app.app_context():
        admin = User(username='superadmin', role='superadmin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
    print("✅ Superadmin creado: usuario: superadmin / contraseña: admin123")

@app.cli.command("create-admin")
def create_admin():
    from models import User
    with app.app_context():
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
    print("✅ Admin creado: usuario: admin / contraseña: admin123")

if __name__ == '__main__':
    print("⚠️ Iniciando servidor...")
    app.run(host='0.0.0.0', port=5000, debug=True)
    {{ edit_1 }}
    print(f"Servidor en ejecución en http://0.0.0.0:5000")