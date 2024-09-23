// script.js

// Function to read and display XML content from file or textarea
function displayXML() {
    let fileInput = document.getElementById('xmlFile');
    let textArea = document.getElementById('xmlText');
    let xmlQuery = document.getElementById('xmlQuery');
    let xmlDisplay = document.getElementById('xmlDisplay');
    
    // Clear the display area
    xmlDisplay.innerHTML = '';

    if (fileInput.files.length > 0 && xmlQuery.value.trim() !== "") {
        // If an XML file is uploaded
        let file = fileInput.files[0];
        let reader = new FileReader();

        reader.onload = function(e) {
            let xmlContent = e.target.result;
            xmlDisplay.textContent = formatXML(xmlContent, xmlQuery.value);
        };

        reader.readAsText(file);
    } else if (textArea.value.trim() !== "" && xmlQuery.value.trim() !== "") {
        // If XML is pasted into the textarea
        let xmlContent = textArea.value;
        xmlDisplay.textContent = formatXML(xmlContent, xmlQuery.value);
    } else {
        xmlDisplay.textContent = "No XML content provided.";
    }

}

// Function to format XML (pretty print)
function formatXML(xml,xmlQuery) {
    // get result by calling Backend/main.py
    const url = 'http://127.0.0.1:5000/process_xml';

    // Prepare the data to be sent
    const data = {
        xml: xml,
        query: xmlQuery
    };

    // Make an asynchronous POST request to the backend
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        // Handle the result returned from the backend
        console.log('Result:', result);
        document.getElementById('xmlDisplay').textContent = `${result}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('xmlDisplay').textContent = 'Error processing XML.';
    });
}

