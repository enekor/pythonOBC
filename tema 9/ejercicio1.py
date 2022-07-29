
def main():

    paises = []

    for x in range(5):
        paises.append(input(f'dime el pais numero {x+1}: '))

    paisesset = set(paises)
    print(list(sorted(paisesset)))

if __name__ == '__main__':
    main()