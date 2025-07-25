#include <iostream>
#include <string>

using namespace std;

int main() {
  int r, g, b;
  string c;

  cin >> r >> g >> b >> c;

  int cost;
  if (c == "Red") {
    cost = min(g, b);
  } else if (c == "Green") {
    cost = min(r, b);
  } else if (c == "Blue") {
    cost = min(r, g);
  }

  cout << cost << endl;
}
