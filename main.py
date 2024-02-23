from flask import Flask, make_response, jsonify, request
from bd import cars

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/cars", methods=['GET', 'POST'])
def cars_methods():
    if request.method == 'GET':
        return make_response( jsonify(
                message='Cars list',
                data= cars
            ))
    elif request.method == 'POST':
        car = request.json
        cars.append(car)
        return make_response(
            jsonify(
                message='Car registered!',
                data=car
            )
        )

@app.route("/cars/del", methods=['DELETE'])
def delete_car():
    return make_response(
        jsonify(
            cars.pop()
        )
    )

app.run()