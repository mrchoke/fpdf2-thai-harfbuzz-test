import os

from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration
font_type = 'otf'
font_path = f'{os.getcwd()}/{font_type}-tlwg-0.7.3'
font_size = 14

print(font_path)

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

font_config = FontConfiguration()

html = ''
css = ''' 
    .row:after {
        content: "";
        display: table;
        clear: both;
    }
    .column { float: left; width: 50%;}
    div.break { page-break-before:always; }
'''
for font_name in font_names:
    html += '<div class="break">'
    html += f'<h1 class="{font_name}">{font_name}</h1>'
    html += f'''
    <div class="row {font_name}">
        <div class="column">๏ เป็นมนุษย์สุดประเสริฐเลิศคุณค่า</div>
        <div class="column">กว่าบรรดาฝูงสัตว์เดรัจฉาน </div>
    </div>
    <div class="row {font_name}">
        <div class="column">จงฝ่าฟันพัฒนาวิชาการ</div>
        <div class="column">อย่าล้างผลาญฤๅเข่นฆ่าบีฑาใคร</div>
    </div>

    <div class="row {font_name}">
        <div class="column">ไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่า</div>
        <div class="column">หัดอภัยเหมือนกีฬาอัชฌาสัย</div>
    </div>

    <div class="row {font_name}">
        <div class="column">ปฏิบัติประพฤติกฎกำหนดใจ</div>
        <div class="column">พูดจาให้จ๊ะ ๆ จ๋า ๆ น่าฟังเอย ฯ</div>
    </div>

    <pre class="{font_name}">
    ที่ ท่า ทิ้ง ท้า กิ๊ง ก๊ง ตี๋ ต๋า บ่น ป่น บ้น ป้น บ๊น ป๊น บ๋น ป๋น
    บิน ปิน บีน ปีน บิ่น ปิ่น บัน ปั่น บั่น ก็ ป็
    ปู่ ญ ญุ ญู ญฺ ฐ ฐุ ฐู ฐฺ กุ ฎุ ฎู ฎฺ ฏุ ฏู ฏฺ
    บำ บ่ำ ปำ ป่ำ ปํ ปิํ บํ บิํ
    ปะเฺติ็ลฺ โฺญฺ็จฺ ปั็วฮฺ ทฺ็อง เปฺิ็ว มูํย แต็่ง เจฺํอ เปรฺิ่ห์ โจ๊่
    เปฺี่ย โฺทร ม็่อง เติ็ง อาื ยาึ ปิํปี็ป็่ป๊่ปฺ่ จือรฺุ การฺู
    </pre>
    </div>'''
    css += f'''
        @font-face {{
            font-family: {font_name};
            font-weight: 400;
            src: url("file://{font_path}/{font_name}.{font_type}");
        }}
        @font-face {{
            font-family: {font_name};
            font-weight: 700;
            src: url("file://{font_path}/{font_name}-Bold.{font_type}");
        }}
        .{font_name} {{ font-family: {font_name};}}
        p.{font_name} {{ font-size: {font_size}pt; }}
        '''

html = HTML(string=html)
css = CSS(string=css, font_config=font_config)

html.write_pdf(
    'weasyptint-thai.pdf', stylesheets=[css], font_config=font_config)
