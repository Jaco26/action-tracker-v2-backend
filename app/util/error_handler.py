from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

class ErrorHandler:
  def jsonify_default_exceptions(self, error):
    res = jsonify({
      'code': error.code if isinstance(error, HTTPException) else 500,
      'message': str(error)
    })
    res.status_code = error.code if isinstance(error, HTTPException) else 500
    return res

  def init_app(self, app):
    for code in default_exceptions.keys():
      app.register_error_handler(code, self.jsonify_default_exceptions)