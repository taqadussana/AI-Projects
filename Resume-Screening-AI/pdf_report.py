from fpdf import FPDF


def _clean(text):
    """
    Clean text for PDF and prevent long unbreakable words.
    """
    text = str(text)

    text = text.replace(",", ", ")

    return text.encode("latin-1", "ignore").decode("latin-1")


def build_pdf_report(df):

    pdf = FPDF()

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)

    pdf.cell(
        0,
        12,
        _clean("Resume Screening AI Pro - Results Report"),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font("Helvetica", "", 11)

    pdf.set_text_color(90, 90, 90)

    pdf.cell(
        0,
        8,
        _clean(f"Candidates Screened: {len(df)}"),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(5)

    for _, row in df.iterrows():

        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(0, 0, 0)

        pdf.cell(
            0,
            8,
            _clean(row["Candidate"]),
            new_x="LMARGIN",
            new_y="NEXT"
        )

        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(60, 60, 60)

        pdf.cell(
            0,
            7,
            _clean(
                f"Match Score: {row['Match Score']}%    |    Skill Score: {row['Skill Score']}%"
            ),
            new_x="LMARGIN",
            new_y="NEXT"
        )

        pdf.set_x(pdf.l_margin)

        pdf.multi_cell(
            pdf.epw,
            6,
            _clean(
                f"Matched Skills: {row.get('Matched Skills', '') or 'None'}"
            )
        )

        pdf.set_x(pdf.l_margin)

        pdf.multi_cell(
            pdf.epw,
            6,
            _clean(
                f"Missing Skills: {row.get('Missing Skills', '') or 'None'}"
            )
        )

        pdf.ln(4)

    return bytes(pdf.output())