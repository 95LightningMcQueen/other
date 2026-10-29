import math

def taylor_ln(x:float,eps:float) -> tuple[float, int]:
    
    if x < -1 or x > 1:
        print('Данный ряд расходится при значениях >= 1 и < -1.')

    total_sum: float = 0.0
    denom_fac: int = 1
    first: float = -x

    while abs(first) > eps:
        total_sum += first
        denom_fac += 1
        first = -math.pow(x,denom_fac) / denom_fac

    return total_sum, denom_fac


x: float = 0.2
eps: float = 0.0001

result,iterations = taylor_ln(x,eps)
print(f'Итоговое значение: {result:.6f}. Кол-во итераций: {iterations}.')