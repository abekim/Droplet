"""
Error handlers

author: @abekim
"""
from blogger import app
from flask import jsonify

@app.errorhandler(404)
def not_found_exception(e):
    """
    404 "Not Found" handler
    """
    app.logger.error(e)
    return jsonify(ERROR="Not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    500 "Internal Server Error" handler
    """
    app.logger.error(e)
    return jsonify(ERROR="There was an internal server error while processing your request.\nError message from the server: %s" % e), 500