Did  a little housekeeping and seperating the README from my personal notes on the project's scope and future featurs, requirements, and overall implementation details.

## Features/Roadmap:

### File uploads and handling
* Explore ways to make pdf conversion faster (ideally constant time)
    * Greedy vs Non-greedy algorithms
    * How to process files in batches
    * Asynchronous programming(?)
    * Streaming?
* Explore ways to make audio conversion faster (ideally constant time)
* ~~Set up an upload route to handle PDF uploads~~ (partial implementation)
* ~~Set limits for PDF file size and validation~~
* Save PDFs and metadata in SQLite db
* Test

### Text-To-Speech integration
* ~~Look up Python packages/libraries for Natural-sounding TTS (OpenAI Whisper?)~~ (partial implementation)
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
