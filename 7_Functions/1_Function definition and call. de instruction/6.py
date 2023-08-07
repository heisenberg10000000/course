def get_body_mass_index(weight, height):

    height_m = height / 100

    index = weight / (height_m ** 2)


    if index < 18.5:

        print("Недостаточная масса тела")

    elif index <= 25:

        print("Норма")

    else:

        print("Избыточная масса тела")

