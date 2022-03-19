#include <iostream>

int main() {
    int n; std::cin >> n;
    long long a; std::cin >> a;
    long long b; std::cin >> b;

    long long f = a;
    long long s = b;

    while (f != s) {
        if (f > s) {
            f = f/2;
        } else {
            s = s/2;
        }
    }

    if (f == a || s == b) {
        std::cout << f/2 << std::endl;
    } else {
        std::cout << f << std::endl;
    }

    return 0;
}