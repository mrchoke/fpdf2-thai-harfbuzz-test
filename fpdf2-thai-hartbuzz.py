from fpdf import FPDF

pdf = FPDF()

filename = 'test-thai-shaping.pdf'
font_type = 'otf'  # 'ttf'
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
    'ที่ ท่า ทิ้ง ท้า กิ๊ง ก๊ง ตี๋ ต๋า บ่น ป่น บ้น ป้น บ๊น ป๊น บ๋น ป๋น',
    'บิน ปิน บีน ปีน บิ่น ปิ่น บัน ปั่น บั่น ก็ ป็',
    'ปู่ ญ ญุ ญู ญฺ ฐ ฐุ ฐู ฐฺ กุ ฎุ ฎู ฎฺ ฏุ ฏู ฏฺ',
    'บำ บ่ำ ปำ ป่ำ ปํ ปิํ บํ บิํ',
    'ปะเฺติ็ลฺ โฺญฺ็จฺ ปั็วฮฺ ทฺ็อง เปฺิ็ว มูํย แต็่ง เจฺํอ เปรฺิ่ห์ โจ๊่',
    'เปฺี่ย โฺทร ม็่อง เติ็ง อาื ยาึ ปิํปี็ป็่ป๊่ปฺ่ จือรฺุ การฺู',
]
"""  'ป ปี ปี่ ปี้ ปี๊ ปี๋ ปา ป่า ป้า ป๊า ป๋า ปำ ป่ำ ปุ ปู ปฺ ปํ ปิํ',
    'บ บี บี่ บี้่ บี๊ บี๋ บา บ่า บ้า บ๊า บ๋า บำ บ่ำ บุ บู บฺ บํ บิํ',
    'ฬ ฬี ฬี่ ฬี้ ฬี๊ ฬี๋ ฬา ฬ่า ฬ้า ฬ๊า ฬ๋า ฬำ ฬ่ำ ฬุ ฬู ฬฺ ฬํ ฬิํ',
    'ญ ญี ญี่ ญี้ ญี๊ ญี๋ ญา ญ่า ญ้า ญ๊า ญ๋า ญำ ญ่ำ ญุ ญู ญฺ ญํ ญิํ',
    'ฐ ฐี ฐี่ ฐี้ ฐี๊ ฐี๋ ฐา ฐ่า ฐ้า ฐ๊า ฐ๋า ฐำ ฐ่ำ ฐุ ฐู ฐฺ ฐํ ฐิํ',
    'ฎ ฎี ฎี่ ฎี้ ฎี๊ ฎี๋ ฎา ฎ่า ฎ้า ฎ๊า ฎ๋า ฎำ ฎ่ำ ฎุ ฎู ฎฺ ฎํ ฎิํ',
    'ฏ ฏี ฏี่ ฏี้ ฏี๊ ฏี๋ ฏา ฏ่า ฏ้า ฏ๊า ฏ๋า ฏำ ฏ่ำ ฏุ ฏู ฏฺ ฏํ ฏิํ', """

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
