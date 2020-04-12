import 'dart:io';

main(List<String> args) {
  var N = int.parse(stdin.readLineSync());

  while (N > 0) {
    if (N % 10 == 7) {
      print("Yes");
      return;
    } else {
      N ~/= 10;
    }
  }
  print("No");
}
