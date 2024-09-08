
class Pizza:

    def __init__(self, variedad: str):
        self.variedad = variedad
    
    def establecer_variedad(self, variedad: str):
        self.variedad = variedad

    def obtener_variedad(self) -> str:
        return self.variedad

class MaestroPizzero:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre(self, nombre: str):
        self.nombre = nombre

    def obtener_nombre(self) -> str:
        return self.nombre

    def tomar_pedido(self, variedad: str):
        if isinstance(variedad, str):
            nueva_pizza = Pizza(variedad) 
            self.pizzas_por_cocinar.append(nueva_pizza) 

    def cocinar(self):
        if len(self.pizzas_por_cocinar) > 0:
            self.pizzas_por_entregar.extend(self.pizzas_por_cocinar) 
            self.pizzas_por_cocinar.clear()

    def entregar(self) -> list:
        pizzas_a_entregar = self.pizzas_por_entregar[:2]
        self.pizzas_por_entregar = self.pizzas_por_entregar[2:]
        return pizzas_a_entregar
    
    def obtener_pizzas_por_cocinar(self) -> list:
        return self.pizzas_por_cocinar

    def obtener_pizzas_por_entregar(self) -> list:
        return self.pizzas_por_entregar
    

class Mozo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pizzas = []

    def obtener_pizzas(self):
        return self.pizzas 

    def establecer_nombre(self, nombre: str):
        self.nombre = nombre

    def obtener_nombre(self) -> str:
        return self.nombre

    def tomar_pizzas(self, pizzas: list):
        pizzas_a_tomar = 2 - len(self.pizzas)
        self.pizzas.extend(pizzas[:pizzas_a_tomar])
    
    def servir_pizzas(self):
        self.pizzas.clear()

    def obtener_estado_libre(self) -> bool:
        return len(self.pizzas) < 2
    

class TesterPizzeria:
    def main(self):
      
        maestro = MaestroPizzero("Don Pipo")

        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Carlos")

        maestro.tomar_pedido("Muzzarella")
        maestro.tomar_pedido("Napolitana")
        maestro.tomar_pedido("Fugazzetta")
        

        maestro.cocinar()

        pizzas_para_mozo1 = maestro.entregar()
        mozo1.tomar_pizzas(pizzas_para_mozo1)
        pizzas_para_mozo2 = maestro.entregar()
        mozo2.tomar_pizzas(pizzas_para_mozo2)

      
        print("Pizzas que lleva Mozo1:", [pizza.obtener_variedad() for pizza in mozo1.obtener_pizzas()])
        print("Pizzas que lleva Mozo2:", [pizza.obtener_variedad() for pizza in mozo2.obtener_pizzas()])

        mozo1.servir_pizzas()
        mozo2.servir_pizzas()

        print("Mozo1 está libre:", mozo1.obtener_estado_libre())
        print("Mozo2 está libre:", mozo2.obtener_estado_libre())

if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()

list1 = [0, 1, 2, 3]



