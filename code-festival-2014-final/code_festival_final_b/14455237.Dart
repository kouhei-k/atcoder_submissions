import 'dart:io';

main(List<String> args) {
  var S = stdin.readLineSync().split("").map((x) => int.parse(x));
  var k = 1;
  var ans = 0;
  for (var x in S) {
    ans += k * x;
    k *= -1;
  }
  print(ans);
}
