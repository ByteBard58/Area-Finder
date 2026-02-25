from flask import Flask, render_template, request, jsonify
import numpy as np
from area_finder import area_sc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        coordinates = data.get('coordinates', [])
        assume_unordered = data.get('assume_unordered', False)

        if len(coordinates) < 3:
            return jsonify({'success': False, 'error': 'At least 3 vertices are required to form a polygon.'}), 400

        # Validate and convert to float
        target_coords = []
        for coord in coordinates:
            try:
                x, y = float(coord['x']), float(coord['y'])
                target_coords.append([x, y])
            except (ValueError, TypeError):
                return jsonify({'success': False, 'error': f'Invalid coordinate provided: {coord}. Must be numbers.'}), 400

        target_array = np.array(target_coords)
        
        area = area_sc(target_array, assume_unordered=assume_unordered)
        
        if area == 0:
            return jsonify({'success': True, 'area': 0, 'message': 'The provided points are collinear and do not form an enclosed shape.'})
        
        return jsonify({'success': True, 'area': float(area)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)
