def test_function():
    def inner_function():
        print('Я внутри функции test_function')
    inner_function()

test_function()
#inner_function() #выдаёт ошибку т.к. inner_function() существует только в функции test_function()
print(globals()) #test_function() является глобальной