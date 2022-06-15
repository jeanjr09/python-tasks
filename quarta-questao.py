# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
#
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = (sp + rj + mg + es + outros)
print('valor total:', total)
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
poutros = ((outros/total)*100)

print('Porcentagem de SP: {}'.format(psp))
print('Porcentagem de RJ: {}'.format(prj))
print('Porcentagem de MG: {}'.format(pmg))
print('Porcentagem de ES: {}'.format(pes))
print('Porcentagem de Outros: {}'.format(poutros))
print('Porcentagem de OUT {}'.format(pout))