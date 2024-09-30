# Xpress

## Overview

**Xpress** is a web-based XML processor, allowing users to upload, parse, and query XML documents. It features a simple interface for XML parsing and offers basic XPath Query capabilities. The application is containerized using Docker, ensuring easy deployment and scalability.

## Features

- **XML Upload and Compressing**: Upload XML files to Compress them to a more compact form
- **XML Queries**: User can input queries in XPath format to query the uploaded XML document efficiently. The queries can be made in `O(logn)` time complexity where `n` is the number of leaf nodes present in the document. The syntax and semantic validation of the XPath query is handled by the application itself.

## Research Perspective
- The algorithm for the XML compression is inspired from the paper: 


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SameerSharma-57/Xpress.git
   cd Xpress
   ```

2. Build the Docker container:
   ```bash
   docker build -t sde_path_queries .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 8080:8080 sde_path_queries
   ```

4. Access the application by visiting `http://localhost:8080` in your browser.


## Tech Stack

- **Backend**: Python
- **Frontend**: HTML, CSS, JavaScript, JQuery, Bootstrap
- **Deployment**: Docker, GCP

## Contributions

Contributions are welcome! Fork the repository, submit issues, or create pull requests to enhance Xpress.

## License

This project is licensed under the MIT License.