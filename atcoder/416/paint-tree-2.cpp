#include <bits/stdc++.h>
using namespace std;

// TLE I HATE U

using ll = long long;

const int MAXN = 200005;
vector<int> tree[MAXN];
ll A[MAXN];

int N, K;
const int MAX_PATHS = 1000;
const int MAX_DEPTH = 20;

struct Path {
  ll sum;
  vector<int> nodes;
  Path() : sum(0), nodes() {}
  Path(ll s, vector<int> n) : sum(s), nodes(move(n)) {}

  bool operator<(const Path &other) const { return sum > other.sum; }
};

vector<Path> all_paths;

void dfs_path(int u, int parent, int depth, ll sum, vector<int> &path) {
  if (depth > MAX_DEPTH)
    return;
  all_paths.emplace_back(sum, path);

  for (int v : tree[u]) {
    if (v != parent) {
      path.push_back(v);
      dfs_path(v, u, depth + 1, sum + A[v], path);
      path.pop_back();
    }
  }
}

void collect_all_paths() {
  for (int i = 1; i <= N; ++i) {
    vector<int> path = {i};
    dfs_path(i, -1, 0, A[i], path);
  }

  sort(all_paths.begin(), all_paths.end());
  if ((int)all_paths.size() > MAX_PATHS)
    all_paths.resize(MAX_PATHS);
}

ll find_max_sum() {
  ll max_sum = 0;
  int total = all_paths.size();

  vector<int> used(N + 1, 0);

  function<void(int, int, ll)> dfs = [&](int idx, int count, ll current_sum) {
    if (count > K)
      return;
    max_sum = max(max_sum, current_sum);
    if (idx >= total)
      return;

    for (int i = idx; i < total; ++i) {
      bool conflict = false;
      for (int v : all_paths[i].nodes) {
        if (used[v]) {
          conflict = true;
          break;
        }
      }
      if (conflict)
        continue;

      for (int v : all_paths[i].nodes)
        used[v] = 1;
      dfs(i + 1, count + 1, current_sum + all_paths[i].sum);
      for (int v : all_paths[i].nodes)
        used[v] = 0;
    }
  };

  dfs(0, 0, 0);
  return max_sum;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> N >> K;
  for (int i = 1; i <= N; ++i)
    cin >> A[i];
  for (int i = 1; i < N; ++i) {
    int u, v;
    cin >> u >> v;
    tree[u].push_back(v);
    tree[v].push_back(u);
  }

  collect_all_paths();
  cout << find_max_sum() << '\n';
  return 0;
}
