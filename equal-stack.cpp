#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int equal_stacks(vector<int> &height_1, vector<int> &height_2,
                 vector<int> &height_3) {
  vector<int> sum_1, sum_2, sum_3;
  int total = 0;

  for (int i = height_1.size() - 1; i >= 0; i--) {
    total += height_1[i];
    sum_1.push_back(total);
  }

  total = 0;
  for (int i = height_2.size() - 1; i >= 0; i--) {
    total += height_2[i];
    sum_2.push_back(total);
  }

  total = 0;
  for (int i = height_3.size() - 1; i >= 0; i--) {
    total += height_3[i];
    sum_3.push_back(total);
  }

  unordered_set<int> set_1(sum_1.begin(), sum_1.end());
  unordered_set<int> set_2(sum_2.begin(), sum_2.end());
  unordered_set<int> set_3(sum_3.begin(), sum_3.end());

  int max = 0;

  for (int h : sum_1) {
    if (set_2.count(h) && set_3.count(h)) {
      if (h > max) {
        max = h;
      }
    }
  }

  return max;
}

int main() {
  int n_1, n_2, n_3;
  cin >> n_1 >> n_2 >> n_3;

  vector<int> h_1(n_1), h_2(n_2), h_3(n_3);

  for (int i = 0; i < n_1; ++i) {
    cin >> h_1[i];
  }
  for (int i = 0; i < n_2; ++i) {
    cin >> h_2[i];
  }
  for (int i = 0; i < n_3; ++i) {
    cin >> h_3[i];
  }

  cout << equal_stacks(h_1, h_2, h_3) << endl;
  return 0;
}
