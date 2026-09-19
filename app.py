#Código tem o objetivo de analisar o consumo de água com base nos 
# inputs fornecidos das variáveis tipo_imovel e consumo_mensal

#Entradas
tipo_imovel = input("Digite o seu tipo de imóvel (comercial, casa ou apartamento): ").lower()
consumo_mensal = float(input("Qual o seu consumo mensal de água em m³? "))

#Saídas
match tipo_imovel:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")     
    case "apartamento" if consumo_mensal < 10:
        print("Consumo econômico - excelente controle de água!")     
    case "apartamento" | "casa" if consumo_mensal <= 25:
        print("Consumo moderado - dentro do padrão residencial.")      
    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")