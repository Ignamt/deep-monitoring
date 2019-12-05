"""API que expone los métodos del servicio para monitoreo."""
from flask import Flask, jsonify, redirect, url_for


def instance_api():
    """Crea una instancia del objeto WSGI de la API.

    Usamos esta función para poder usar el objeto con pytest y gunicorn.
    """
    api = Flask("api")

    @api.route("/")
    def index():
        return redirect(url_for("alive"))

    @api.route("/alive")
    def alive():
        return jsonify({"alive": True})

    @api.route("/predict", methods=["GET"])
    def predict():
        # TODO: Add an endpoint to return the model's prediction.
        return jsonify(message="La predicción podría ir en este endpoint!")

    return api
