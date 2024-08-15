from langchain_community.document_loaders import PyMuPDFLoader

invoice_dir = "Invoice Format.pdf"

def data_extraction(dir):
    loader = PyMuPDFLoader(dir)
    pages = loader.load()
    text = "\n\n".join(page.page_content for page in pages)

    return text


# print(data_extraction(dir=invoice_dir))