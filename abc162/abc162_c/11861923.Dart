import 'dart:io';

main(List<String> args) {
  var K = int.parse(stdin.readLineSync());
  var ans = 0;
  for (var i = 1; i <= K; i++) {
    for (var j = 1; j <= K; j++) {
      for (var k = 1; k <= K; k++) {
        var tmp = i.gcd(j);
        ans += tmp.gcd(k);
      }
    }
  }
  print(ans);
}
