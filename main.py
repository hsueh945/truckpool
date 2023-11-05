from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

# 假设的货物和路线数据库
# 在真实的应用中，这将被替换为数据库调用
FAKE_DATABASE = {
    'loads': [],
    'routes': []
}

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Truckpool API!"

# 添加货物信息
@app.route('/add_load', methods=['POST'])
def add_load():
    data = request.json
    if not data or 'load_id' not in data or 'content' not in data:
        raise BadRequest('Invalid load data.')
    FAKE_DATABASE['loads'].append(data)
    return jsonify({'status': 'success', 'message': 'Load added.'}), 201

# 获取所有货物信息
@app.route('/get_loads', methods=['GET'])
def get_loads():
    return jsonify(FAKE_DATABASE['loads'])

# 添加路线信息
@app.route('/add_route', methods=['POST'])
def add_route():
    data = request.json
    if not data or 'route_id' not in data or 'origin' not in data or 'destination' not in data:
        raise BadRequest('Invalid route data.')
    FAKE_DATABASE['routes'].append(data)
    return jsonify({'status': 'success', 'message': 'Route added.'}), 201

# 获取所有路线信息
@app.route('/get_routes', methods=['GET'])
def get_routes():
    return jsonify(FAKE_DATABASE['routes'])

# 货物匹配逻辑（简化版）
@app.route('/match_load', methods=['POST'])
def match_load():
    data = request.json
    # 这里应该有一个复杂的匹配算法
    # 现在我们只是简单地返回第一个路线
    if FAKE_DATABASE['routes']:
        return jsonify({'matched_route': FAKE_DATABASE['routes'][0]})
    else:
        return jsonify({'status': 'error', 'message': 'No routes available.'})

if __name__ == '__main__':
    app.run(debug=True)