from flask import Flask, request, jsonify


app = Flask(__name__)

zodiac_compatibility = {
        'Aries': {'Gemini': 60, 'Leo': 80, 'Sagittarius': 70, 'Cancer': 40, 'Capricorn': 50},
        'Taurus': {'Cancer': 80, 'Virgo': 70, 'Capricorn': 60, 'Gemini': 40, 'Sagittarius': 50},
        'Gemini': {'Libra': 80, 'Aquarius': 70, 'Leo': 60, 'Cancer': 40, 'Virgo': 50},
        'Cancer': {'Scorpio': 80, 'Pisces': 70, 'Taurus': 60, 'Gemini': 40, 'Aquarius': 50},
        'Leo': {'Sagittarius': 80, 'Aries': 70, 'Libra': 60, 'Cancer': 40, 'Capricorn': 50},
        'Virgo': {'Capricorn': 80, 'Taurus': 70, 'Scorpio': 60, 'Gemini': 40, 'Sagittarius': 50},
        'Libra': {'Aquarius': 80, 'Gemini': 70, 'Leo': 60, 'Cancer': 40, 'Pisces': 50},
        'Scorpio': {'Pisces': 80, 'Cancer': 70, 'Virgo': 60, 'Taurus': 40, 'Aquarius': 50},
        'Sagittarius': {'Aries': 80, 'Leo': 70, 'Aquarius': 60, 'Gemini': 40, 'Virgo': 50},
        'Capricorn': {'Taurus': 80, 'Virgo': 70, 'Scorpio': 60, 'Aries': 40, 'Libra': 50},
        'Aquarius': {'Libra': 80, 'Gemini': 70, 'Sagittarius': 60, 'Cancer': 40, 'Scorpio': 50},
        'Pisces': {'Scorpio': 80, 'Cancer': 70, 'Capricorn': 60, 'Taurus': 40, 'Leo': 50}
    }

zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    

@app.route('/zodiac-compatibility', methods=['GET'])
def get_zodiac_compatibility():
    sign1 = request.args.get('sign1')
    sign2 = request.args.get('sign2')

    if sign1 not in zodiac_signs or sign2 not in zodiac_signs:
        return jsonify({'error': 'Invalid zodiac sign.'}), 400
    
    compatibility = zodiac_compatibility[sign1][sign2]
    
    response = {'compatibility': f'{compatibility}%'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()