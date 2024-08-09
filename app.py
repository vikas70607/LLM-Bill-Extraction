import PyPDF2
import openai
import os

# Initialize OpenAI API
openai.api_key = 'your-key'  # Replace with your OpenAI API key

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def extract_information(text):
    prompt = f"""
    Extract and format the following information from the text:
    1. Customer details (Name, Address, Phone Number, Email)
    2. List of products (Product Name, Quantity, Price per unit, Total price)
    3. Total amount
    
    Text: {text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0
    )
    
    return response.choices[0].message.content

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    extracted_info = extract_information(text)
    print(extracted_info)

if __name__ == "__main__":
    main("sample Invoice.pdf")
