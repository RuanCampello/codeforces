#include <iostream>

using namespace std;

int main() {
  string input;

  cin >> input;

  int a = input[0] - '0';
  int b = input[2] - '0';
  char op = input[1];

  if (op == '+') {
    cout << a + b << endl;
  } else {
    cout << a - b << endl;
  }
}
