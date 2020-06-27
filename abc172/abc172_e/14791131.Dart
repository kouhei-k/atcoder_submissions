import 'dart:io';

import 'dart:math';

List g1 = [1, 1];
List g2 = [1, 1];
List inverse = [0, 1];
void prev_cmb(N, mod) {
  for (var i = 2; i < N + 1; i++) {
    g1.add((g1.last * i) % mod);
    inverse.add((-inverse[mod % i] * (mod ~/ i)) % mod);
    g2.add((g2.last * inverse.last) % mod);
  }
}

int cmb(int n, int r, mod) {
  if (r < 0 || r > n) return (0);
  r = min(r, n - r);
  var ret = g1[n] * g2[r] % mod;
  ret *= g2[n - r];
  ret %= mod;
  return (ret);
}

void main(List<String> args) {
  List NM = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NM[0];
  int M = NM[1];

  var mod = pow(10, 9) + 7;
  prev_cmb(M, mod);
  int ans = cmb(M, N, mod) * g1[N] % mod;
  var tmp = -1;
  var ans2 = 0;
  var tmp2 = 0;
  //print(g2);
  for (var i = 0; i <= N; i++) {
    tmp *= -1;
    tmp2 = cmb(N, i, mod) * g1[M - i] % mod;
    tmp2 *= g2[M - N];
    ans2 += tmp2 * tmp;

    //print("$i ${cmb(N, i, mod)}, ${(cmb(M - i, N - i, mod) * g1[N - i])}");
    //print(ans2);
    ans2 %= mod;
  }

  print(ans * ans2 % mod);
}
