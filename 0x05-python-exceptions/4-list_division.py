#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ite in range(list_length):
        try:
            res = my_list_1[ite] / my_list_2[ite]
        except(TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            new_list.append(res)
    return(new_list)
