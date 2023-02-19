from fpdf import FPDF

pdf = FPDF()

filename = 'test-thai-sentents-shaping.pdf'
font_type = 'otf'
font_path = f'{font_type}-tlwg-0.7.3'  # https://github.com/tlwg/fonts-tlwg
font_size = 14

font_names = [
    'Garuda',
    'Kinnari',
    'Laksaman',
    'Loma',
    'Norasi',
    'Purisa',
    'Sawasdee',
    'TlwgMono',
    'TlwgTypewriter',
    'TlwgTypist',
    'TlwgTypo',
    'Umpush',
    'Waree',
]

thai_texts = [
    '๏ เป็นมนุษย์สุดประเสริฐเลิศคุณค่า    กว่าบรรดาฝูงสัตว์เดรัจฉาน',
    'จงฝ่าฟันพัฒนาวิชาการ           อย่าล้างผลาญฤๅเข่นฆ่าบีฑาใคร',
    'ไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่า     หัดอภัยเหมือนกีฬาอัชฌาสัย',
    'ปฏิบัติประพฤติกฎกำหนดใจ        พูดจาให้จ๊ะๆ จ๋าๆ น่าฟังเอย ฯ',
]

for font_name in font_names:

    pdf.add_page()
    pdf.add_font(font_name, fname=f'{font_path}/{font_name}.{font_type}')

    pdf.set_font('Helvetica', '', font_size)
    pdf.text(x=10, y=10, txt=font_name)
    pdf.text(x=10, y=24, txt='Only FPDF')
    pdf.text(x=10, y=(34 + (len(thai_texts) * font_size)), txt='With harfbuzz')

    pdf.set_font(font_name, '', font_size)

    for i, thai_text in enumerate(thai_texts):

        pdf.text(x=15, y=(34 + (font_size * i)), txt=thai_text)

    for i, thai_text in enumerate(thai_texts):
        pdf.harfbuzz_text(
            x=15, y=((44 + (len(thai_texts) * font_size)) + (font_size * i)), txt=thai_text)

pdf.output(filename)
