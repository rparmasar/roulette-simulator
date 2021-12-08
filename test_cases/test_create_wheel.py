from lib import wheel

def testWheelCreate():
    test_wheel = wheel.createWheel()
    assert(isinstance(test_wheel, wheel.Wheel))