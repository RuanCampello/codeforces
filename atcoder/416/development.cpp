#include <algorithm>
#include <iostream>
#include <vector>

// couldn't make it not get TLE BLOODY HELL

using namespace std;

const int MAXN = 505;
const long long INF = 1e18;

int N;
long long T;
long long D[MAXN][MAXN];
bool has_airport[MAXN];
bool dist_dirty = true;

void floyd_warshall() {
  for (int k = 1; k <= N; k++)
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= N; j++)
        if (D[i][k] < INF && D[k][j] < INF)
          D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

  dist_dirty = false;
}

long long total_sum() {
  if (dist_dirty)
    floyd_warshall();

  vector<long long> minTo(N + 1, INF), minFrom(N + 1, INF);

  for (int i = 1; i <= N; i++) {
    for (int a = 1; a <= N; a++) {
      if (!has_airport[a])
        continue;
      if (D[i][a] < INF)
        minTo[i] = min(minTo[i], D[i][a]);
      if (D[a][i] < INF)
        minFrom[i] = min(minFrom[i], D[a][i]);
    }
  }

  long long sum = 0;

  for (int x = 1; x <= N; x++) {
    for (int y = 1; y <= N; y++) {
      if (x == y)
        continue;

      long long best = D[x][y];
      if (minTo[x] < INF && minFrom[y] < INF)
        best = min(best, minTo[x] + T + minFrom[y]);

      if (best < INF)
        sum += best;
    }
  }

  return sum;
}

int main() {
  int M, K, Q;
  cin >> N >> M;

  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      D[i][j] = (i == j ? 0 : INF);

  for (int i = 0; i < M; i++) {
    int u, v;
    long long c;
    cin >> u >> v >> c;
    D[u][v] = min(D[u][v], c);
    D[v][u] = min(D[v][u], c);
  }

  cin >> K >> T;
  for (int i = 0; i < K; i++) {
    int x;
    cin >> x;
    has_airport[x] = true;
  }

  cin >> Q;
  while (Q--) {
    int type;
    cin >> type;
    if (type == 1) {
      int u, v;
      long long c;
      cin >> u >> v >> c;
      if (c < D[u][v]) {
        D[u][v] = c;
        D[v][u] = c;
        dist_dirty = true;
      }
    } else if (type == 2) {
      int x;
      cin >> x;
      has_airport[x] = true;
    } else {
      cout << total_sum() << endl;
    }
  }

  return 0;
}
