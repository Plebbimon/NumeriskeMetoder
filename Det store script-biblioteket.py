# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:51:52 2020

@author: sebbe
"""

#Dette er MYE å lese gjennom, men jeg vil heller at det skal stå litt for mye dritt enn litt for lite info :P


import numpy as np
from scipy.misc import derivative

#|-------------------------------------------|


#Her kan vi definere funksjonen som programmene kjører gjennom!
def funksjon(x):
    #return (-1)*np.sqrt(x) #Uttrykket fra noen eksamensoppgaver
    return (-1)*np.sqrt(x)


#|-------------------------------------------|


def funksjon_derivert(x):
    return derivative(funksjon,x)





#|-------------------------------------------|



#FIKSPUNKTITERASJON MED WHILE
def fikspunkt_while():
    print("FIKSPUNKT | WHILE:")
    #Litt forhåndsarbeid for å få x og et tall for nøyaktighet:
    x = float(input("Gjett en startverdi for x: ")) #Gjetter en x-verdi
    presisjon = float(input("Velg en størrelse for nøyaktighet/iterasjoner (desimaltall som 0.0001): ")) #Velger hvor presist svar vi vil ha, altså hvor mange ganger koden kjører gjennom før den er fornøyd
    i = 0 #Teller antall iterasjoner for ekstra informasjon om kjøringen
    
    #Denne setter vi for å starte at koden kjører inn i loopen
    x0 = x-1
    
    #Her er selve fikspunktiterasjonen:
    while abs(x-x0) > presisjon: #Mens forskjellen mellom forrige x og nye x er større enn målet for presisjon, så kjører denne!
        x0 = x #Setter ny verdi for gammel x hver gang koden kjører gjennom for å få nest siste x før koden sjekker for forskjellen (abs(x-x0))
        x = funksjon(x) #Dette er hele fikspunkt, at x = f(x_n), bare at her oppdaterer vi gammel x til en ny x, i stedet for å bruke "n"
        i+=1 #Denne bare teller oppover for hver "while"-loop
        
    #Dette gir koden ut:
    return x, i


        
#print(fikspunkt_while())



#|-------------------------------------------|



def fikspunkt_for(): #Fungerer fint denne her også, men pass på for numpy errors ved for høy grad av iterasjoner kombinert med spicy funksjoner
    print("FIKSPUNKT | FOR:")
    #Litt forhåndsarbeid for å få x og et tall for nøyaktighet:
    x = float(input("Gjett en startverdi for x: "))
    iterasjoner = int(input("Velg antall iterasjoner: "))
    
    #Her er selve fikspunktiterasjonen:
    for i in range(iterasjoner): #Mens forskjellen mellom forrige x og nye x er større enn målet for presisjon, så kjører denne!
        x = funksjon(x) #Dette er hele fikspunkt, at x = f(x_n), bare at her oppdaterer vi gammel x til en ny x, i stedet for å bruke "n"
        
    #Dette gir koden ut:
    return x, iterasjoner


        
#print(fikspunkt_for())



#|-------------------------------------------|


def implisitt_for():
    #Forhåndsarbeid for en startverdi og antall iterasoner, samt steg
    y = float(input("Startverdi implisitt metode: "))   #Bruker y fordi implisitt metode er uttrykt ved y(t0)=y0
    n = int(input("Antall iterasjoner: "))
    h = 1/n #h er størrelsen på stegene som tas for hver iterasjon, her er den satt til 1/n for kompatabilitet

    for k in range(n): #En kjekk liten for-løkke, den tar 
        z=y #Dette blir nåværende y, mens linjen skriver neste y som uttrykt ved vår nåværende y og steg
        for i in range(n):
            y=z+h*funksjon(y) #Dette er selve implisitte metode | VIKTIG - "y" er y_(k+1), mens "z" er y_k
    
    return y
            
#print(implisitt_for())


#|-------------------------------------------|



def eksplisitt_for():
     #Forhåndsarbeid for en startverdi og antall iterasoner, samt steg
    y = float(input("Startverdi eksplisitt metode: "))   #Bruker y fordi implisitt metode er uttrykt ved y(t0)=y0
    n = int(input("Antall iterasjoner: "))
    h = 1/n #h er størrelsen på stegene som tas for hver iterasjon, her er den satt til 1/n for kompatabilitet
    
    #Selve algoritmen for eksplisitt metode
    for i in range(n):
        y = y + h*funksjon(y) #For hver kjøring oppdaterer y seg selv med et nytt uttrykk for y(altså y_k+1) som bruker nåværende y
   
    return y


#print(eksplisitt_for())



#|-------------------------------------------|



def newtons_metode():
    x = int(input("Gjett en x: "))
    grense = float(input("Grense (f.eks 0.0001): "))
    i=0
    
    while True:
        x0=x #Forrige x, også kalt x_0
        x = x - funksjon(x) / funksjon_derivert(x)
        steg = abs(x-x0) #Regner delta/differanse mellom forrige x og nye x
        
        if steg < grense: #Sjekker når stegene begynner å bli mindre enn grensen vi har satt
            break #Bryter while-løkken, vi sier oss fornøyde
            
        i+=1 #Teller antal iterasjoner
        
    return x,i #x-verdi og iterasjoner


#print(newtons_metode())




#|-------------------------------------------|

#TRAPES RIEMANN-AREAL
def trapes_areal():
    nedre_grense = float(input("Nedre grense(a): "))
    ovre_grense = float(input("Øvre grense(b): "))
    steg = 1/int(input("Antall steg i heltall: "))
    summ = 0 #Dette er det samlede arealet vi skal frem til
    
    x = nedre_grense #vi starter med x i a
    #while-løkken går så lenge x ikke når vår b-verdi i integralet fra a til b
    while (x < ovre_grense):
        venstre_y = funksjon(x) #venstre y-verdi for trapeset vårt
        hoyre_y = funksjon(x+steg) #høyre y-verdi for trapeset vårt
        #"areal" under er arealet for hvert trapes som lages, basert på antall steg i integralet/summen
        areal = 0.5 * steg * (venstre_y+hoyre_y)
        summ += areal #Arealet legges til total areal
        x += steg #Øker x-verdien med steglengden, slik at vi kan regne ut arealet for neste trapes
        
    return summ, 1/steg


    
#print(trapes_areal())



#|-------------------------------------------|


#TRAPESMETODEN
def trapes_difflikning():
    y = float(input("Sett inn y: "))
    n = int(input("Antall steg: "))
    h = 1/n
    for i in range(n):
        z=y
        for k in range(n):
            y=z + (1/2) * h * (funksjon(z)+funksjon(y))
            
    return y

#print(trapes_difflikning())



#|-------------------------------------------|


#RIEMANN
def riemann():
    nedre_grense = float(input("Nedre grense(a): "))
    ovre_grense = float(input("Øvre grense(b): "))
    n = int(input("Antall steg i heltall: "))
    #"steg" er en størrelse på hvor stort hvert steg blir, som utgjør lengden på hvert rektangel(areal)
    steg = (ovre_grense - nedre_grense)/n #steget definert av intervallet, delt på antall steg vi tenker å ta
    summ = 0 #arealet totalt
    
    x = nedre_grense #begynner i nedre grense
    while (x < ovre_grense): #helt til den når øvre grense
        areal = funksjon(x)*steg #areal for hvert rektangel
        summ += areal #rektangelet legges til total areal
        x += steg #steg videre
        
    return summ #returnerer totalt areal


#print(riemann())

