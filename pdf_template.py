# We are going to create a pdf notebook with multiple categories or topics and several pages per topic.

from fpdf import FPDF
import pandas as pd

C = 0  # color constant repeated in code down.

# Create a pdf instance using the FPDF module. And we format it: Portrait orientation, units in mm and A4 format.
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

topics_df = pd.read_csv(
    r"topics.csv", sep=","
)  # here we open the topics.csv file with the pandas read module and save it in a data frame.

# with this for loop we repeatedly create the main pdf pages (where the main topic is placed) with their cells and headers.
for (
    index,
    row,
) in (
    topics_df.iterrows()
):  # iterrow is used to iterate over all the rows in the .csv file.
    pdf.add_page()  # this is the call to the FPDF instance to create a page in pdf format.

    # Create the header, page title:
    pdf.set_font(
        family="Times", style="B", size=22
    )  # adjust the format of the text in the cells (boxes),
    pdf.set_text_color(254, 0, 0)  # and the color.
    pdf.cell(
        w=0, h=12, txt=f'{row["Order"]}: {row["Topic"]}', align="C", ln=1
    )  # create the cell where the header is located.
    # (w=cell width; h=height; text, align=where the text is (left, center, right); ln=line breaks until the next cell).

    # Create a line that underlines the title of each initial page of the topics.
    pdf.line(
        45, 21, 166, 21
    )  # from the horizontal position (x) 45 mm to 200 mm (horizontal length of the line). And the height (vertical position y) is 21 mm.
    pdf.set_draw_color(C, C, C)  # select the rgb color of the guide.

    # for loop to create the lines on the pages (initial of each topic) that serve as a guide to write straight.
    for y in range(
        33, 275, 12
    ):  # from the distance of 33 mm, to 275 mm, draw a "line" every 12 mm.
        pdf.line(
            10, y, 200, y
        )  # from the horizontal position (x) 10 mm to 200 mm (horizontal length of the line).
        pdf.set_draw_color(C, C, C)  # select the rgb color of the guide.

    # Create the footer on the main pages of the topics.
    pdf.ln(265)  # where the two footers are created (topic and pager)
    pdf.set_font(family="Times", style="I", size=8)  # text format.
    pdf.set_text_color(198, 198, 198)  # color
    pdf.cell(
        w=0, h=10, txt=row["Topic"], align="L"
    )  # adjust the cell with the parameters we want.

    # add page number with its style and color.
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=str(pdf.page_no()), align="R")

    # create a for loop with the blank pages that exist for each topic.
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Create the footer for the empty pages.
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(198, 198, 198)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="L")

        # add page number with its style and color.
        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=str(pdf.page_no()), align="R")

        # for loop to create the lines on the pages that serve as a guide to write straight.
        for y in range(20, 275, 12):
            pdf.line(10, y, 200, y)
            pdf.set_draw_color(C, C, C)

pdf.output("template.pdf")