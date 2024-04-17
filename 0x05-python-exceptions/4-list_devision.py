#!/usr/bin/python3
def def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("Wrong type")
            res = 0
        except zeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
