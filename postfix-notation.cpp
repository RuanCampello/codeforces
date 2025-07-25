#include <cmath>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

int main() {
  string input;
  getline(cin, input);

  stack<double> st;
  stringstream ss(input);
  string token;

  while (ss >> token) {
    if (token == "+" || token == "-" || token == "*" || token == "/" ||
        token == "%" || token == "^") {
      double b = st.top();
      st.pop();

      double a = st.top();
      st.pop();

      double result;

      if (token == "+") {
        result = a + b;
      } else if (token == "-") {
        result = a - b;
      } else if (token == "*") {
        result = a * b;
      } else if (token == "/") {
        result = a / b;
      } else if (token == "%") {
        result = fmod(a, b);
      } else if (token == "^") {
        result = pow(a, b);
      }

      st.push(result);
    } else {
      st.push(stod(token));
    }
  }

  cout << fixed << setprecision(1) << st.top() << endl;

  return 0;
}
