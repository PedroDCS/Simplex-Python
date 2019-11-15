
"""
A Matriz-
o vetor de recursos 'b' de A-
c Custos-
Solucao basica factivel inicial(vetores base)-
Indices das variaveis nao basicas
numero de linhas de a-
numero de colunas de a-
Titulo do problema
"""
from itertools import repeat
import numpy
from scipy import linalg
import random


A = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]]# Matrz

b = [100000, 30000, 30000, 25000, 50000, 50000, 50000]
c = [-0.043, -0.037, -0.018, -0.028, -0.015, -0.024, 0, 0, 0, 0, 0, 0]
IndicesBase = [1, 4, 6, 7, 9, 11, 12]
IndicesNaoBase = [2, 3, 5, 8, 10]
m = 7#Linhas de A
n = 12#Colunas de A
Titulo = 'Carteira de Investimento [Corrar et al]'

#A, b, c, IndicesBase, IndicesNaoBase, m, n, Titulo
class simplexA():
    Iteracao = 0
    print("\t\t\tMatriz A")

    for i in range(m):
        print(A[i])
    print("Vetor b")
    print(b)
    print("Vetor Custo")
    print(c)

    # Exibe o titulo do problema
    print('\n-------------------------------------------------------------')
    print('Titulo: ', Titulo)
    print('-------------------------------------------------------------')

    # Laco principal da aplicacao: executa os 5 passos propostos por Bertsimas e Tsiksiklis para realizar
    # uma iteracao completa do método Simplex.
    rodar = 1
    while rodar == 1:

# Passo 1: Calculando SBF inicial
        print('Iteracao # ', Iteracao)
        print('Indices Basicos   :')
        for i in IndicesBase:
            print(' ', i)
        print('\tIndices Não Basicos:')
        for i in IndicesNaoBase:
            print(' ', i)

        # Cria o espaco reservado para a matriz basica B de dimensao m x m
        B = []
        # Copia as colunas que formam a base inicial
        for i in A:
            aux = []
            for j in IndicesBase:
                aux.append(i[j-1])
            B.append(aux)
        print("Matriz B")




        # Calcula a SBF inicial pelo produto da inversa de B com b
        bb = linalg.inv(B)
        BMenosUm = []
        for i in bb:
            aux = []
            for j in i:
                aux.append(float(j))
            BMenosUm.append(aux)
        x = numpy.dot(BMenosUm, b)

        # Exibe a inversa da base (apenas debug)
        print("Base^-1:")
        for i in BMenosUm:
            print(i)
        print("Matriz x:")
        # Exibe a solucao básica factível da iteração corrente, apenas variáveis básicas (apenas debug)
        print('\tSBF # ', Iteracao, ':\n');
        for i in range(m):
            print('\t\tx[', IndicesBase[i], '] = ', x[i])

        # Exibe o valor da funcao objetivo
        Objetivo = 0
        for i in range(m):
            #print(c[IndicesBase[i]-1])
            Objetivo = Objetivo + c[IndicesBase[i]-1] * x[i]
        print('\tObjetivo: ', Objetivo, '\n')


# Passo 2: Calculando os custos reduzidos dos indices nao basicos

        # Para cada indice nao base, calcula o custo reduzido correspondente

        # Vetor de custo basico, i.e., parte de c que está relacionado com as variáveis básicas atuais
        CustoBase = []
        for i in range(m):
            CustoBase.append(c[IndicesBase[i]-1])

        # Exibe vetor de custo basico (apenas debug)
        print('\tCusto Basico')
        for i in range(m):
            print('\t\tc_B[', IndicesBase[i], '] = ', CustoBase[i])

        # Escolhe algum indice nao basico cujo custo reduzido e' negativo. Dentre os negativos, escolhe
        # o 'mais negativo'
        JotaEscolhido  = -1
        CustoEscolhido = 0#verificar se é isso mesmo --- CustoEscolhido <- Inf;

        for j in IndicesNaoBase:
            BB = []
            for i in A:
                BB.append(i[j-1])

            print("BB")
            for i in BB:
                print(i)
            input()
            # Calcula a j-esima direcao factivel pelo produto -B^{-1}A_j, apenas para debug
            #Direcao = -BMenosUm % * % A[, j];


            input()
        """
        IndicesNaoBase = [2, 3, 5, 8, 10]
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        [1, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0]
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
        for(j in IndicesNaoBase)
        {
            # Calcula o custo reduzido
            Custo = c[j] - t(CustoBase) %*% BMenosUm %*% A[,j];
        
            # Guarda um indice de direcao basica factivel com custo reduzido negativo, se houver
            if(Custo < 0)
            {
                # Verifica se a j-ésima direcao básica é a que contem o custo reduzido 'mais negativo'
                if(Custo < CustoEscolhido)
                {
                    # Atualiza candidata a entrar na base
                    JotaEscolhido  <- j;
                    CustoEscolhido <- Custo;
                }
            }

            # Exibe a j-ésima direcao factivel (apenas para debug)
            cat('\tDirecao Factivel', j, ', Custo Reduzido = ', Custo, '\n');
            for(i in 1:m)
            {
                cat('\t\td_B[', IndicesBase[i], '] = ', Direcao[i], '\n');
            }
        }
"""


if __name__ == "__main__":
    simplexA()