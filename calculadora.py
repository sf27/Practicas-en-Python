#/usr/bin env python
# -*- encoding: utf-8 -*-

""" 
	Programación Funcional
	Ejemplo de una calculadora sencilla utilizando funciones de orden superior y lambdas
	Autor: Elio Rincón
"""
from __future__ import division
from string import digits as digitos

def fn(a):
	def operacion(fnO):
		def fny(b):
			return fnO(a, b)
		return fny
	return operacion 

def menu():
	print "\nMenú Principal"
	print "0. Salir"
	print "1. Sumar"
	print "2. Restar"
	print "3. Multiplicar"
	print "4. Dividir"
	option = raw_input("Seleccione su opción: \n")
	return 0 if option not in list(digitos) else int(option)

def datos_entrada():
	x = float(raw_input("Ingrese X: "))
	y = float(raw_input("Ingrese Y: "))
	return x, y

def Principal():
	opcion = menu()
	if opcion > 0 and opcion < 5: 
		operaciones = {1: lambda x, y: x+y,
					   2: lambda x, y: x-y,
			           3: lambda x, y: x*y,
			           4: lambda x, y: "ZeroDivisionError: integer division or modulo by zero" if y == 0 else float(x/y)}
		a, b = datos_entrada()
		operacion = operaciones[opcion]
		resultado = fn(a)(operacion)(b)
		#resultado = fn(5)(mas)(4) => 9
		#resultado = fn(5)(menos)(4) => 1
		#resultado = fn(5)(por)(4) => 20
		#resultado = fn(5)(entre)(4) => 1.25
		print "\n\nResultado: {r}".format(r=resultado)
		print raw_input("Presione Enter para continuar...")
		return Principal()


Principal()
