from flask import Flask, jsonify
from config import Config
from models import db, ProfessionalLevel, Markup, CourseDraft

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # --- ROTA INICIAL DE TESTE ---
    @app.get("/")
    def home():
        return "<h2>API funcionando ✅</h2><p>Use /health, /seed ou /levels para testar.</p>"

    # --- ROTA DE SAÚDE ---
    @app.get("/health")
    def health():
        return jsonify(status="ok")

    # --- ROTA PARA POPULAR O BANCO ---
    @app.route("/seed", methods=["GET", "POST"])
    def seed():
        created_levels = False
        created_markups = False

        if not ProfessionalLevel.query.first():
            db.session.add_all([
                ProfessionalLevel(name="NÍVEL I", hourly_total=63.24),
                ProfessionalLevel(name="NÍVEL II", hourly_total=84.32),
                ProfessionalLevel(name="NÍVEL III", hourly_total=107.88),
            ])
            created_levels = True

        if not Markup.query.first():
            db.session.add_all([
                Markup(category="LIVRE", label="Marketing", pct=4),
                Markup(category="LIVRE", label="Evasão", pct=5),
                Markup(category="LIVRE", label="Inadimplência", pct=1),
                Markup(category="LIVRE", label="Descontos", pct=20),
                Markup(category="LIVRE", label="Taxa Admin", pct=3),
                Markup(category="LIVRE", label="Margem", pct=10),
            ])
            created_markups = True

        if created_levels or created_markups:
            db.session.commit()
            return jsonify(ok=True, message="Dados inseridos com sucesso.")
        else:
            return jsonify(ok=True, message="Nada a inserir — já existe conteúdo no banco.")

    # --- ROTA PARA RETORNAR NÍVEIS ---
    @app.get("/levels")
    def get_levels():
        levels = ProfessionalLevel.query.order_by(ProfessionalLevel.id).all()
        return jsonify([
            {"id": l.id, "name": l.name, "hourly_total": float(l.hourly_total)}
            for l in levels
        ])

    return app
