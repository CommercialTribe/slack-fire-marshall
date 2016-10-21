# say a random arnold quote from list on OSx command line
from random import randint
from subprocess import call

qs = [
    "To crush your enemies, see them driven before you, and to hear the lamentation of their women!",
    "Your clothes, give them to me, now!",
    "Do it!",
    "If it bleeds, we can kill it",
    "See you at the party Richter!",
    "Let off some steam, Bennett",
    "I'll be back",
    "Get to the chopper!",
    "Hasta La Vista, Baby!",
    "Now this is the plan : Get your ass to Mars!",
    "It's not a tumor!",
    "I live to see you eat that contract, but I hope you leave enough room for my fist, because I'm going to ram it into your stomach and break your goddamn spine! RAAGH!",
    "Dillon, you son of a bitch!",
    "You hit like a vegetarian!",
    "What the fuck did I do wrong?!"]

q = randint(0,9)

call(["say", "-v", "Daniel", qs[q]])

