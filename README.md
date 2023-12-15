# PDF To Audiobook

A Flask web application for converting PDF files into audiobooks.

## Dependencies
A list of this application's dependencies can be found in requirements.txt

## How to run PDF To Audiobook (locally)
1. Clone this repository.
2. Navigate to the local folder you cloned the repository into and open it in your terminal of choice.
3. Depending on your preference, you could set up a Python virtual environment or install dependencies globally. Click [here](https://docs.python.org/3/library/venv.html) for more information on setting up virtual environments.
4. Install dependencies by running this command in your terminal window:
```
pip install -r requirements.txt
```
5. Run the application using in the terminal window:
```
flask run
```

## Features/Roadmap:

### User authentication
* Set up a simple user login system; Sign up and Log in
* Figure out password hashing/small security features
* Guard against simple SQL injection attacks

### File uploads
* Set up an upload route to handle PDF uploads
* Set limits for PDF file size and validation
* Save PDFs and metadata in SQLite db
* Test

### Text-To-Speech integration
* Look up Python packages/libraries for TTS
* Set up a conversion route to handle PDF to MPEG conversion
* Test

### Streaming (Downloads)
* Look into Flask streaming
* Set up a streaming/download route to handle MPEG downloads
* Consider file persistence vs streaming
