import lxml.etree as etree
from xmlCompressor import XMLCompressor
from flask import Flask, request, jsonify
from flask_cors import CORS

def process_xml():
    # sys.stdout = open('bin/output.txt', 'w') # create if does not exist


    try: 
        data = request.get_json()
        xml_content = data['xml']
        query = data['query']
        tree = etree.fromstring(xml_content)
        compressedXML = XMLCompressor(tree)
    # print(compressedXML.pathCodes)
    # query = 'book/section/title'
    # print(compressedXML.XPathQueryEncoding(query))
    # print(compressedXML.get(query))
        # compressedXML.XPathQueryEncoding(query)
        return jsonify(compressedXML.get(query))
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)  
    @app.route('/process_xml', methods=['POST'])
    def process():
        return process_xml()
    app.run(debug=True)

