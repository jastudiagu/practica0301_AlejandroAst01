import datetime

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)



inicio = datetime.datetime.now()

print(fibonacci(1))

final = datetime.datetime.now()

tiempo = final - inicio

print(tiempo)