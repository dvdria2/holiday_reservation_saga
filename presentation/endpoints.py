from flask import Blueprint, request, render_template
from jinja2 import Template

bp = Blueprint('endpoints', __name__, url_prefix='/')


@bp.route('reservation/', methods=("GET", "POST",))
def start_saga_reservation():
    if request.method == "POST":
        pass
    return render_template("reservations/reservation_page.html")