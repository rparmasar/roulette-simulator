from app.lib import spoke, wheel

def testWheelSpin():
    test_wheel = wheel.createWheel()
    test_spin = test_wheel.spin()
    assert(isinstance(test_spin, spoke.Spoke))


    
