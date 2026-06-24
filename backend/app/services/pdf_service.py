import fitz

def extract_pdf_info(pdf_path):

    doc = fitz.open(pdf_path)

    pages_data = []
    full_text = ""

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        text = page.get_text()

        pages_data.append({
            "page": page_num + 1,
            "text": text
        })

        full_text += text

    return {
        "pages": len(doc),
        "characters": len(full_text),
        "pages_data": pages_data
    }