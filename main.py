import cv2
import pytesseract
from openai import OpenAI

ai_client = OpenAI(
    api_key="YOUR_OPEN_AI_API_KEY"
)

def preprocess_image(image):
    image = cv2.imread(image)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image

    cv2.imwrite('gray_image.jpg', gray)

    # Apply thresholding
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the thresholded image

    cv2.imwrite('thresholded_image.jpg', threshold)

    return threshold

def extract_text(image):
    return pytesseract.image_to_string(image)

def ai_extract(text_content):
    prompt = """You are a receipt parser AI. I am going to provide you with text extracted from an image of a store receipt.
    I need you to return a JSON object with this structure:
    {“total”, “business”, “items”: [{“title”, “quantity”, “price”}], “transaction_timestamp”}.
    Return the prices as integers that represent the number of pennies (£1 = 100) Only return the JSON object.
    Do not return anything else. Here is the text extracted from the receipt: """ + text_content

    response = ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content[response.choices[0].message.content.find('{'):response.choices[0].message.content.rfind('}')+1]

if __name__ == '__main__':

    image_path = "receipt.jpg"

    preprocessed_image = preprocess_image(image_path)

    text_content = extract_text(preprocessed_image)

    json_data = ai_extract(text_content)

    with open('receipt.json', 'w') as f:
        f.write(json_data)