import server as s
from flask import Blueprint, jsonify, request, current_app
import Database as db
import pandas as pd
from Extensions import Graphs as gp
plot_bp = Blueprint('plot', __name__)
db = db.Database()
gp = gp.Graph(True)


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
    data = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
    gp.generate_graph(data, 'producte', 'pes', 'Pes total per producte')
