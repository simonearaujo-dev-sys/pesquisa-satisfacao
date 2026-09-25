# ======================================================
 # PESQUISA DE SATISFAÇÃO — ATENDIMENTO AO CLIENTE
 # Empresa: TudoWeb
 # Aluna: Simone Araujo
 # ======================================================
 # ---------- DEFINIR QUANTIDADE DE ENTREVISTADOS ----------
 # ↓↓↓ Para TESTE com 10 — use essa linha abaixo ↓↓↓
 # quantidade = 10
 # ↓↓↓ Para VERSÃO FINAL com 50 — use essa linha abaixo ↓↓↓
quantidade = 50
 # ---------- INICIALIZAR CONTADORES ----------
excelente = 0
bom = 0
ruim = 0
 # ---------- LAÇO DE REPETIÇÃO — FOR ----------
for i in range(quantidade):
     print(f"\n--- Entrevistado {i+1} de {quantidade} ---")
     
     # Coletar dados
     nome = input("Digite o nome: ")
     idade = int(input("Digite a idade: "))
     
     opiniao = 0
     
     # ---------- VALIDAÇÃO — WHILE + AND ----------
     while opiniao != 1 and opiniao != 2 and opiniao != 3:
         print("\nEscolha a opinião:")
         print("1 — EXCELENTE")
         print("2 — BOM")
         print("3 — RUIM")
         opiniao = int(input("Digite sua opção (1/2/3): "))
         
         if opiniao not in (1, 2, 3):
             print("❌ Opção INVÁLIDA! Digite apenas 1, 2 ou 3.")
     
     # ---------- CLASSIFICAR RESPOSTA — IF / ELIF / ELSE ----------
     if opiniao == 1:
         excelente = excelente + 1
     elif opiniao == 2:
         bom = bom + 1
     else:
         ruim = ruim + 1
 # ---------- EXIBIR RESULTADOS FINAIS ----------
print("\n" + "="*45)
print("         RESULTADO DA PESQUISA")
print("="*45)
print(f"Total de entrevistados: {quantidade}")
print(f"a) Quantidade EXCELENTE: {excelente}")
print(f"b) Quantidade RUIM:      {ruim}")
print("="*45)