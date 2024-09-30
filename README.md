# Xpress

## Overview

**Xpress** is a web-based XML processor and compressor, allowing users to upload, parse, compress and query XML documents. It features a simple interface for XML compressing and offers basic XPath Query functionalities. The application is containerized using Docker, ensuring easy deployment and scalability.

## Features

- **XML Upload and Compressing**: Upload XML files to Compress them to a more compact form. 
- **XML Queries**: User can input queries in XPath format to query the uploaded XML document efficiently. The queries can be made in `O(logn)` time complexity where `n` is the number of leaf nodes present in the document. The syntax and semantic validation of the XPath query is handled by the application itself.

## Research Perspective

- The algorithm for the XML compression is inspired from the paper: https://dl.acm.org/doi/pdf/10.1145/872757.872775. The algorithm is optimized to `O(logn)` to decrease the time complexity of querying the xml document repeatedly by a trade off in slight increase in time complexity of compression. 

<!-- A two column table -->
| **In Paper** | **In Xpress** |
| --- | --- |
| Compression Complexity: `O(n)` | Compression complexity: `O(nlogn)` |
| Query Complexity: `O(n)` | Query Complexity: `O(logn)` |

- The optimized query complexity is acheived by sorting the leaf nodes of the xml tree in order of their interval and therefore, each time a query is made, the application can directly jump to the required leaf nodes in `O(logn)` time complexity using binary search. While during compression, the cost of sorting the leaf nodes is incresed to `O(nlogn)`.


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

## License

This project is licensed under the MIT License.
