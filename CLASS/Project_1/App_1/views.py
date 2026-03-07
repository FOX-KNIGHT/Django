from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<body style="background-color: #3e5b50; font-family: sans-serif; padding: 20px;">
                            <h1>Welcome to my First Django Project <img src="https://tse1.mm.bing.net/th/id/OIP.AnEcLPA3x4bruESvEyj4CQHaHa?rs=1&pid=ImgDetMain&o=7&rm=3" alt="Django Logo" height ="50" width="50"></h1>
                            <h3>Name: Siddhant</h3>
                            <ul>
                                <li style="color:Orange;">Regd.No: 24E110A78</li>
                                <li style="color:white">DOB: 16-07-2007</li>
                                <li style="color:green;">Dept: CSE-core</li>
                            </ul>
                        </body>''')

def Info(request):
    return HttpResponse("""<h1>INFORMATION SECTION ==></h1>
                        <h3 style="color:Orange;">Name: Siddhant</h3>
                        <p style="color:blue">Redg.No= 24E110A78</p>
                        <p>DOB: 16-07-2007</p>
                        <p style="color:green;">Dept: CSE-core</p>""")