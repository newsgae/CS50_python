from fpdf import FPDF


'''
Create a PDF with an image of an "xxx took CS50 t-shirt",
    shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that
    prompts the user for their name and outputs, using fpdf2,
     a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard,
     with these specifications:

        The orientation of the PDF should be Portrait.
        The format of the PDF should be A4, which is 210mm wide by 297mm tall.
        The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
        The shirt’s image should be centered horizontally.
        The user’s name should be on top of the shirt, in white text.
        no need to wrap long names across multiple lines


first must done:
     pip install fpdf2
     download picture: wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
     Before writing any code, do read through fpdf2’s tutorial to learn how to use it.
        https://py-pdf.github.io/fpdf2/Tutorial.html
    skim fpdf2’s API (application programming interface) to see all of its functions and parameters
        https://py-pdf.github.io/fpdf2/fpdf/

'''


class PDF(FPDF):
    def header(self):


        # set margins
        self.set_margins(left=1.0, top=2.0, right=1.0)

        # set title font
        self.set_font('helvetica', 'B', 32)
        # set title color
        self.set_text_color(0, 0, 0)
        # print title
        self.cell(w=200, h=15, text='CS50 Shirtificate', align='C')
        # set shirt image, name, define (x, y) at upper left corner, define width and height
        self.image('shirtificate.png', x=35, y=35, w=120, h=120 )

    def shirt(self, name):
        self.name = name
        # set shirt font size
        self.set_font('helvetica', style='B', size=16)
        # set shirt font color to white
        self.set_text_color(225, 255, 255)
        # print shirt font
        self.cell(w=-210, h=150, text=f'{self.name} took CS50', border=0, align='C', fill=False)


def main():
    # get name
    name = str(input('Name: '))
    # name = 'John Hopikins'

    # create pdf class
    pdf = PDF()
    # setup page
    pdf.add_page(orientation="portrait", format="A4")
    # provide name
    pdf.shirt(name)
    # create pdf
    pdf.output('shirtificate.pdf')


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/shirtificate
# submit50 cs50/problems/2022/python/shirtificate