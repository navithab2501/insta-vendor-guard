import easyocr

# OCR Reader (once create pannuvom)
reader = easyocr.Reader(['en'])


def extract_text(image_path):
    """
    Image-la irundhu text extract pannum function
    """

    result = reader.readtext(image_path)

    extracted_text = ""

    for item in result:
        extracted_text += item[1] + "\n"

    return extracted_text