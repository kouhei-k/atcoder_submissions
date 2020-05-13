import "dart:io";

main(List<String> args) {
  List<int> s = stdin.readLineSync().split("").map((x) => int.parse(x)).toList();
  int ans = s.reduce((a, b) => a + b);
  print(ans);
}
