#include <iostream>
#include <set>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;

  set<int> distinct;
  for (int i = 0; i < n; ++i) {
    int num;
    cin >> num;
    distinct.insert(num);
  }

  cout << distinct.size() << "\n";
  return 0;
}
