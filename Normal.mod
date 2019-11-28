
# Modelo AMPL na forma Normal

var milhoComprado >= 0; # Quantidade em toneladas de milho comprado
var milhoPlantado >= 0; # Quantidade em toneladas de milho produzido

minimize Custo: (350 * milhoComprado) + (milhoPlantado * 145.73);

#subject to

R1: milhoComprado + milhoPlantado >= 45; # Quantidade mínima de produção do milho

solve;
display Custo, milhoComprado, milhoPlantado, R1;

# 11.25 toneladas por hectare
# Custo por tonelada = 145.73