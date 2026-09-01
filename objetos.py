"""
class Perro{
    public string Nombre {get;set;}
    public int Edad {get;set;}
    public Perro(){
        Edad = 0;
    }
    public Perro(string nombre, int edad){
        this.Nombre = nombre
        this.Edad = edad;
    }
    public string Ladrar(){
        return $"Guau {this.Nombre}";
    }
    public override string ToString(){
        return $"{this.Nombre} tiene {this.Edad} años"
    }
}
Perro p = new Perro();
Perro q = new Perro("Fido", 5);
Console.WriteLine(q)
"""
class Perro:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self)->str:
        return f"Guau {self.nombre}"
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"
    
p = Perro();
q = Perro("Fido", 5);
print(q.ladrar())
print(q)