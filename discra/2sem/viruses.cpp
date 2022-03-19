#include <iostream>

int main() {
    int n, m, t; std::cin >> n >> m >> t;
    std::pair<int, int> viruses[t];
    
    int y, x;
    for (int i = 0; i < t; i++) {
        std::cin >> y >> x;
        viruses[i] = std::pair<int, int>(y - 1, x - 1);
    }
    
    int farest = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int min = n + m + 1;
            for (int k = 0; k < t; k++) {
                int d = std::abs(i - viruses[k].first) + std::abs(j - viruses[k].second);
                if (d < min) min = d;
            }
            if (min > farest) farest = min;
        }   
    }

    std::cout << farest << std::endl;
    
    return 0;
}