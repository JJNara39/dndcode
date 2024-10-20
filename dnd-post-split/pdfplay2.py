from PyPDF2 import PdfReader, PdfWriter

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
output_pdf1 = 'dnd5e_sheet_filled2.pdf'
output_pdf2 = 'dnd5e_sheet_filled3.pdf'
output_pdf3 = 'dnd5e_sheet_filled4.pdf'
output_pdf4 = 'dnd5e_sheet_filled5.pdf'
output_pdf5 = 'dnd5e_sheet_filled6.pdf'
checkbox_name1 = "Check Box 12"
checkbox_name2 = "Check Box 14"
checkbox_name3 = "Check Box 15"
checkbox_name4 = "Check Box 11"
checkbox_name5 = "Check Box 18"
fill_checkbox(input_pdf, output_pdf1, checkbox_name1)
fill_checkbox(input_pdf, output_pdf2, checkbox_name2)
fill_checkbox(input_pdf, output_pdf3, checkbox_name3)
fill_checkbox(input_pdf, output_pdf4, checkbox_name4)
fill_checkbox(input_pdf, output_pdf5, checkbox_name5)
# fill_fields_with_names(input_pdf, output_pdf)
# Example usage
#print_checkbox_values(input_pdf)