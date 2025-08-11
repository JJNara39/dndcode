from PyPDF2 import PdfReader, PdfWriter
import time

def fill_fields_with_names(input_pdf, output_pdf):
    # Read input file
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Loop through all the pages
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

        #Get form fields from that page
        fields = reader.get_fields()



        # If there are fields, fill them with field name
        if fields:
            for field_name, field_info in fields.items():
                #Fill each field with name
                writer.update_page_form_field_values(
                    writer.pages[page_num], {field_name: field_name}
                )
    # Write the output pdf
    with open(output_pdf, 'wb') as output_file:
        #Add a delay
        time.sleep(10) #sleeps for 6s
        writer.write(output_file)

def fill_checkbox(input_pdf, output_pdf, checkbox_name, value="/Yes"):
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Loop through all pages
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

        # Get the form fields of the PDF
        fields = reader.get_fields()

        # If the checkbox exists in the fields, set its value to "Yes" (checked)
        if checkbox_name in fields:
            writer.update_page_form_field_values(
                writer.pages[page_num],
                {checkbox_name: value}
            )

    # Write the modified PDF to a new file
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

def print_checkbox_values(input_pdf):
    reader = PdfReader(input_pdf)
    fields = reader.get_fields()

    for field_name, field_info in fields.items():
        if 'Check Box' in field_name:
            print(f"Field: {field_name}")
            print(f"Field Info: {field_info}")
            print()

input_pdf = 'DnD_5E_CharacterSheet_FormFillable.pdf'
# output_pdf = 'dnd5e_sheet_filled.pdf'
output_pdf1 = 'dnd5e_sheet_filled1.pdf'
checkbox_name1 = "Check Box 327"
#fill_checkbox(input_pdf, output_pdf1, checkbox_name1)
fill_fields_with_names(input_pdf, output_pdf1)
# Example usage
#print_checkbox_values(input_pdf)