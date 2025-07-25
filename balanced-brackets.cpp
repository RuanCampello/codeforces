#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    string s;
    cin >> s;
    stack<char> st;
    bool is_balanced = true;
    for (char ch : s) {
      if (ch == '(' || ch == '{' || ch == '[') {
        st.push(ch);
      } else {
        if (st.empty()) {
          is_balanced = false;
          break;
        }
        char top = st.top();
        st.pop();
        if ((ch == ')' && top != '(') || (ch == '}' && top != '{') ||
            (ch == ']' && top != '[')) {
          is_balanced = false;
          break;
        }
      }
    }
    if (!st.empty()) {
      is_balanced = false;
    }
    cout << (is_balanced ? "YES" : "NO") << endl;
  }
  return 0;
}
