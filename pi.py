## ══════════════════════════════════════════════════════════
## ══ Programa para calculo de PI para fins de valor venal ══
## ══════════════════════════════════════════════════════════

# Modulo para limpar a tela do sistema.
import os
os.system("cls")

# definição de variaveis
prenotacao = float(input("Digite o valor da prenotação (R$): "))
custas = float(input("Digite o valor das custas (R$): "))

valorvenal = float(input("Digite o valor venal total do imóvel (R$):"))
areaterreno = float(input("Digite a área do terreno (m²): "))    
venalterreno = float(input("Digiteo valor venal territorial(m²): "))
areaideal = float(input("Digite a área ideal do imóvel (m²): "))
fracaoideal = float(input("Digite a fração ideal do imóvel (%): "))
valorapartamento = venalterreno / areaterreno * areaideal * (fracaoideal / 100)
valorapartamento_pi = valorvenal - valorapartamento
print(f"O valor de PI para o imóvel é de R$:{valorapartamento_pi:.2f}")
print(f"O valor venal do imóvel é de R$:{valorapartamento:.2f}")
# processamento das custas
complemento = custas - prenotacao
print(f"O depósito complementar é de R$:{complemento:.2f}")