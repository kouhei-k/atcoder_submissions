import 'dart:io';

main(List<String> args) {
  var N = int.parse(stdin.readLineSync());
  String S = stdin.readLineSync();

  var t = new Map();
  t['R'] = new Set();
  t['G'] = new Set();
  t['B'] = new Set();
  for (var i = 0; i < N; i++) {
    t[S[i]].add(i);
  }
  var ans = 0;
  var L = t["B"].length;
  for (var x in t['R']) {
    for (var y in t['G']) {
      ans += L;
      if (t["B"].contains(2 * y - x)) {
        ans -= 1;
      }
      if (t["B"].contains(2 * x - y)) {
        ans -= 1;
      }
      if ((x + y) % 2 == 0 && t["B"].contains((x + y) ~/ 2)) {
        ans -= 1;
      }
    }
  }
  print(ans);
}
