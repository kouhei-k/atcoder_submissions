import 'dart:io';

main(List<String> args) {
  List NK = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NK[0];
  int K = NK[1];
  int ans = 1;
  int tmp = 1;
  int mod = 1000000007;
  for (var i = 1; i < N + 1; i++) {
    tmp = tmp - (i - 1) + N - (i - 1);
    if (i >= K) {
      ans += tmp;
      ans %= mod;
    }
  }
  print(ans);
}
