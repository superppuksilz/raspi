import module.frontviewCall as frontviewCall
import module.rearview as rearview
import module.emergency as emergency
import module.requestReceiver as reqReceiver 


# main pi, used in Rearview, Bluetooth

fvcall = frontviewCall.FrontViewCall()
rv = rearview.RearView()
emer = emergency.Emergency()

reqReceiver.start()

IDLE = 0
FRONT = 1
REAR = 2

modeStat = IDLE


#modeStat = FRONT

        


while True:
    
    modeStat = reqReceiver.get_status()
    print(modeStat)
    if modeStat ==  IDLE or modeStat == REAR:
	modeStat = rv.showView(modeStat)
    else :
	modeStat = fvcall.showView(modeStat)
