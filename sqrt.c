#include <stdio.h>
#include  <math.h>

float squareroot (float a);

int main(){

  float a,s;

  printf("type in a number \n");
  printf("After each input type enter. \n");
  printf("input a: ");
  scanf("%f",&a);
  printf("the number you typed was %f\n",a);

  s = squareroot(a);
  printf("the aquare root of %f is %f",a,s);

}
float squareroot(float a){

  float s = sqrt(a);
  return s;

}
