import 'dart:io';

main(List<String> args) {
  int X = int.parse(stdin.readLineSync());
  print(360 ~/ 360.gcd(X));
}
