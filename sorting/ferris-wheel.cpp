#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, x;
  cin >> n >> x;

  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  int light = 0, heavy = n - 1;
  int res = 0;

  while (heavy >= light) {
    if (arr[light] + arr[heavy] <= x) {
      res += 1;
      light += 1;
      heavy -= 1;
    } else {
      res += 1;
      heavy -= 1;
    }
  }

  cout << res << endl;

  return 0;
}
