//  @Author ArdaBalkir 02-23

#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct DNA {
    vector<string> genes;
};

DNA createDNA(string str1, string str2) {
    DNA dna;

    int len = min(str1.length(), str2.length());
    len -= len % 4;
    len = min(len, 40);

    for (int i = 0; i < len; i += 4) {
        string gene1 = str1.substr(i, 4);
        string gene2 = str2.substr(i, 4);
        if (gene1 == gene2) {
            dna.genes.push_back(gene1);
        } else {
            dna.genes.push_back("X");  // mark the mismatched genes
        }
    }

    return dna;
}

int main() {
    string input1 = "AGCTTAGCTTAGCTTAGCTTAGCTTAGCTTAGCTTAGCTTAC";
    string input2 = "AGCTTAGCTTAGCTTAGCTTAGCTTAGCTTAGCTTAGCTTGC";
    
    DNA dna = createDNA(input1, input2);

    cout << "DNA: ";
    for (string gene : dna.genes) {
        cout << gene << " ";
    }
    cout << endl;

    return 0;
}
