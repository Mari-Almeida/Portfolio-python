A = input("Informe um valor para a variável A:")
B = input("Informe um valor para a variável B:")

if (A>B):
    aux=A;
    A=B;
    B=aux;

print("O Valor da variável A agora é:", A);
print("O Valor da variável B agora é:", B);