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
import numpy
from scipy import linalg

# A = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#      [1, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#      [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]]  # Matrz
#
# b = [100000, 30000, 30000, 25000, 50000, 50000, 50000]
# c = [-0.043, -0.037, -0.018, -0.028, -0.015, -0.024, 0, 0, 0, 0, 0, 0]
# IndicesBase = [1, 4, 6, 7, 9, 11, 12]
# IndicesNaoBase = [2, 3, 5, 8, 10]
# m = 7  # Linhas de A
# n = 12  # Colunas de A
# Titulo = 'Carteira de Investimento [Corrar et al]'

A = [[1, 0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 0, 0],
     [1, 2, 0.5, 0, 0, 0, 1, 0],
     [2.5, 1, 4, 0, 0, 0, 0, 1]]  # Matrz
b = [3000, 2500, 500, 6000, 10000]
c = [50, 90, 120, 65, 92, 140, 0, 0, 0]

IndicesBase = [4, 5, 6, 7, 8]
IndicesNaoBase = [1, 2, 3]

m = 5  # Linhas de A
n = 8  # Colunas de A

Titulo = 'Produzir ou Comprar Motores [Lachtermarcher]'


# A, b, c, IndicesBase, IndicesNaoBase, m, n, Titulo
def simplexA():
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
    while 1:
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
                aux.append(i[j - 1])
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
        print('\tSBF # ', Iteracao, ':\n')
        for i in range(m):
            print('\t\tx[', IndicesBase[i], '] = ', x[i])

        # Exibe o valor da funcao objetivo
        Objetivo = 0
        for i in range(m):
            # print(c[IndicesBase[i]-1])
            Objetivo = Objetivo + c[IndicesBase[i] - 1] * x[i]
        print('\tObjetivo: ', Objetivo, '\n')

        # Passo 2: Calculando os custos reduzidos dos indices nao basicos

        # Para cada indice nao base, calcula o custo reduzido correspondente

        # Vetor de custo basico, i.e., parte de c que está relacionado com as variáveis básicas atuais
        CustoBase = []
        for i in range(m):
            CustoBase.append(c[IndicesBase[i] - 1])

        # Exibe vetor de custo basico (apenas debug)
        print('\tCusto Basico')
        for i in range(m):
            print('\t\tc_B[', IndicesBase[i], '] = ', CustoBase[i])

        # Escolhe algum indice nao basico cujo custo reduzido e' negativo. Dentre os negativos, escolhe
        # o 'mais negativo'
        JotaEscolhido = -1
        CustoEscolhido = numpy.inf
        for j in IndicesNaoBase:
            BB = []
            for i in A:
                BB.append(i[j - 1])
            print("BB")
            for i in BB:
                print(i)

            # Calcula a j-esima direcao factivel pelo produto -B^{-1}A_j, apenas para debug
            MenosBmenosUm = numpy.dot(BMenosUm, -1)
            Direcao = numpy.dot(MenosBmenosUm, BB)
            print("j-esima direcao factivel")
            for i in Direcao:
                print(i)

            # Calcula o custo reduzido
            Custo = c[j - 1] - numpy.dot(numpy.transpose(CustoBase), numpy.dot(BMenosUm, BB))
            print("Custo Reduzido", Custo)

            # Guarda um indice de direcao basica factivel com custo reduzido negativo, se houver
            if Custo < 0:
                # Verifica se a j-ésima direcao básica é a que contem o custo reduzido 'mais negativo'
                if Custo < CustoEscolhido:
                    # Atualiza candidata a entrar na base
                    JotaEscolhido = j
                    CustoEscolhido = Custo

            # Exibe a j-ésima direcao factivel (apenas para debug)
            print('\tDirecao Factivel', j, ', Custo Reduzido = ', Custo)
            for i in range(m):
                print('\t\td_B[', IndicesBase[i], '] = ', Direcao[i])

        # Se nao encontrou nenhum indice com custo reduzido negativo, e' porque chegamos no otimo

        if JotaEscolhido == -1:
            # Exibe solucao ótima (apenas debug)
            ValObjetivo = 0
            for i in range(m):
                ValObjetivo = ValObjetivo + CustoBase[i] * x[i]
            print('\nObjetivo = ', ValObjetivo, '(encontrado na ', Iteracao, 'a. iteracao)')
            Solucao = []
            for i in range(n):
                Solucao.append(0)
            for i in range(m):
                Solucao[IndicesBase[i] - 1] = x[i]

            for i in range(n):
                print('x[', i, '] = ', Solucao[i])

            print('\n\n\n')
            return x
        # Exibe quem entra na base
        print('\tVariavel Entra Base: x[', JotaEscolhido, ']\n')
        ################################################################################################################
        ################################################################################################################
        ################################################################################################################
        ################################################################################################################
        ################################################################################################################

        #
        # Passo 3: Computa vetor u
        #
        # Não chegamos em uma solucao ótima ainda. Alguma variável básica deve sair da base para dar
        # lugar a entrada de uma variável não básica. Computa 'u' para verificar se solucao é ilimitada
        AJotaEscolhido = []
        for i in A:
            AJotaEscolhido.append(i[JotaEscolhido])
        print("J Escolhido:")
        for i in AJotaEscolhido:
            print(i)
        u = numpy.dot(BMenosUm, AJotaEscolhido)

        print("u")
        for i in u:
            print(i)
        # Verifica se nenhum componente de u e' positivo
        ExistePositivo = False
        for i in range(m):
            if u[i] > 0:
                ExistePositivo = True

        # Testa. Se não houver no vetor 'u' (sinal inverso da direcao factivel) nenhum componente
        # positivo, é porque o valor ótimo é - infinito.
        if ExistePositivo == False:
            print('\n\nCusto Otimo = -Infinito')
            rep = [numpy.inf, n]  # verificar depois
            print(rep)
            exit()

        #
        # Passo 4: Determina o valor de Theta
        #

        # Chuta um valor alto para o theta, e vai reduzindo de acordo com a razao x_i / u_i
        Theta = numpy.inf
        IndiceL = -1

        # Varre indices basicos determinando o valor de theta que garante factibilidade
        for i in range(m):
            # Calcula a razao
            if u[i] > 0:
                # Calcula a razao
                Razao = x[i] / u[i]
                # Atualiza a razao, pois encontramos um menor valor de theta
                if Razao < Theta:
                    Theta = Razao
                    IndiceL = IndicesBase[i]

        # Exibe variavel que irá deixar a base (apenas debug)
        print('\tVariavel  Sai  Base: x[', IndiceL, '], Theta = ', Theta, '\n')
        #
        # Passo 5: Atualiza variável básica e não-básica
        #

        # Calcula novo valor da nao-basica, e atualiza base
        for i in range(m):
            # Se encontramos o L-ésimo indica da variável básica que deixará a base, substitui-a
            # pela variável não-básica correspondente à j-ésima direção factível de redução de custo
            if IndicesBase[i] == IndiceL:
                x[i] = Theta
                IndicesBase[i] = JotaEscolhido

        # Para as demais variáveis não básicas, apenas atualiza o índice de quem saiu da base (e
        # entrou no conjunto das não-básicas
        for i in range(n - m):
            if IndicesNaoBase[i] == JotaEscolhido:
                IndicesNaoBase[i] = IndiceL
        # Incrementa o numero da iteracao
        Iteracao = Iteracao + 1

    return x
    input()


if __name__ == "__main__":
    simplexA()
