import lxml.etree as etree
from .backend.xmlCompressor import XMLCompressor
from flask import Flask, render_template, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import os
from io import BytesIO

app = Flask(__name__)
CORS(app)
compressedXMLs = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/process_xml', methods=['POST'])
def process_xml():
    """
    API route to handle XML query processing.
    Expects a JSON request containing 'query' and 'fileName' fields.
    It fetches the pre-uploaded and compressed XML based on filename and processes the query.
    Returns the result or an error if something goes wrong.
    """
    try:
        data = request.get_json()
        query = data['query']
        filename = data['fileName']
        return jsonify(compressedXMLs[filename].get(query))
    except Exception as e:
        return jsonify({'error': True, 'message': str(e)})
    

@app.route('/post_xml', methods=['POST'])
def post_xml():
    """
    API route to handle XML file upload and compression.
    Expects a JSON request containing 'fileContent' (XML data as string) and 'fileName'.
    Parses the XML, compresses it using XMLCompressor, and stores it for later use.
    """
    try:
        data = request.get_json()
        xml_content = data['fileContent']
        filename = data['fileName']
        tree = etree.fromstring(xml_content)
        compressedXML = XMLCompressor(tree)
        compressedXMLs[filename] = compressedXML

        return jsonify({'success': 'XML file uploaded successfully!', 'download_url': f'/download/{filename}'})
    except Exception as e:
        return jsonify({'error': True, 'message': str(e)})
    
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """
    Route to download the compressed XML file.
    """
    try:
        # Ensure the file exists in the upload folder
        upload_data = compressedXMLs[filename].to_string() 
        return send_file(BytesIO(upload_data.encode()), as_attachment=True, download_name=filename.split('.')[0] + '.txt')
    except Exception as e:
        print(e)
        return jsonify({'error': True, 'message': 'File not found!'}), 404

@app.route('/')
def index():
    """
    Route to serve the main index HTML file, which likely contains a form
    to upload XML files and make queries to the above-defined API endpoints.
    """
    return render_template('index.html')  # Render the index HTML

if __name__ == '__main__':
    app.run(debug=True)  # Run the app
