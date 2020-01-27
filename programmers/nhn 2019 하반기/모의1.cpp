#include <iostream>
#include <string>
using namespace std;
string field[101][101];
string field2[101][101];
int N, W;

void turning(int i, int j, string loc, int k) {
	int n = N-k*2;
	if (n==1)
		return;
	string nowName = field[i][j];
	int cycleLen = (n-1) * 4;
	int w = W % cycleLen;
	if (w < 0) {
		w = cycleLen + w;
	}
	if (loc=="UP") {
		w = w + j;
	} else if (loc=="RIGHT") {
		w = w + (n-1) + i;
	} else if (loc=="DOWN") {
		w = w + (n-1)*2 + (n-j+1);
	} else if (loc=="LEFT") {
		w = w + (n-1)*3 + (n-i+1);
	}
	w = w % cycleLen;
	if (w==0)
		w = cycleLen;
	int ii = k+1, jj = k+1, cnt = 0;
	for (int p = 0; p < N-k*2-1; p++) {
		jj += 1;
		cnt += 1;
		if (cnt == w) {
			field2[ii][jj] = nowName;
			return;
		};
	}
	for (int p = 0; p < N-k*2-1; p++) {
		ii += 1;
		cnt += 1;
		if (cnt == w) {
			field2[ii][jj] = nowName;
			return;
		};
	}
	for (int p = 0; p < N-k*2-1; p++) {
		jj -= 1;
		cnt += 1;
		if (cnt == w) {
			field2[ii][jj] = nowName;
			return;
		};
	}
	for (int p = 0; p < N-k*2-1; p++) {
		ii -= 1;
		cnt += 1;
		if (cnt == w) {
			field2[ii][jj] = nowName;
			return;
		};
	}
}

int main() {
	cin >> N >> W;
	W--;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> field[i][j];
		}
	}
	if (N%2 == 1) {
		int c = N%2+1;
		field2[c][c] = field[c][c];
	}
	int k = 0;
	while (k < N/2) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i==1+k && (j>=1+k && j<=N-k-1)) {
					turning(i, j, "UP", k);
				}
				else if (j==N-k && (i>=1+k && i<=N-k-1)) {
					turning(i, j, "RIGHT", k);
				}
				else if (i==N-k && (j>=1+k+1 && j<=N-k)) {
					turning(i, j, "DOWN", k);
				}
				else if (j==1+k && (i>=1+k+1 && i<=N-k)) {
					turning(i, j, "LEFT", k);
				}
			}
		}
		k++;
	}
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (j==N) {
				cout << field2[i][j] << '\n';
			} else {
				cout << field2[i][j] << ' ';
			}
		}
	}
		
	return 0;
}

