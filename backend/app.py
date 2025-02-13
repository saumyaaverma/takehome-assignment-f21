from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """

    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    minimum_episodes = request.args.get("minEpisodes")
    if(minimum_episodes == None):
        return create_response({"shows": db.get('shows')})
    else:
        shows = db.get('shows')
        min_list = []
        for show in shows:
            if(show["episodes_seen"] >= int(minimum_episodes)):
                min_list.append(show)
        if(len(min_list) == 0):
            return create_response(status=404, message="No shows with episodes gretater or equal than this exist")
        return create_response({"shows": min_list})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


@app.route("/shows/<id>", methods=['GET'])
def get_show(id):
    try:
        if db.getById('shows', int(id)) is None:
            return create_response(status=404, message="No show with this id exists")
        db.getById('shows', int(id))
        return create_response((db.get('shows')[int(id)-1]))
    except:
        return create_response(status=404, message="No show with this id exists")


@app.route("/shows", methods=['POST'])
def post_show():
    if "episodes_seen" not in request.json and "name" not in request.json:
        return create_response(status=422, message="name and episodes_seen parameter missing") 
    elif "name" not in request.json:
        return create_response(status=422, message="name parameter missing") 
    elif "episodes_seen" not in request.json:
        return create_response(status=422, message="episodes_seen parameter missing")    
    else: 
        dict = db.create("shows", request.json)
        return create_response(dict, status = 201)

@app.route("/shows/<id>", methods=['PUT'])
def update_show(id):
    try:
        if db.getById('shows', int(id)) is None:
            return create_response(status=404, message="No show with this id exists")
        if "name" in request.json:
            db.getById('shows', int(id))["name"] = request.json["name"]
        if "episodes_seen" in request.json:
            db.getById('shows', int(id))["episodes_seen"] = request.json["episodes_seen"]
        db.updateById("shows", id, request.json)
        dict = ((db.get('shows')[int(id)-1]))
        return create_response(dict, status = 201)
    except:
        return create_response(status=404, message="No show with this id exists")
#TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
