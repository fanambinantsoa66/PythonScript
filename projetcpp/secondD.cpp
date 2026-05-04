#include<iostream>
#include<math.h>
using namespace std;
int main(void)
{
 float secondD(float a, float b, float c)

  { 
     float x,x1,x2,delta;
     do
     {
     std::cout<<"Enter a"<<std::endl;
     std::cin>>a;
     }
     while(a=0);
 
  std::cout<<"Enter b"<<std::endl;
  std::cin>>b;
  std::cout<<"Enter c"<<std::endl;
  std::cin>>c;
  delta=b*b-4*a*c;
  if(delta==0)
  
  x=-b/(2*a);
  std::cout<<"racine double x="<<x<<std::endl;
  
  if(delta>0)
  
  x1=-b-sqrt(delta)/2*a;
  x2=-b+sqrt(delta)/2*a;
  std::cout<<"valeur de x1 :"<<x1<<std::endl;
  std::cout<<"valeur de x2 :"<<x2<<std::endl;
  
  else
  std::cout<<"pas de soluion "<<std::endl;
  }
}

