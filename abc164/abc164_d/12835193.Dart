import 'dart:io';
import 'dart:math';

main(List<String> args) {
  List S = stdin.readLineSync().split('').map((x) => int.parse(x)).toList();
  int N = S.length;
  var mods = Map();
  int s = 0;
  mods[0] = 1;
  var D = []..length = N;
  D[0] = 1;
  for (var i = 1; i < N; i++) {
    D[i] = D[i - 1] * 10 % 2019;
  }

  for (var i = N - 1; i >= 0; i--) {
    s += D[N - 1 - i] * S[i];
    s %= 2019;
    if (mods.containsKey(s))
      mods[s] += 1;
    else
      mods[s] = 1;
  }
  int ans = 0;
  mods.forEach((k, v) => ans += (v * (v - 1)) ~/ 2);
  //print(mods);
  print(ans);
}
