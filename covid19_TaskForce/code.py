from datetime import timedelta, date, datetime
def code(request):
    Total = (request.GET['total'])
    my_date = (request.GET['startdate'])
    noofquarantine = (request.GET['noofquarantine'])
    nonq = (request.GET['nonq'])
    Total_rooms = (request.GET['room'])
    Quarantine_days = (request.GET['qt'])
    num_days=Total//Total_rooms
    remaining=Total%Total_rooms
    if (remaining!=0):
        num_days+=1
    total_days = Quarantine_days * num_days
    
    end_date = my_date + timedelta(days=total_days)
    d = {'enddate': end_date, 'quara': noofquarantine, 'free': nonq}
    return (d)

