from datetime import timedelta, date, datetime
from .models import destination
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
def simple():

    dests = destination.objects.all()
    dic = {}
    k=1
    for dest in dests:
        if (k==1):
            Total =  dest.Total
            my_date = dest.start
            noofquarantine = dest.num_quarantine
            nonq = dest.num_free
            Total_rooms = dest.room
            Quarantine_days = dest.num_quarantine
            num_days=(Total-noofquarantine-nonq)//Total_rooms
            remaining = (Total-noofquarantine-nonq) % Total_rooms
            if (remaining!=0):
                num_days+=1
            total_days = Quarantine_days * num_days
            date = []
            rem = []
            slot = []
            li=[]
            for j in range(num_days):
                date1 = my_date + timedelta(days=(Quarantine_days)*j)
                slot1 = 'S' + str(j + 1)
                Remaining = (Total - noofquarantine - nonq) -(Total_rooms*(j+1))
                date.append(date1)
                slot.append(slot1)
                if j == num_days - 1:
                    rem.append(0)
                else:
                    rem.append(Remaining)
                li.append(j)
            

            end_date = my_date + timedelta(days=total_days-Quarantine_days)
            zipped_list = zip(date, rem, slot)
            
            # dic={'end':end_date,'slots':slot,'rem':rem,'date':date,'num':li}
            k+=2
    # Total = (request.GET['total'])
    # my_date = (request.GET['startdate'])
    # noofquarantine = (request.GET['noofquarantine'])
    # nonq = (request.GET['nonq'])
    # Total_rooms = (request.GET['room'])
    # Quarantine_days = (request.GET['qt'])
    # num_days=(Total-noofquarantine-nonq)//Total_rooms
    # remaining=Total%Total_rooms
    # if (remaining!=0):
    #     num_days+=1
    # total_days = Quarantine_days * num_days
    
    # end_date = my_date + timedelta(days=total_days)
    # d = {'enddate': end_date, 'quara': noofquarantine, 'free': nonq}
    return zipped_list,end_date

