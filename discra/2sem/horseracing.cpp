#include <iostream>
#include <vector>

int main() {
    int n, k; std::cin >> n >> k;
    std::vector<bool> lost(n, false);
    int lostCount = 0;

    int f = -1, s;
    while (f != 0) {
        std::cin >> f;
        if (f == 0) break;
        std::cin >> s;

        if (!lost[s-1]) {
            lostCount++;
            lost[s-1] = true;
        }
    }


    std::string msg = (!lost[k-1] && lostCount == n - 1) ? "Yes" : "No";
    std::cout << msg << std::endl;
    
    return 0;
}