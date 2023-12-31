from http import client
from urllib import request
from google.api_core.client_options import ClientOptions
from google.cloud import documentai

project_id = "gcp-dsi-dev"
location = "us"
file_path = "D:\PICX\Cropped Images\img (2).jpg"
processor_display_name = "doc_ocr_processor"

def quickstart(
    project_id: str,
    location: str,
    file_path: str,
    processor_display_name: str = "doc_ocr_processor",
       
):
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    parent = client.common_location_path(project_id, location)
    
    processor = client.create_processor(
        parent=parent,
        processor=documentai.Processor(
        type_ = "OCR_PROCESSOR",
        display_name = processor_display_name,
        ),
    )
    
    print(f"Processor Name: {processor.name}")
    
    with open(file_path, "rb") as image:
        image_content = image.read()
        
    raw_document = documentai.RawDocument(
        content = image_content,
        mime_type = "image/jpeg",
        )
    
    request = documentai.ProcessRequest(name = processor.name, raw_document = raw_document)

    result = client.process_document(request = request)
    
    document = result.document
    
    print("The document contains the following text : ")
    print(document.text)