import keyboardmodule as km
from motor import Motor
km.init()
wheel=Motor()
while True:
    if km.getKey('w'):
        print('forward')
        wheel.forward(100)
    elif km.getKey('s'):
        print('backward')
        wheel.backward(100)
    else:
        wheel.stop(0)