#include <iostream>

using namespace std;

int binary_search(int arr[], int left, int right, int needle) {
  int res = -1;
  while (left <= right) {
    int middle = right + (left - right) / 2;

    if (arr[middle] >= needle) {
      res = middle + 1;
      right = middle - 1;
    } else
      left = middle + 1;
  }

  return res;
}

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, q;
  cin >> n >> q;
  int arr[n];
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  for (int i = 0; i < q; i++) {
    int needle;
    cin >> needle;

    cout << binary_search(arr, 0, n - 1, needle) << endl;
  }

  return 0;
}
