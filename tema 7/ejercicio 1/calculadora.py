import calculadora.divisor.division as divide
import calculadora.multiplicador.multiplicacion as multi
import calculadora.restador.resta as subs
import calculadora.sumador.suma as add

def main():
    print("10 + 5 =",add.sumar(10,5))
    print("10 - 5 =",subs.restar(10,5))
    print("10 X 5 =",multi.multiplicar(10,5))
    print("10 / 5 =",divide.dividir(10,5))

if __name__ == "__main__":
    main()