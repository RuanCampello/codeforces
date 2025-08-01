#include <algorithm>
#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  while (t--) {
    int n, x;
    cin >> n >> x;

    pair<int, pair<int, int>> pairs[n + 1];

    for (int i = 1; i <= n; i++) {
      cin >> pairs[i].first >> pairs[i].second.first >> pairs[i].second.second;
    }

    sort(pairs + 1, pairs + n + 1);
    int cursor = x;

    for (int i = 1; i <= n; i++) {
      if (pairs[i].first > cursor)
        break;

      cursor = max(cursor, pairs[i].second.second);
    }

    cout << cursor << '\n';
  }

  return 0;
}
