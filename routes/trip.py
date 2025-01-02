from flask import Blueprint, jsonify, request
import Database as db
import pandas as pd

trip_bp = Blueprint('trip', __name__)

db = db.Database()


@trip_bp.route("/producte", methods=["GET"])
@trip_bp.route("/producte/<producte>", methods=["GET"])
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
    return jsonify(data)


# Rutes per Client
@trip_bp.route('/client')
@trip_bp.route('/client/<client>')
def clientByPes(client=None):
    if client:
        sql = 'SELECT client, SUM(pes) as pes FROM products WHERE LOWER(client) = LOWER(?) GROUP BY client'
        params = (client,)
    else:
        sql = 'SELECT client, SUM(pes) as pes FROM products GROUP BY client'
        params = ()

    rows, columns = db.query(sql, params)
    data = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
    return jsonify(data)


# Rutes per Data


@trip_bp.route('/data')
@trip_bp.route('/data/<year>')
def dataByPes(year=None):
    if year:
        sql = 'SELECT "data entrega", SUM(pes) as pes  FROM products WHERE strftime("%Y", "data entrega") = ? GROUP BY "data entrega"'
        params = (year,)
    else:
        sql = 'SELECT "data entrega", SUM(pes) as pes FROM products GROUP BY "data entrega"'
        params = ()
    rows, columns = db.query(sql, params)
    data = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
    return jsonify(data)


# Rutes per Transportista


@trip_bp.route('/transportista')
@trip_bp.route('/transportista/<transportista>')
def transportistaByPes(transportista=None):

    if transportista:
        sql = 'SELECT transportista, SUM(pes) as pes FROM products WHERE transportista = ? GROUP BY transportista'
        params = (transportista,)
    else:
        sql = 'SELECT transportista, SUM(pes) as pes FROM products GROUP BY transportista'
        params = ()

    rows, columns = db.query(sql, params)
    data = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
    return jsonify(data)


# Rutes per Destí


@trip_bp.route('/desti')
@trip_bp.route('/desti/<desti>')
def destiByPes(desti=None):

    if desti:
        sql = 'SELECT desti, SUM(pes) as pes FROM products WHERE desti = ? GROUP BY desti'
        params = (desti,)
    else:
        sql = 'SELECT desti, SUM(pes) as pes FROM products GROUP BY desti'
        params = ()

    rows, columns = db.query(sql, params)
    data = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
    return jsonify(data)
