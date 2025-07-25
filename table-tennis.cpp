#include <deque>
#include <iostream>

using namespace std;

int main() {
  int n;
  long long k;
  cin >> n >> k;

  deque<int> players;

  for (int i = 0; i < n; i++) {
    int power;
    cin >> power;
    players.push_back(power);
  }

  int current = players.front();
  players.pop_front();
  long long wins = 0;

  while (true) {
    int next = players.front();
    players.pop_front();

    if (current > next) {
      wins += 1;
      players.push_back(next);
    } else {
      players.push_back(current);
      current = next;
      wins = 1;
    }

    if (wins >= k || wins == n) {
      cout << current << endl;
      return 0;
    }
  }
}
