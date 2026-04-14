cp1 = float(input('Digite a nota do seu Checkpoint 1 (0 a 10): '))
cp2 = float(input('Digite a nota do seu Checkpoint 2 (0 a 10): '))
cp3 = float(input('Digite a nota do seu Checkpoint 3 (0 a 10): '))
sp1 = float(input('Digite a nota do seu Sprint 1 (0 a 10): '))
sp2 = float(input('DIgite a nota do seu Sprint 2 (0 a 10): '))
gs = float(input('Digite a nota da sua Global Solution (0 a 10): '))
menor = ()
if cp1 < cp2:
    menor = cp1
elif cp2 < cp1 and cp2 < cp3:
    menor = cp2
elif cp3 < cp1 and cp3 < cp2:
    menor = cp3
elif cp1 == cp2 and cp2 ==cp3:
    menor = cp1
else:
    menor = cp1
mediasemestre = ((cp1 + cp2 + cp3 - menor + sp1 + sp2)/4) * 0.4 + (gs * 0.6)
mediapeso = mediasemestre * 0.4
print(f'A media do semestre foi {mediasemestre:.2f} 0 a 10')
print(f'A media do semestre com peso foi {mediapeso:.2f} 0 a 4')
