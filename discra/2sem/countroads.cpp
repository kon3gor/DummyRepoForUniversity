#include <iostream>

int main() {
    int n; std::cin >> n;
    int c = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int t; std::cin >> t;
            c += t;
        }
    }

    std::cout << c/2 << std::endl;

    return 0;

}