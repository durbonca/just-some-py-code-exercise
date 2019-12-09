def run():
    print('CALCULAME LA DIVISA')
    print('convertir pesos mex a pesos col')
    print('')
    amount = float(input('ingresa la cantidad de mex '))
    result = foreing_exchange_calculator(amount)
    print('resultado de mex $ {} a col es $ {}'.format(amount, result))
    print('')

def foreing_exchange_calculator(amount):
        mex_to_col_rate = 145.97
        return mex_to_col_rate * amount

if __name__ == "__main__":
    run()