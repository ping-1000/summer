#include <iostream>
using namespace std;
int main(){

  int i;
  float f;
  double d;
  char c;
  string s;
  bool done;

  i= 65521;
  d = 3.1415926535897932384626;
  f = 2.7182818284590;
  c = 'A';
  s = "This is a string of characters.";
  done = true;
  cout << i << "\n";
  cout << d << "\n";
  cout << f << "\n";
  cout << c << "\n";
  cout << s << "\n";
  cout << done << "\n";
  done = false;
  cout << done << "\n";
  return 0;
}
