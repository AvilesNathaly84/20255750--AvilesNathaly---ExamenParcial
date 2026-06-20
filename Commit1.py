# commit 1

class Recurso:
    def __init__(self, codigo_identificador: str):
        self.codigo_identificador = codigo_identificador
        self.multa = 0

    def calculo_multa(self):
        pass
        
class Bibliotecario:
    def __init__ (self, nombre_empleado: str, codigo_usuario: str):
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario

class RegistroAtencion:
    def __init__(self, codigo_unico: str, carnet_alumno: str, nombre_empleado: str, codigo_usuario: str ):
        self.codigo_unico = codigo_unico
        self.carnet_alumno = carnet_alumno
        self._recursos: list[Recurso] = []
        self.bibliotecario = Bibliotecario(nombre_empleado, codigo_usuario)

    def cargarRecursos(self, recurso: Recurso):
        if len(self._recursos) >= 4:
            raise ValueError ("Límite de recursos por atención alcanzado")
        self._recursos.append(Recurso)

    def desvincularRecurso(self, codigo_identificador: str):
        if not self._recursos:
            print("La lista de recursos se encuentra vacía")
            return
        for r in self._recursos:
            if codigo_identificador == r.codigo_identificador:
                self._recursos.remove(r)
                return
        print("Código identificador no encontrado")

@property
def recursos(self):
    return tuple(self._recursos)

class PrestamoLibro(Recurso):
    def __init__(self, codigo_identificador:str):
        super(self, codigo_identificador)
    
    def calculo_multa(self):
        self.multa-= 2.5
        return self.multa

class UsoSaleEstudio(Recurso):
    def __init__(self, codigo_identificador):
        super().__init__(codigo_identificador)
    
    def calculo_multa(self, horas_exceso: int, factor: float):
        self.multa += horas_exceso * factor
        return self.multa