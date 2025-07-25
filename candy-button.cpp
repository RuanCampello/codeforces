#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, c;

  cin >> n >> c;

  vector<int> t(n);
  for (int i = 0; i < n; i++) {
    cin >> t[i];
  }

  int candies = 0;
  int last_candy = -c - 1;

  for (int i = 0; i < n; i++) {
    if (t[i] - last_candy >= c) {
      candies += 1;
      last_candy = t[i];
    }
  }

  cout << candies << endl;
  return 0;
}
