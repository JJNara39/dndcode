import PyPDF2
def fill_pdf(input_pdf_path, output_pdf_path, data): #This function to fill it, well where do we get the file, where will we put the file, what is going in the file
    with open(input_pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)

            #Getting form fields
            fields = reader.get_fields()

            if fields:
                for key, value in data.items():
                    #Fill each field with name
                    writer.update_page_form_field_values(
                        writer.pages[page_num], {key: value}
                    )
                
            #Write the filled form to output PDF
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)

# Example data to fill
data = {
    'CharacterName': 'Arthas Menethil',
    'Race ': 'Human',
    'ClassLevel': 'Paladin 1',
    'STR': '18'
}

# File paths (use the correct file paths for your case)
input_pdf_path = 'DnD_5E_CharacterSheet_FormFillable.pdf'
output_pdf_path = 'Char1_dnd5e_sheet.pdf'

# Run the function to fill the PDF
fill_pdf(input_pdf_path, output_pdf_path, data)

# This was meant to list the fields'
'''
pdf_path = 'DnD_5E_CharacterSheet_FormFillable.pdf'
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get total number of pages
    num_pages = len(pdf_reader.pages)
    print(f"Total Pages: {num_pages}")
    
    # Extract form fields from the entire PDF
    fields = pdf_reader.get_fields()

    if fields:
        # Loop through each page and list the fields
        for page_num in range(num_pages):
            print(f"\n--- Fields on Page {page_num + 1} ---")
            for field_name, field_info in fields.items():
                # PyPDF2 does not directly associate fields with pages, so we list them all
                # This section just lists all fields in the PDF, since PyPDF2 doesn't know the page
                print(f"Field Name: {field_name}, Value: {field_info.get('/V')}")
    else:
        print("No form fields found.")        
'''