from PyPDF2 import PdfReader
import re

# Open the PDF file
with open('pdfInvoice2.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    #Invoice Date, Invoice #, Due Date, Qty, Brief Description, Balance Due

    """
    Invoice #
    11111111
    """

    # Define regex patterns for "Invoice #" and the invoice number
    invoiceNum_label_pattern = r'Invoice #'
    invoiceNum_number_pattern = r'\d+'
    # Define regex patterns for "Invoice Date" and the invoice date
    invoiceDate_label_pattern = r'Invoice Date'
    invoiceDate_date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
    # Define regex patterns for "Due Date" and the date
    invoiceDue_label_pattern = r'Due Date'
    invoiceDue_date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
    # Define regex patterns for "Qty" and the quanity amount
    invoiceQty_label_pattern = r'Qty'
    invoiceQty_amount_pattern = r'\d+'#r'(?:Qty\s+)?(\d+)(?!Item)'#r'\d+'
    # Define regex patterns for "Balance Due" and the total balance
    invoiceBal_label_pattern = r'Balance Due'
    invoiceBal_balance_pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'
    # Define regex patterns for "Description" and a breif desciption
    invoiceDesc_label_pattern = r'Description'
    invoiceDesc_description_pattern = r'(?<=Description)[A-Za-z0-9\s]+'

    # Loop through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text2 = page.extract_text()

        # Use regular expressions to search for patterns
        # Search for the label pattern
        numLabel_match = re.search(invoiceNum_label_pattern, text2)
        dateLabel_match = re.search(invoiceDate_label_pattern, text2)
        dueLabel_match = re.search(invoiceDue_label_pattern, text2)
        qtyLabel_match = re.search(invoiceQty_label_pattern, text2)
        balLabel_match = re.search(invoiceBal_label_pattern, text2)
        descLabel_match = re.search(invoiceDesc_label_pattern, text2)
    #"""
    #Extract Invoice Date information if matches are found
    if dateLabel_match:
        # Get the starting position of the label
        dateLabel_start = dateLabel_match.start()

        # Extract text starting from the position of the label
        dateText_after_label = text2[dateLabel_start:]
        # Search for the invoice date in the text after the label
        date_match = re.search(invoiceDate_date_pattern, dateText_after_label)

        if date_match:
            invoice_date = date_match.group()
            print("Invoice Date:", invoice_date)
        else:
            print("Invoice Date not found.")
    else:
        print("Invoice Date Label not found.")
    # Extract Inovice # information if matches are found
    if numLabel_match:
        # Get the starting position of the label
        numLabel_start = numLabel_match.start()

        # Extract text starting from the position of the label
        text_after_label = text2[numLabel_start:]

        # Search for the invoice number in the text after the label
        number_match = re.search(invoiceNum_number_pattern, text_after_label)

        if number_match:
            invoice_number = number_match.group()
            print("Invoice Number:", invoice_number)
        else:
            print("Invoice Number not found.")
    else:
        print("Invoice Number Label not found.")
    #"""
    #Extract Invoice Due Date information if matches are found
    if dueLabel_match:
        # Get the starting position of the label
        dueLabel_start = dueLabel_match.start()

        # Extract text starting from the position of the label
        dueText_after_label = text2[dueLabel_start:]
        # Search for the invoice date in the text after the label
        due_match = re.search(invoiceDue_date_pattern, dueText_after_label)

        if due_match:
            invoice_due = due_match.group()
            print("Invoice Due Date:", invoice_due)
        else:
            print("Invoice Due Date not found.")
    else:
        print("Invoice Due Date Label not found.")
    #Extract Invoice Qty information if matches are found
    if qtyLabel_match:
        quantities = []
        # Get the starting position of the label
        qtyLabel_start = qtyLabel_match.start()

        # Extract text starting from the position of the label
        qtyText_after_label = text2[qtyLabel_start:]
        """
        for line in qtyText_after_label:
            qty_match = re.search(invoiceQty_amount_pattern, line)
            if qty_match:
                quantities.append(qty_match.group(1))
            else:
                if 'Item' in line:
                    break
        #"""
        #qty_match = re.findall(invoiceQty_amount_pattern, qtyText_after_label)
        #print(qtyText_after_label)
        # Search for the invoice date in the text after the label
        qty_match = re.search(invoiceQty_amount_pattern, qtyText_after_label)

        if qty_match:
            #invoice_qty = []
            invoice_qty = qty_match.group()
            print("Invoice Quantity:", invoice_qty)
        else:
            print("Invoice Quantity not found.")
    else:
        print("Invoice Quantity Label not found.")
    #Extract Invoice Total Balance information if matches are found
    if balLabel_match:
        # Get the starting position of the label
        balLabel_start = balLabel_match.start()

        # Extract text starting from the position of the label
        balText_after_label = text2[balLabel_start:]
        #print(dateText_after_label)
        # Search for the invoice date in the text after the label
        bal_match = re.search(invoiceBal_balance_pattern, balText_after_label)

        if bal_match:
            invoice_bal = bal_match.group()
            print("Invoice Balance Due:", invoice_bal)
        else:
            print("Invoice Balance Due not found.")
    else:
        print("Invoice Balance Due Label not found.")
    
    """
    #Description text extraction is broken due to needing to change the
    #original invoice pdf file, using word, causing format to break.
    #Extract Invoice Product Description information if matches are found
    if descLabel_match:
        # Get the starting position of the label
        descLabel_start = descLabel_match.start()
        #print("start")
        #print(descLabel_start)

        # Extract text starting from the position of the label
        descText_after_label = text2[descLabel_start:]
        #print(descText_after_label)
        # Search for the invoice date in the text after the label
        desc_match = re.search(invoiceDesc_description_pattern, descText_after_label)

        if desc_match:
            invoice_desc = desc_match.group().strip()
            print("Invoice Description:", invoice_desc)
        else:
            print("Invoice Description not found.")
    else:
        print("Invoice Description Label not found.")
    """

    
    
