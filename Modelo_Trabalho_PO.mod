var milhoComprado >= 0; # Quantidade em toneladas de milho comprado
var milhoPlantado >= 0; # Quantidade em toneladas de milho produzido

minimize Custo: ((250 * milhoComprado) + (milhoComprado * 100)) + (milhoPlantado * 145.73);

subject to

r5: milhoComprado + milhoPlantado >= 45; # Quantidade mínima de produção do milho

solve;
display Custo, milhoComprado, milhoPlantado;

# 11.25 toneladas por hectare
# Custo por tonelada = 145.73