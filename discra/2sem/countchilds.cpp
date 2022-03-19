#include <iostream>
#include <vector>

int main() {
    int n, m; std::cin >> n; std::cin >> m;
    
    std::vector<int> tunnels(n, 0);

    for (int i = 0; i < m; i++) {
        int a, b; std::cin >> a >> b;
        tunnels[a-1]++;
        tunnels[b-1]++;
    }

    for (int i = 0; i < n; i++) std::cout << tunnels[i] << " ";
    std::cout << std::endl;

    return 0;

}