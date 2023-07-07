from fpdf import FPDF

# Define a custom PDF class inheriting from FPDF
class Report(FPDF):
    def header(self):
        # Set up the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Account Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Set up the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        # Set up the chapter title
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, data):
        # Set up the chapter body
        self.set_font('Arial', '', 10)
        for item in data:
            for key, value in item.items():
                if key == 'Transactions':
                    self.transaction_table(value)
                else:
                    self.cell(0, 5, f'{key}: {value}', 0, 1, 'L')
            self.ln(5)

    def transaction_table(self, transactions):
        # Set up the transaction table
        self.set_font('Arial', 'B', 10)
        self.cell(50, 7, 'Transaction Type', 1, 0, 'C')
        self.cell(40, 7, 'Date', 1, 0, 'C')
        self.cell(40, 7, 'Amount', 1, 1, 'C')
        self.set_font('Arial', '', 10)
        for transaction in transactions:
            self.cell(50, 7, transaction[0], 1, 0, 'C')
            self.cell(40, 7, transaction[1], 1, 0, 'C')
            self.cell(40, 7, str(transaction[2]), 1, 1, 'C')
        self.ln(5)
