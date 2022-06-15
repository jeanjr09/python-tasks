# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
#    que calcule e retorne:

# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
import json

with open("dados.json", encoding="utf-8") as faturamento:
    faturamento_diario = json.load(faturamento)

print(max(faturamento_diario, key = lambda item:item.get('faturamento')))
print(min(faturamento_diario, key = lambda item:item.get('faturamento')))

total = 0
for dic in faturamento_diario:
    total += dic['faturamento']

media = total / len(faturamento_diario)

acima_media = 0

for dic in faturamento_diario:  
    if dic['faturamento'] > media:  
        acima_media += 1 


print(f'Número de dias de valores acima da média: {acima_media}')
 

    
