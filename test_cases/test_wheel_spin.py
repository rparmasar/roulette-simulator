from lib import wheel, wheel_spoke

def testWheelSpin():
    test_wheel = wheel.createWheel()
    test_spin = test_wheel.spin()
    assert(isinstance(test_spin, wheel_spoke.Spoke))


    
