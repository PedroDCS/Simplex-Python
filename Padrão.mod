
# Modelo AMPL na forma Padrão

var milhoComprado >= 0; # Quantidade em toneladas de milho comprado
var milhoPlantado >= 0; # Quantidade em toneladas de milho produzido
var x >= 0;
var y >= 0;

minimize Custo: (350 * milhoComprado) + (milhoPlantado * 145.73);

subject to

R1: milhoComprado + milhoPlantado -x = 45; # Quantidade mínima de produção do milho

solve;
display Custo, milhoComprado, milhoPlantado, x,  R1;

# 11.25 toneladas por hectare
# Custo por tonelada = 145.73
