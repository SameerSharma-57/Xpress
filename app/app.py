from fileinput import filename
import re
from isort import file
import lxml.etree as etree
from sympy import comp
from backend.xmlCompressor import XMLCompressor
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
compressedXMLs = {}
@app.route('/process_xml', methods=['POST'])
def process_xml():
    try:
        data = request.get_json()
        query = data['query']
        filename = data['fileName']
        return jsonify(compressedXMLs[filename].get(query))
    except Exception as e:
        return jsonify({'error': True, 'message': str(e)})
@app.route('/post_xml', methods=['POST'])
def post_xml():
    try:
        data = request.get_json()
        xml_content = data['fileContent']
        filename = data['fileName']
        tree = etree.fromstring(xml_content)
        compressedXML = XMLCompressor(tree)
        compressedXMLs[filename] = compressedXML
        return jsonify({'success': 'XML file uploaded successfully!'})
    except Exception as e:
        return jsonify({'error': True, 'message': str(e)})

@app.route('/')
def index():
    return render_template('index.html')  # Render the index HTML

if __name__ == '__main__':
    app.run(debug=True)  # Run the app
