// script.js
var fileName = '';	
function uploadFile() {
    let fileInput = document.getElementById('xmlFile');
    let file = fileInput.files[0];
    let reader = new FileReader();
    console.log(file.name)
    reader.onload = function(e) {
        let fileContent = e.target.result; 
        fileName = file.name;

        let xhr = new XMLHttpRequest();

        // Update progress bar
        xhr.upload.addEventListener('progress', function(e) {
            let percent = (e.loaded / e.total) * 100;
            document.getElementById('progressBar').value = Math.round(percent);
            document.getElementById('progressBar').style.width = Math.round(percent) + '%';
            document.getElementById('loaded_n_total').textContent = `${Math.round(percent)}%`;
        });

        // Handle the upload completion
        xhr.addEventListener('load', function() {
            if (xhr.status === 200) {
                document.getElementById('status').textContent = 'Upload Complete!';
            } else {
                document.getElementById('status').textContent = 'Upload Failed!';
            }
        });

        // Handle any errors
        xhr.addEventListener('error', function() {
            document.getElementById('status').textContent = 'Upload Failed!';
        });

        // Open and send the file content as a string
        xhr.open('POST', '/post_xml');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({ fileContent: fileContent, fileName: fileName }));
    };

    reader.onerror = function() {
        document.getElementById('status').textContent = 'Error reading file!';
    };

    // Read the file as a text string
    reader.readAsText(file);
}





// Function to format XML (pretty print)
function getResult() {
    // get result by calling Backend/main.py
    const url = '/process_xml';
    let xmlQuery = document.getElementById('xmlQuery').value;
    // Prepare the data to be sent
    const data = {
        query: xmlQuery,
        fileName: fileName
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
        console.log(result);	
        if(result['error']) {
            document.getElementById('xmlDisplay').textContent ='Please correct your query or xml file';
            return;
        }
        document.getElementById('xmlDisplay').textContent = `${result}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('xmlDisplay').textContent = 'Error processing XML.';
    });
}

