

from flask import Blueprint, render_template, request, redirect, url_for

locadora_bp = Blueprint(
    "locadora",
    __name__,
    url_prefix="/locadora"
)

@locadora_bp.route("/")
def index():
    return render_template("locadora/lista.html")


@locadora_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        # Aqui futuramente será salva a nova locação no banco de dados.
        # Por enquanto, apenas retorna para a página principal.
        return redirect(url_for("locadora.index"))

    return render_template("locadora/formulario.html")