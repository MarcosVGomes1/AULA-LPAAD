#temp = float(input("digite sua temperatura: "))

#if temp > 30:
    #print("vá se hidratar")

#numero = int(input("digite um número inteiro: "))

#if numero % 2 == 0:
    #print("numero par")
#else:
    #print("numero impar")

#saldo_disponivel = int(input("digite o valor da do saldo disponivel: "))
#valor_transacao = int(input("digite o valor da transação: "))
#saldo_suficiente = saldo_disponivel >= valor_transacao

#if saldo_suficiente:
    #print("transação autorizada")
#else:
    #print("transação negada")

#producao = [120,135,128,142,150]

#producao.append(int(input("digite o novo valor: ")))
#producao.append(int(input("digite o novo valor: ")))
#producao.append(int(input("digite o novo valor: ")))
#producao.append(int(input("digite o novo valor: ")))

#quantidade = len(producao)

#print(quantidade)
#print(producao)

#problema 1
faturamento = (18500, 21300, 17800, 24600, 27400)

dias = len(faturamento)
print("dias analisados: ", dias)

total = sum(faturamento)
print("total de faturamentos: ", total)

medio = total / len(faturamento)
print("media diaria: ", medio)

#maximo = max(faturamento)
print("valor maximo: ", maximo)

#minimo = min(faturamento)
print("valor minimo: ", minimo)

if medio >= 22000:
    print("bom desempenho")
elif medio < 22000 and medio >= 19000:
    print("desempenho regular")
else:
    print("desempenho critico")


#problema 2
#velocidade = int(input("digite a velocidade do veiculo: "))
multa = 0
percentual = 0

if velocidade > 70:
    multa = (velocidade - 70) * 9
    percentual = ((velocidade - 70)*100) / 70
    print(f"voce esta acima da velocidade, multado no valor de {multa} , teve um excesso de {percentual}")
    if percentual > 50:
        print("sua carteira esta suspensa por um ano")
else: 
    print("voce esta dentro do limite")

#problema 3

turnos = [485,510,472,498,455,520]

qtd_turnos= len(turnos)
print("quantidade de turnos: ", qtd_turnos)
total_turnos= sum(turnos)
print("total de produção avalidada, ", total_turnos)
media = total_turnos / qtd_turnos
print("media por turno, ", media)
maximo2 = max(turnos)
print("valor maximo: ", maximo2)
minimo2 = min(turnos)
print("valor minimo: ", minimo2)
if minimo2 < 460:
    print("alerta operacional, há um valor abaixo: ", minimo2)

if media >= 500:
    print("meta atendida")
elif media < 500 and media >= 480:
    print("atenção")
else:
    print("abaixo da meta")





