def task2(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result.update({value: key})
    return result


print(task2(name=233, lastname=23, hername=22))

