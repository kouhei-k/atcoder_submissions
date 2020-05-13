import "dart:io";
import "dart:math";

main(List<String> args) {
  final int N = int.parse(stdin.readLineSync());
  List<int> A =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();

  int ans = A.reduce(max);
  for (var x in A) {
    int count = 0;
    while (x % 2 == 0) {
      x ~/= 2;
      ++count;
    }
    ans = min(ans, count);
  }
  print(ans);
}
