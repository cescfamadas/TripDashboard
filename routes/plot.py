import server as s
from flask import Blueprint, jsonify, request, current_app
import Database as db
import pandas as pd
from Extensions import Graph as gp
plot_bp = Blueprint('plot', __name__)
db = db.Database()


@ plot_bp.route("/producte", methods=["GET"])
@ plot_bp.route("/producte/<producte>", methods=["GET"])
def pesTotalByProduct(producte=None):
    """
    Retorna el pes total per producte
    ---
    parameters:
      - name: producte
        in: query
        type: string
        required: false
        description: Nom del producte
    responses:
      200:
        description: Pes total per producte
        schema:
          id: pes_total_per_producte
    """
    if producte:
        sql = "SELECT producte, SUM(pes) as pes FROM products WHERE producte = ? GROUP BY producte"
        params = (producte,)
    else:
        sql = "SELECT producte, SUM(pes) as pes FROM products GROUP BY producte"
        params = ()

    rows, columns = db.query(sql, params)
    data = pd.DataFrame(rows, columns=columns,)
    plot_div = gp.generate_bar(
        data=data, x_label='producte', y_label='pes', title='Pes total per producte')

    return plot_div
