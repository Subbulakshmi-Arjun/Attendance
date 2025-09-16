from django.shortcuts import render
from .models import Attendance
from datetime import datetime,date

# Create your views here.
def index(request):
    today=date.today()
    now_time=datetime.now().time()
    message=""
    if request.method == "POST":
        staff_no=request.POST["no"]
        mode=request.POST["mode"]
        o, created = Attendance.objects.get_or_create(Staffid=staff_no, Date=today)

        if mode=="in":
            if o.punch_in_time is None:
                o.punch_in_time=now_time
                o.save()
                message="Punch in recorded"
            else:
                message="you are already punch in today"
        elif mode=="out":
            if o.punch_out_time is None:
                o.punch_out_time=now_time
                o.save()
                message="Punch out recorded"
            else:
                message="you are already punch out today"
    context={"today":today,
             "now_time":now_time.strftime("%H:%M"),
            "message":message}


            
    return render(request,'app/attendance.html',context)
    
    
