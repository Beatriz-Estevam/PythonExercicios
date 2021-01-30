from math import cos, sin, tan, pi

rad = float(input('Valor do ângulo (em graus): '))
angulo = (rad*pi)/180
print(25*('-'))
print('O Seno de {} é: {:.3f}'.format(angulo, sin(angulo)))
print('O Cosseno de {} é: {:.3f}'.format(angulo, cos(angulo)))
print('A Tangente de {} é: {:.3f}'.format(angulo, tan(angulo)))
print(25*('-'))
