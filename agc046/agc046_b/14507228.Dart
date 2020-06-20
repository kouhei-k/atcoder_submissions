import 'dart:io';

main(List<String> args) {
  List ABCD = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  var A = ABCD[0];
  var B = ABCD[1];
  var C = ABCD[2];
  var D = ABCD[3];
  var c = C - A;
  var d = D - B;
  List<List<int>> dp =
      List.generate(c + 1, (_) => List.generate(d + 1, (_) => 0));

  var mod = 998244353;
  dp[0][0] = 1;
  var ret;
  for (var i = 0; i < c + 1; i++) {
    for (var j = 0; j < d + 1; j++) {
      if (i == 0 && j == 0) continue;
      ret = 0;
      if (i > 0 && j > 0) {
        if (i == j && i == 1) {
          ret -= (A + i - 1) * (B + j - 1);
        } else {
          ret -= dp[i - 1][j - 1];
          ret *= (A + i - 1) * (B + j - 1);
        }
      }
      if (i > 0) ret += dp[i - 1][j] * (B + j);
      if (j > 0) ret += dp[i][j - 1] * (A + i);
      ret %= mod;
      dp[i][j] = ret;
    }
  }
  print(dp[c][d]);
}
