# -*- coding: utf-8 -*-
class Equipo:
	
    def __init__(self, nombre, entrenador, estadio, puntos):
        """
            Inicializa los datos de un equipo
            Parameters:
            nombre:str  -- nombre del equipo
            entrenador:str-- entrenador del equipo
            estadio:str -- estadio del equipo
            puntos:int -- puntos del equipo
        
        """
        self.__nombre = nombre
        self.__entrenador = entrenador
        self.__estadio = estadio 
        self.__puntos =  puntos
    
    def setNombre(self, nombre):
        """
        Establece el nombre del equipo
        Parameters:
        nombre: str -- nombre del equipo
        """
        self.__nombre = nombre

    def setEntrenador(self, entrenador):
        """
        Establece el entrenador del equipo
        Parameters:
        entrenador: str -- nombre del entrenador
        """
        self.__entrenador = entrenador
    
    def setEstadio(self, estadio):
        """
        Establece el estadio del equipo
        Parameters:
        estadio: str -- nombre del estadio
        """
        self.__estadio = estadio
    
    def setPuntos(self, puntos):
        """
        Establece el número de puntos del equipo
        Parameters:
        puntos: int -- número de puntos del equipo
        """
        self.__puntos = puntos
        
    def getNombre(self):
        """
        Brinda el nombre del equipo
        Parameters:
        none
        """
        return self.__nombre
    
    def getEntrenador(self):
        """
        Brinda el entrenador del equipo
        Parameters:
        none
        """
        return self.__entrenador
    
    def getEstadio(self):
        """
        Brinda el estadio del equipo
        Parameters:
        none
        """
        return self.__estadio
    
    def getPuntos(self):
        """
        Brinda el número de putnos del equipo
        Parameters:
        none
        """
        return self.__puntos
        
    def __str__(self):
        """
        Regresa todos los datos del equipo
        Parameters:
        none
        """
        return "Nombre: " + self.__nombre + "Entrenador: " + self.__entrenador + "Estadio: "+ self.__estadio+ str(self.__puntos)



  