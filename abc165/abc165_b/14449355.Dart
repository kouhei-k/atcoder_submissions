import 'dart:io';

main(List<String> args) {
  var X = int.parse(stdin.readLineSync());
  var a = 100;
  var count = 0;
  while (a < X) {
    count++;
    a += a ~/ 100;
  }
  print(count);
}
