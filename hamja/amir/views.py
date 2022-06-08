from django.shortcuts import render
from datetime import datetime

def a(request):
    nam = request.POST.get('name')
    ro = request.POST.get('roll')
    dep = request.POST.get('dept')
    sem = request.POST.get('sem')

    d= datetime.now()
    name = "Amir Hamja"
    roll = 123456
    semester = '8th'
    department = 'Computer Technology'
    all_inf = {'n': name, 'r': roll, 's': semester, 'd': department, 'dt': d, 
    'nm': nam, 'roll': ro, 'dept': dep, 'sem':sem}
    return render(request, 'a.html', all_inf )
