from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def APP():
    put_html('<center><h3>استمارة الطالب المقبول</h3></center>').style('background-color:#154D71; color:gold; padding:25px')
    put_html('<p> تصدير السيرة الذاتية للطلاب المؤهلين للدراسة</p>').style('text-align:center; font-weight:bold;')
    put_html('<center> <img src="https://undergrad.umn.edu/sites/undergrad.umn.edu/files/2024-01/student-success_lockup_horizontal.png" width="400px"> </center>')
    data = input_group(
        'ملى استمارة الطالب المتفوق المؤهل',
        [
            input('اسم الطالب',name='student'),
            input('عنوان الطالب',name="addrs"),
            input('البريد الالكتروني',name='email'),
            input('رقم الهاتف',name='phone',type=NUMBER),
            radio('مؤهلات الطالب',options=['DIBLOMA','Bachelor.s','High school'],name='CERTI'),
            checkbox('اتقان اللغات',options=['Arabic','English'],inline=True,name='lang')

        ]



    )
    imgs= file_upload(
        'تحميل صورة شخصية',
        accept='image/*',
        multiple=True
    )
    for img in imgs:
        global rr 
        rr=img['content']

    put_text('Student CV :')
    put_table([

        ['Studentimg','Name','Address','email','Phone','Certificate','Languge'],
        [put_image(rr).style('width:50px;'),data['student'],data['addrs'],data['email'],data['phone'],data['CERTI'],data['lang']]
    ])




start_server(APP,port=3335,debug=True)
