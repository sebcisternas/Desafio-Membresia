from abc import ABC, abstractmethod

# Clase abstracta que contendrá los comportamientos para los tipos de membresía a implementar
class  Membresia (ABC):
    
    # Constructor
    def __init__(self, correo_subs: str, num_tarjeta: str): 
        self.__correo_subs = correo_subs
        self.__num_tarjeta = num_tarjeta
        
    # Getter
    # Método que devuelve el correo del suscriptor
    @property
    def correo_subs(self):
        return self.__correo_subs
    # Método que devuelve el número de tarjeta 
    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int ):
        pass 
     # El método será modificado en cada clase para comportarse de cierta manera según la situación.
     # Se le coloca un pass porque no tiene implementación lógica. 
    
    # Método para crear una nueva membresía, con acceso protegido
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1: 
            return MembresiaBasica(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 2: 
            return MembresiaFamiliar(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 3: 
            return MembresiaSinConexion(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 4: 
            return MembresiaPro(self.correo_subs, self.num_tarjeta)
    
class MembresiaGratis(Membresia):
    
    # Atributos
    costo = 0 
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia: int):
      
        if nueva_membresia < 1 or nueva_membresia > 4: 
            return self
        else: 
            return self._crear_nueva_membresia(nueva_membresia)
    
class MembresiaBasica(Membresia):
    # Clase para la membresía básica
    
    costo = 3000
    cantidad_dispositivos = 2
    
    # Constructor de la membresía básica, que también llama al constructor de la clase padre 'Membresia'
    def __init__(self, correo_subs: str, num_tarjeta: str):
        super().__init__(correo_subs, num_tarjeta)
        
        # Se define el atributo 'dias_regalo' según el tipo de membresía
        if isinstance(self, MembresiaFamiliar) or isinstance(self, MembresiaSinConexion):
            self.dias_regalo = 7 
        elif isinstance(self, MembresiaPro):
            self.dias_regalo = 15
        
    def cancelar_suscripcion(self):
        return MembresiaGratis(self.correo_subs, self.num_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        if nueva_membresia < 2 or nueva_membresia > 4: 
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
        # Si no, creará la nueva membresía tipo gratis

# Se utiliza la clase 'Membresia_Basica' para heredar sus atributos y métodos
class MembresiaFamiliar(MembresiaBasica):
    
    # Atributos de clase
    costo = 5000
    cantidad_dispositivos = 5 
    
    # Método para cambiar la suscripción
    def cambiar_suscripcion (self, nueva_membresia: int):
        # Si la membresía nueva no está entre los tipos permitidos, retorna la misma membresía
        if nueva_membresia not in [1,3,4]:    
            return self 
        else: # Si no, crea la nueva membresía de tipo familiar
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass
    # No se ha definido aún la lógica de este método
    
class MembresiaSinConexion(MembresiaBasica):
    
    # Atributos de clase 
    costo = 3500
    cantidad_dispositivos = 2
    
    # Método para cambiar la suscripción
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_contenido(self):
        pass
    # Este método no tiene sentido(?)
    
class MembresiaPro(MembresiaFamiliar,MembresiaSinConexion,MembresiaBasica):
    
    # Atributos de clase
    costo = 7000
    cantidad_dispositivos = 6
    
    def __init__(self, correo_subs: str, num_tarjeta: str):
        super().__init__(correo_subs, num_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia >3: 
            return self
        else: 
            return self._crear_nueva_membresia(nueva_membresia)
        
# Casos de prueba
# Caso 1: Crear una membresía gratis
g = MembresiaGratis("correodeprueba@correo.cl", "123")
print(type(g))

# Caso 2: Cambiar de gratis a básica 
# Se crea un objeto básico y se cambia la suscripción pasándole un uno
basica = g.cambiar_suscripcion(1)
print(type(basica))

# Caso 3: Cambiar de básica a familiar 
f = basica.cambiar_suscripcion(2)
print(type(f))

# Caso 4: Cambiar a Sin Conexión 
sc = f.cambiar_suscripcion(3)
print(f.dias_regalo)
print(type(sc))
print ("días de regalo: ", sc.dias_regalo)

# Caso 5: Cambiar a Pro 
p = sc.cambiar_suscripcion(4)
print(type(p))
print("Costo:",p.costo)
print ("días de regalo: ", p.dias_regalo)

# Caso 6: Cancelar suscripción 
# Volvemos a la membresía gratis
c =  p.cancelar_suscripcion()
print(type(c))

# Conclusión: 
# Se aplicó Herencia, Herencia múltiple y polimorfismo al ver comportamientos diferentes para un mismo método
# Se utilizó encapsulación, ya que los atributos están protegidos.