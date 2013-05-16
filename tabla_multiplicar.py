#/usr/bin env python
#-*- encoding:utf-8 -*-

<<<<<<< HEAD
def tabla(a=1):
	def num(b=1):
		return a * b
	return num
=======
#high order functions
def tabla(a=1):
  def num(b=1):
	return a * b
  return num
>>>>>>> c227a7289879cdc7b928b7f114fc98a304bb94fb

print("Tabla de multiplicar")
n = int(raw_input("Ingrese un numero: "))
e = tabla(n)
for i in range(1, 11):
	print " {a} * {b}  = {r}".format(a=n, b=i, r=e(i))
<<<<<<< HEAD











=======
>>>>>>> c227a7289879cdc7b928b7f114fc98a304bb94fb
