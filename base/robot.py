#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class Robot:

	def __init__(self, nom = "C3PO"):
		self.nom = nom
		self.position = 0, 0

	def __str__(self):
		return "Bonjour à vous, je m'appelle {0} et j'ai besoin de votre aide pour sortir du labyrinthe.".format(self.nom)

	def __repr__(self):
		return "<Robot de Roboc>"
		
	def move(value):
		if nbr = value[1:] = "":
			nbr = 1
		try:
			nbr = int(value[1:])
		except:
			print("Merci d'entrer un nombre pour les autres caractères.")

		try:
			direction = value[0]
		except:
			print("Merci d'entrer N, E, S ou W comme premier caractère.")
		if direction.lower() = "n":
			self.position = y - nbr, x
		elif direction.lower() = "e":
			self.position = y, x + nbr
		elif direction.lower() = "s":
			self.position = y + nbr, x
		elif direction.lower() = "w":
			self.position = y, x - nbr
		print(self.position)