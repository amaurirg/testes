import subprocess
from time import sleep


def typing_in_terminal(word):
    sleep(0.5)
    print(f'{word} ..... OK')

words = ['Saúde', 'Disposição', 'Motivação', 'Foco', 'Determinação', 'Evolução', 'Amor pelo que faz', 'Café']

subprocess.run(['clear'], shell=True)

sleep(1.6)

print('\nVerificando antes de começar a trabalhar ...\n')

sleep(0.6)

for word in words:
    typing_in_terminal(word)

sleep(0.6)
print('\nÓtimo dia de trabalho pra você!\n\n\n')
