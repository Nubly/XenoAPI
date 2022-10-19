from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from core import app
from schemas import schema
import sqlalchemy


@app.route("/api/v1/hydro", methods=["GET"])
def test_response():
    return "The API is working!\nCome back soon for more updates!"
# def graphql_playground():
#     return PLAYGROUND_HTML, 200

@app.route("/api/v1/hydro", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema=schema, data=data, context_value=request, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    Session = Session()
    app.run(debug=True)
