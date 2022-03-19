#include <iostream>
#include <vector>

int main() {
    int n; std::cin >> n;
    
    std::vector< std::vector<int> > roads(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int l; std::cin >> l;
            roads[i][j] = l;
        }   
    }
    int best = 3000;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int a = roads[i][j];
            for (int k = j + 1; k < n; k++) {
                int b = roads[i][k];
                int r = a + b + roads[j][k];
                if (best > r) best = r;
            }
        }   
    }

    std::cout << best << std::endl;
    
    return 0;
}