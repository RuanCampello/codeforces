#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int quant;
    cin >> quant;

    while (quant--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i)
            cin >> arr[i];

        vector<int> bit_count(32, 0);
        for (int a : arr) {
            for (int i = 0; i < 32; ++i)
                if (a & (1 << i))
                    bit_count[i]++;
        }

        long long max_xor_sum = 0;
        for (int x : arr) {
            long long curr = 0;
            for (int i = 0; i < 32; ++i) {
                int bit = (1 << i);
                if (x & bit) {
                    curr += 1LL * bit * (n - bit_count[i]);
                } else {
                    curr += 1LL * bit * bit_count[i];
                }
            }
            max_xor_sum = max(max_xor_sum, curr);
        }

        cout << max_xor_sum << '\n';
    }

    return 0;
}

