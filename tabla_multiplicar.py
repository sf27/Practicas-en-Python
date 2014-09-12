#/usr/bin env python
#-*- encoding:utf-8 -*-

#high order functions
def tabla(a=1):
  def num(b=1):
	return a * b
  return num

print("Tabla de multiplicar")
n = int(raw_input("Ingrese un numero: "))
e = tabla(n)
for i in range(1, 11):
	print " {a} * {b}  = {r}".format(a=n, b=i, r=e(i))

