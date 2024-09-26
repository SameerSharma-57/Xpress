import lxml.etree as etree
from .backend.xmlCompressor import XMLCompressor
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process_xml', methods=['POST'])
def process_xml():
    try:
        data = request.get_json()
        xml_content = data['xml']
        query = data['query']
        tree = etree.fromstring(xml_content)
        compressedXML = XMLCompressor(tree)
        return jsonify(compressedXML.get(query))
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    return render_template('index.html')  # Render the index HTML

if __name__ == '__main__':
    app.run(debug=True)  # Run the app
