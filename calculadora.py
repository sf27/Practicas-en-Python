#/usr/bin env python
# -*- encoding: utf-8 -*-

""" 
	Programación Funcional
	Ejemplo de una calculadora sencilla utilizando funciones de orden superior y lambdas
	Autor: Elio Rincón
"""

def fn(a):
	def operacion(fnO):
		def y(b):
			return fnO(a, b)
		return y
	return operacion 

def Principal():
	print "\nMenú Principal"
	print "0. Salir"
	print "1. Sumar"
	print "2. Restar"
	print "3. Multiplicar"
	print "4. Dividir"
	return int(raw_input("Seleccione su opción: \n") or 0)

def input_num():
	x = int(raw_input("Ingrese X: "))
	y = int(raw_input("Ingrese Y: "))
	return x, y

def opciones():
	opcs = {1: lambda x, y: x+y,
			2: lambda x, y: x-y,
			3: lambda x, y: x*y,
			4: lambda x, y: "ZeroDivisionError" if y == 0 else x/y}
	opc = Principal()
	if opc > 0 and opc < 5: 
		a, b = input_num()
		operacion = opcs[opc]
		resultado = fn(a)(operacion)(b)
		#resultado = fn(5)(suma)(4)
		print "\n\nResultado: " + str(resultado) + "\n\n" 
		print raw_input("Presione Enter para continuar...")
		return opciones()


opciones()
