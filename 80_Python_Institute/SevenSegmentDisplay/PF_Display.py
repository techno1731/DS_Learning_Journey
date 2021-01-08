""" A pure python implementation of the classical 7-segment display, widely used in older electronics """


def get_number():
    numero = str(input("Please enter any integer number: "))
    return numero

def transform_number(numero):
    numero_segmentado = []
    numero_segmentado_seven = []
    dict_conversor = {"0":"###\n# #\n# #\n# #\n###",\
                      "1":"  #\n  #\n  #\n  #\n  #",\
                      "2":"###\n  #\n###\n#  \n###",\
                      "3":"###\n  #\n###\n  #\n###",\
                      "4":"# #\n# #\n###\n  #\n  #",\
                      "5":"###\n#  \n###\n  #\n###",\
                      "6":"###\n#  \n###\n# #\n###",\
                      "7":"###\n  #\n  #\n  #\n  #",\
                      "8":"###\n# #\n###\n# #\n###",\
                      "9":"###\n# #\n###\n  #\n###"}
    for digit in numero:
        numero_segmentado.append(dict_conversor[digit])
    for i in range(len(numero)):
        numero_segmentado_seven.append(numero_segmentado[i].split("\n"))
    #print(numero_segmentado_seven)
    return numero_segmentado_seven

def print_numbers(numero_segmentado_seven):
    for fila in range(5):
        for i, val in enumerate(numero_segmentado_seven):
            if i+1 == len(numero_segmentado_seven):
                print(val[fila], end="\n")
            else:
                print(val[fila], end=" ")
    return None

def main():
    numero = get_number()
    numero_segmentado_seven = transform_number(numero)
    print_numbers(numero_segmentado_seven)
    return None

if __name__ == "__main__":
    main()