
opcao = -1


while opcao != 0:
  opcao = int(input("[1] SACAR \n [2] extrato \n [0] sair \n"))

  if opcao == 1 :
    print("SACANDO..." )
  elif opcao == 2:
    print("EXIBINDO EXTRATO..." )
else:
  print("OBRIGADO POR USAR O BANCO")