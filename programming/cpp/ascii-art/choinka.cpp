// 4
//    Q
//   QQQ
//  QQQQQ
// QQQQQQQ
//    M

// 3
//    Q
//   QQQ
//  QQQQQ
//    M

#include <string>
#include <iostream>

using namespace std;

void tree(int size) {
   int i = 0;

   for(int s = size - 1; s >= 0; s--) {
      cout << string(s, ' ') << string(i * 2 + 1, 'Q') << endl;
      i++;
   } 

   cout << string(size - 1, ' ') << 'M' << endl;
}

int main() {
   int size;
   cin >> size; 

   tree(size);
}
