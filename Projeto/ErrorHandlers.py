from Server import App
from flask import jsonify

@App.errorhandler(400)
def tratarError400(error):
   return jsonify()

@App.errorhandler(403)
def tratarError403(error):
   return jsonify()

@App.errorhandler(404)
def tratarError404(error):
   return jsonify()

@App.errorhandler(500)
def tratarError500(error):
   return jsonify()