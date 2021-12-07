from lib import spoke, wheel

def createWheel(wheelType='European'):
    """
    Creates an initial instance of a Wheel according to the wheelType (can be American or European)
    """
    if wheelType == 'European':
        zero_spoke = spoke.Spoke(0, 'green')
        spokes = [spoke.Spoke(i, 'red') if (i % 2) == 0 else spoke.Spoke(i, 'black') for i in range(1, 37, 1)]

        full_spokes = [zero_spoke, *spokes]
        
        new_wheel = wheel.Wheel(full_spokes, wheelType)
        return new_wheel


def main():
    Wheel = createWheel()
    # print(Wheel)
    print([Wheel.spin() for i in range(0, 100)])

    return 'Complete'



if __name__ == '__main__':
    main()