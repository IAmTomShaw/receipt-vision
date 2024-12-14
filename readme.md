# Receipt Parser

This project extracts text from an image of a store receipt and converts it into a structured JSON object using OCR and AI.

## Requirements

- Python 3.x
- OpenCV
- Pytesseract
- OpenAI Python client

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key in [main.py]:
    ```python
    ai_client = OpenAI(
        api_key="YOUR_OPEN_AI_API_KEY"
    )
    ```

## Usage

1. Add an image of a receipt named `receipt.jpg` to the project directory.

2. Run the script:
    ```sh
    python main.py
    ```

3. The extracted JSON data will be saved in `receipt.json`.

## Project Structure

- main.py: The main script that processes the image, extracts text, and converts it to JSON.
- requirements.txt: The list of required Python packages.
- readme.md: Project documentation.

## License

This project is licensed under the MIT License.

## Credit

This project was created by [Tom Shaw](https://tomshaw.dev)
