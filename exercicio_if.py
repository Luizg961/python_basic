
opcao = 0

saldo = 2000
print()
print()
print("opcao 1 conta normal")
print("opcao 2 conta universitaria")
print("opcao 3 conta especial")
print()
opcao = int ( input("inform a sua OPCAO de CONTA "  ))



cheque_especial = 450

if opcao == 1:
    saque = float (input("INFORME O VALOR PARA SACAR " ))
    if saldo >= saque:
        
        print("SAQUE REALIZADO COM SUCESSO")
    elif saque <= (saldo + cheque_especial):
        print("SAQUE REALIZADO COM CHEQUE ESPECIAL")
    else:
        print("SALDO INSUFICIENTE")
elif opcao == 2:
    saque = float (input("INFORME O VALOR PARA SACAR " ))
    if saldo >= saque :
        print("SAQUE REALIZADO COM SUCESSO")
    else:
        print("saldo insuficiente ")
elif opcao == 3 :
    saque = float (input("INFORME O VALOR PARA SACAR " ))
    print("conta especial selecionada SAQUE AUTORIZADO " )
else:
  print("OPÇAO NAO EXISTENTE ")