import numpy as np

def save_to_file(conteudo, nome):
    arquivo_new = open(nome,"w")
    arquivo_new.writelines(conteudo)
    arquivo_new.close()

DIRETORIO = 'grafico/saturacao/db'

l200 = np.load('{0}/L200.npy'.format(DIRETORIO));
l400 = np.load('{0}/L400.npy'.format(DIRETORIO));
l800 = np.load('{0}/L800.npy'.format(DIRETORIO));
l1600 = np.load('{0}/L1600.npy'.format(DIRETORIO));

arquivo200 = ['tempo (t);rugosidade (w)']
for t in range(len(l200)):
    arquivo200.append('\n{0};{1}'.format(t,l200[t]))
save_to_file(arquivo200,'{0}/L200.txt'.format(DIRETORIO))

arquivo400 = ['tempo (t);rugosidade (w)']
for t in range(len(l400)):
    arquivo400.append('\n{0};{1}'.format(t,l400[t]))
save_to_file(arquivo400,'{0}/L400.txt'.format(DIRETORIO))

arquivo800 = ['tempo (t);rugosidade (w)']
for t in range(len(l800)):
    arquivo800.append('\n{0};{1}'.format(t,l800[t]))
save_to_file(arquivo800,'{0}/L800.txt'.format(DIRETORIO))


arquivo1600 = ['tempo (t);rugosidade (w)']
for t in range(len(l1600)):
    arquivo1600.append('\n{0};{1}'.format(t,l1600[t]))
save_to_file(arquivo1600,'{0}/L1600.txt'.format(DIRETORIO))

print('Concluído...')
