import win10toast
import psutil
import time
while True:
    toaster=win10toast.ToastNotifier()
    battery=psutil.sensors_battery()
    plugged=battery.power_plugged
    percent=str(battery.percent)
    if plugged==False:
        plugged="Not Plugged in"
    else:
        plugged="Plugged In"
    toaster.show_toast('Python' , percent+"%  |"+plugged, duration=5)
    time.sleep(30)



