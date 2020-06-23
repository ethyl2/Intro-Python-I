def testing_not_none(my_value=None):
    if my_value:
        print("Here's my value: " + str(my_value))
    else:
        print("I guess my value is None?: " + str(my_value))
    if my_value is not None:
        print("Here's my value again: " + str(my_value))
    else:
        print("I guess my value is None again: " + str(my_value))
    print('\n')


testing_not_none("pizza")
testing_not_none()
testing_not_none(None)
testing_not_none(False)
testing_not_none(True)
testing_not_none([])
