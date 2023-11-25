nome = "Trevor"
xp = 6543
nivel = ""

if xp < 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Imortal"
elif xp >= 10001:
    nivel = "Radiante"

print("O Herói de nome " + nome + " está no nível de " + nivel)