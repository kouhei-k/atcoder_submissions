import 'dart:io';

main(List<String> args) {
  List NY = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NY[0];
  int Y = NY[1];
  int k = 0;
  bool flag = false;
  for (var i = 0; i <= N; i++) {
    for (var j = 0; j <= N - i; j++) {
      k = N - i - j;
      if (i * 10000 + j * 5000 + k * 1000 == Y) {
        print([i, j, k].join(" "));
        flag = true;
        break;
      }
    }
    if (flag) break;
  }
  if (!flag) print("-1 -1 -1");
}
