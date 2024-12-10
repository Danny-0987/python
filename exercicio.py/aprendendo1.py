faturamento = 1200 # tipo: int -> numero inteiro 
custo = 750.0 # tipo: float -> numero com casa decimal

novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print('faturamento foi de', faturamento)
print('o custo foi de', custo)
print('o lucro foi de', lucro)
print('a margem de lucro foi de', round(margem_lucro, 2))

print(10 % 3)
tempo_contrato = 170
tempo_anos = 170 / 12
print('tempo em anos', int(tempo_anos))
tempo_meses = 170 % 12
print('tempo em meses', tempo_meses)
