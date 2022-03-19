#include <iostream>
#include <vector>

int main() {
    int n; std::cin >> n;
    
    std::vector< std::vector<int> > hills(n);
    std::vector<int> colors(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            bool hasRoad; std::cin >> hasRoad;
            if (hasRoad) {
                hills[i].push_back(j);
            }
        }   
    }

    for (int i = 0; i < n; i++) {
        int color; std::cin >> color;
        colors[i] = color;
    }
    
    int c = 0;
    for (int i = 0; i < n; i++) {
        int iColor = colors[i];
        for (int j = 0; j < hills[i].size(); j++) {
            if ( iColor != colors[hills[i][j]]) c++;
        }
    }

    std::cout << c/2 <<std::endl;
    
    return 0;
}