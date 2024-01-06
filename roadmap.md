Did  a little housekeeping and seperated the README from my personal notes for better readability. This doc contains notes on the project's scope and future featurs, requirements, and overall implementation details.

## Features/Roadmap:

### File uploads and handling
#### Problem
Currently, it takes too long to process PDF files, especially complex ones. There needs to be a way to reach constant conversion time for any given file.
* Explore ways to make pdf conversion faster (ideally constant time)
    * Greedy vs Non-greedy algorithms (binary search?)
    * How to process files in batches
    * Asynchronous programming(?)
    * Streaming?
    * ~~Consider other libraries? (https://medium.com/analytics-vidhya/abffd75b1af7)~~
* Explore ways to make audio conversion faster (ideally constant time)
    * Wrapper for espeak-ng? (Would need to test out the library first; Also, might be a hassle to manage a project for a project; Long-term might be worth it)
    * Async, again (Lazy to implement but might be worth it)
* ~~Set up an upload route to handle PDF uploads~~ (partial implementation)
* ~~Set limits for PDF file size and validation~~
* Save PDFs and metadata in SQLite db
* Test

### Text-To-Speech integration
* Look up Python packages/libraries for Natural-sounding TTS (OpenAI Whisper?) (partial implementation)
* ~~Set up a conversion route to handle PDF to MPEG conversion~~
* Test

### User authentication
* Set up a simple user login system; Sign up and Log in
* Figure out password hashing/small security features
* Guard against simple SQL injection attacks

### Streaming (Downloads)
* Look into Flask streaming
* Set up a streaming/download route to handle MPEG downloads
* Consider file persistence vs streaming
