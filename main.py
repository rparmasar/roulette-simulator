from lib import wheel, wheel_spoke

def main():
    Wheel = wheel.createWheel()
    # print(Wheel)
    print([Wheel.spin() for i in range(0, 100)])

    return 'Complete'



if __name__ == '__main__':
    main()