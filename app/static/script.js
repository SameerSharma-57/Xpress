// script.js
var fileName = '';	
var queryResult = '';
function uploadFile() {
    let fileInput = document.getElementById('xmlFile');
    let file = fileInput.files[0];
    let reader = new FileReader();

    document.getElementById('progressBar').value = 0;
    document.getElementById('progressBar').style.width = '0%';
    document.getElementById('loaded_n_total').textContent = '0%';
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

        xhr.addEventListener('load', function() {
            if (xhr.status === 200) {
                let response = JSON.parse(xhr.responseText);
                if (response.success) {
                    // Set the download URL for the compressed file
                    let downloadUrl = response.download_url;
                    let downloadBtn = document.getElementById('downloadBtn');
                    downloadBtn.href = downloadUrl;
                    document.querySelector('#downloadBtn button').style.display = 'inline-block';  // Show the download button
                } else {
                    document.getElementById('status').textContent = 'Upload Failed!';
                }
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

    const startTime = Date.now(); // Capture start time

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
        const endTime = Date.now(); // Capture end time
        const responseTime = endTime - startTime; // Calculate response time in milliseconds

        // Handle the result returned from the backend
        console.log(result);	
        queryResult = result["result"];
        queryTime = result["time"];
        if(result['error']) {
            document.getElementById('xmlDisplay').textContent = 'Please correct your query or XML file';
            return;
        }
        
        document.getElementById('xmlDisplay').textContent = `Result: ${JSON.stringify(result)}\nResponse time: ${responseTime} ms\nQuery time: ${queryTime} ms`;
        document.getElementById('downloadQueryBtn').style.display = 'inline-block';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('xmlDisplay').textContent = 'Error processing XML.';
    });
}

function downloadQueryResult() {
    // Create a blob from the query result string
    let blob = new Blob([queryResult], { type: 'text/plain' });

    // Create a temporary anchor element to trigger the download
    let a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'query_result.txt';  // You can change the filename if needed
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
