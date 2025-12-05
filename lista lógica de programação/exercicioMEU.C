#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    float x;
    float y;
} ponto;

float pto_distancia(ponto *p1, ponto *p2) {
    float dx = p1 -> x - p2 -> x;
    float dy = p1 -> y - p2 -> y;
    return sqrt(dx * dx + dy * dy); }

int main() { ponto a, b;
    printf("Digite o x e y do primeiro ponto:");
    scanf("%f %f" , &a.x , &a.y);

    printf("Digite o x e y do segundo ponto:")
    scanf("%f %f" , &a.x , &a.y);
    
    float distancia = pto_distancia(&a , &b);
    printf("Distância entre dois pontos = %.2f\n", distancia);
    return 0;
