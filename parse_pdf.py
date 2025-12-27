from llama_parse import LlamaParse
import os
from dotenv import load_dotenv


def get_text_from_pdf(filepath):

    # Load env variables
    load_dotenv("info.env")

    LLAMAPARSE_API_KEY = os.getenv("MY_API_KEY")
    parser = LlamaParse(
        api_key=LLAMAPARSE_API_KEY,
        result_type="markdown",  # Markdown is best for vector DBs
        gpt4o_mode=True,
        user_prompt="The document contains financial charts and potentially garbled OCR text. Please correct the text to standard English and describe all trading charts and ROI tables in detail."
    )

    document = parser.load_data(filepath)
    with open("/Users/samuel/Documents/ComputerScience/LLMs/IntroRAG/output.md", "w") as f:
        for doc in document:
            print(f"Text:\n {doc.text}")
            f.write(doc.text)

get_text_from_pdf("Step_1_Workbook _4_TradeWay_test.pdf")






