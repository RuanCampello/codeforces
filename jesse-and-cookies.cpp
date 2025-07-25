#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int cookies(int k, vector<int> arr) {
  priority_queue<int, vector<int>, greater<int>> heap;

  for (int num : arr) {
    heap.push(num);
  }

  int op = 0;

  while (heap.top() < k && heap.size() >= 2) {
    int l = heap.top();
    heap.pop();
    int l2 = heap.top();
    heap.pop();

    int cookies = l + 2 * l2;
    heap.push(cookies);
    op += 1;
  }

  return (heap.top() >= k) ? op : -1;
}

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> arr(n);

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cout << cookies(k, arr) << endl;

  return 0;
}
