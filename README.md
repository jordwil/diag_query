# Diag Query

A simple web service that exposes two API endpoints.
1. Retrieves a list of strings in a text file given a prefix.
2. Stores the selection of prefix a target string containing the prefix.

## Getting Started
### Pip installation:
In your terminal, run the following:
```
git clone https://github.com/jordwil/diag_query
cd diag_query
conda env create -f web_serv.yaml
export FLASK_APP='diag_query.py'
flask run
```

You should see something like this:

```
* Serving Flask app "diag_query"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

Paste the http link into your favorite browser.





### Prerequisites

- Python 3 with conda installed.
- The rest of the requirements are found in requirements.txt
