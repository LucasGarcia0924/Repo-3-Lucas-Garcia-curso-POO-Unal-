class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0) -> None:
    self.x = x
    self.y = y
  def move(self, new_x: float, new_y: float) -> None:
    self.x = new_x
    self.y = new_y
  def reset(self) -> None:
    self.x = 0
    self.y = 0
  def compute_distance(self, point: "Point")-> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance

first_point = Point(x=1, y=1)
second_point = Point(x=2, y=2)

print(first_point.compute_distance(second_point))

class Rectangle:
    def __init__(self, **kwargs):
        method = kwargs.get("method", "1")
        if method == "1":
            corner: Point = kwargs.get("corner", Point())
            self.width = kwargs.get("width", 1)
            self.height = kwargs.get("height", 1)
            self.center = Point((corner.x + self.width) / 2, (corner.y + self.height) / 2)
        elif method == "2":
            Center: Point = kwargs.get("center", Point())
            self.center = Center
            self.width =  kwargs.get("width", 1)
            self.height = kwargs.get("height", 1)
        elif method == "3":
            corner1: Point = kwargs.get("corner1", Point())
            corner2: Point = kwargs.get("corner2", Point())
            self.width = abs(corner2.x - corner1.x)
            self.height = abs(corner2.y - corner1.y)
            self.center = Point((corner1.x + corner2.x) / 2, (corner1.y + corner2.y) / 2)
        else:
            lines: list = kwargs.get("lines", [])
            self.width = lines[0].length
            self.height = lines[1].length
            self.center = Point(
                (lines[0].start.x + lines[0].end.x) / 2,
                (lines[0].start.y + lines[1].end.y) / 2
            )

    def compute_area(self) -> float:
        area = self.width * self.height
        return area
    
    def compute_perimeter(self) -> float:
        perimeter = (self.width + self.height) * 2
        return perimeter
    
    def compute_interference_point(self, point: Point) -> bool:
        left = self.center.x - self.width / 2
        right = self.center.x + self.width / 2
        bottom = self.center.y - self.height / 2
        top = self.center.y + self.height / 2
        if left <= point.x <= right and bottom <= point.y <= top:
            print(f"El punto ({point.x}, {point.y}) está dentro del rectángulo.")
            return True
        else:
            print(f"El punto ({point.x}, {point.y}) está fuera del rectángulo.")
            return False

    def compute_interference_line (self, line: "Line") -> None:
        # Check if either endpoint is inside the rectangle
        if self.compute_interference_point(line.start) and self.compute_interference_point(line.end):
            print("La línea está completamente dentro del rectángulo.")
        elif self.compute_interference_point(line.start) or self.compute_interference_point(line.end):
            print("La línea intersecta el rectángulo.")
        else:
            print("La línea está completamente fuera del rectángulo.")
    
    def __str__(self) -> str:
        return f"Rectángulo centrado en ({self.center.x}, {self.center.y}) con ancho {self.width} y alto {self.height}."

class Square(Rectangle):
    def __init__(self, side: float = 1, center: Point | None = None):
        if center is None:
            center = Point()
        super().__init__(method="2", width=side, height=side, center=center)

    def __str__(self) -> str:
        return f"Cuadrado centrado en ({self.center.x}, {self.center.y}) con lado {self.width}."


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self) -> float:
        return self.start.compute_distance(self.end)

    def compute_slope(self) -> float:
        if self.end.x - self.start.x == 0:
            return float("inf")  # Pendiente infinita
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
    
    def compute_horizontal_cross(self) -> float:
        if self.slope == 0:
            return float("inf")  # Línea horizontal, no cruza el eje x
        return self.start.y - self.slope * self.start.x
    
    def compute_vertical_cross(self) -> float:
        if self.slope == float("inf"):
            return float("inf")  # Línea vertical, no cruza el eje y
        return self.start.x - (self.start.y / self.slope)
    def __str__(self) -> str:
        return f"Línea desde ({self.start.x}, {self.start.y}) hasta ({self.end.x}, {self.end.y})"

if __name__ == "__main__":
    while True:
        elegir = int(input("Elige una opción:\n1. Crear un rectángulo\n2. Crear un cuadrado\n3. Crear una línea\n4. Ver intersecciones\n5. Terminar el programa\n"))
        if elegir == 1:
            print("Creando un rectángulo, elige un método")
            while True:
                method = input("Esquina inferior izquierda (1), centro (2), 2 esquinas opuestas (3) o 4 líneas (4): ")
                if method not in ["1", "2", "3", "4"]:
                    print("Opción no válida. Inténtalo de nuevo.")
                    continue
                break

            if method == "1" or method == "2":
                width = float(input("Ancho del rectángulo: "))
                height = float(input("Alto del rectángulo: "))
            
            if method == "1":
                x = float(input("Coordenada x de la esquina inferior izquierda: "))
                y = float(input("Coordenada y de la esquina inferior izquierda: "))
                Corner_1 = Point(x, y)
                Rectangle_1 = Rectangle(method="1", corner=Corner_1, width=width, height=height)

            elif method == "2":
                x = float(input("Coordenada x del centro: "))
                y = float(input("Coordenada y del centro: "))
                Center = Point(x, y)
                Rectangle_1 = Rectangle(method="2", center=Center, width=width, height=height)

            elif method == "3":
                x1 = float(input("Coordenada x de la primera esquina: "))
                y1 = float(input("Coordenada y de la primera esquina: "))
                x2 = float(input("Coordenada x de la segunda esquina: "))
                y2 = float(input("Coordenada y de la segunda esquina: "))
                Corner_1 = Point(x1, y1)
                Corner_2 = Point(x2, y2)
                Rectangle_1 = Rectangle(method="3", corner1=Corner_1, corner2=Corner_2)

            else:
                print("Creando líneas, inicia por la base:")    
                print("Las líneas deben ser secuenciales y formar un rectángulo.")
                print("Para cada línea, ingresa las coordenadas de inicio y fin.")
                print("El inicio debe ser lo más abajo y a la izquierda posible.")
                lines: list = []
                bandera : bool = True
                while bandera == True:
                    for i in range(4):
                        print(f"Línea {i+1}:")
                        print("Inicio:")
                        x1 = float(input("Coordenada x: "))
                        y1 = float(input("Coordenada y: "))
                        print("Fin:")
                        x2 = float(input("Coordenada x: "))
                        y2 = float(input("Coordenada y: "))
                        start = Point(x1, y1)
                        end = Point(x2, y2)
                        line = Line(start, end)
                        lines.append(line)
                    for line in range(len(lines)-1, 1, -1):
                        if lines[line].start.x != lines[line-1].end.x and lines[line].start.y != lines[line-1].end.y:
                            print("Las líneas no forman un rectángulo. Inténtalo de nuevo haciendo las líneas secuenciales.")
                            lines.clear()
                            break
                        else:
                            bandera = False
                Rectangle_1 = Rectangle(method="4", lines=lines)
            print(Rectangle_1)
            print(f"Área: {Rectangle_1.compute_area()}")
            print(f"Perímetro: {Rectangle_1.compute_perimeter()}")
        elif elegir == 2:
            side = float(input("Lado del cuadrado: "))
            x = float(input("Coordenada x del centro: "))
            y = float(input("Coordenada y del centro: "))
            Center = Point(x, y)
            Square_1 = Square(side, Center)
            print(Square_1)
            print(f"Área: {Square_1.compute_area()}")
            print(f"Perímetro: {Square_1.compute_perimeter()}")
        elif elegir == 3:
            print("Creando una línea:")
            print("Inicio:")
            x1 = float(input("Coordenada x: "))
            y1 = float(input("Coordenada y: "))
            print("Fin:")
            x2 = float(input("Coordenada x: "))
            y2 = float(input("Coordenada y: "))
            start = Point(x1, y1)
            end = Point(x2, y2)
            Line_1 = Line(start, end)
            print(Line_1)
            print(f"Longitud: {Line_1.length}")
            if Line_1.slope == float("inf"):
                print("Pendiente: Infinita (línea vertical)")
            else:
                print(f"Pendiente: {Line_1.slope}")
            if Line_1.compute_horizontal_cross() == float("inf"):
                print("Corte horizontal: Infinito (línea horizontal)")
            else:
                print(f"Corte horizontal (eje y): {Line_1.compute_horizontal_cross()}")
            if Line_1.compute_vertical_cross() == float("inf"):
                print("Corte vertical: Infinito (línea vertical)")
            else:
                print(f"Corte vertical (eje x): {Line_1.compute_vertical_cross()}")
        elif elegir == 4:
            choice2 = str(input("¿Con qué figura quieres ver intersecciones?\n1. Rectángulo\n2. Cuadrado\n"))
            choice3 = str(input("¿Con qué figura quieres ver intersecciones?\n1. Punto\n2. Línea\n"))
            if choice2 == "1":
                if 'Rectangle_1' not in locals():
                    print("No has creado un rectángulo aún.")
                    continue
                if choice3 == "1":
                    x = float(input("Coordenada x del punto: "))
                    y = float(input("Coordenada y del punto: "))
                    Point_1 = Point(x, y)
                    Rectangle_1.compute_interference_point(Point_1)
                elif choice3 == "2":
                    if 'Line_1' not in locals():
                        print("No has creado una línea aún.")
                        continue
                    Rectangle_1.compute_interference_line(Line_1)
                else:
                    print("Opción no válida, intenta de nuevo.")
            elif choice2 == "2":
                if 'Square_1' not in locals():
                    print("No has creado un cuadrado aún.")
                    continue
                if choice3 == "1":
                    x = float(input("Coordenada x del punto: "))
                    y = float(input("Coordenada y del punto: "))
                    Point_1 = Point(x, y)
                    Square_1.compute_interference_point(Point_1)
                elif choice3 == "2":
                    if 'Line_1' not in locals():
                        print("No has creado una línea aún.")
                        continue
                    Square_1.compute_interference_line(Line_1)
                else:
                    print("Opción no válida, intenta de nuevo.")
            continue
        elif elegir == 5:
            print("Terminando el programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")