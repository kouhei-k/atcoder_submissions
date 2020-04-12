import 'dart:io';

main(List<String> args) {
  var N = int.parse(stdin.readLineSync());
  var S1 = (1 + N) * N ~/ 2;
  var S2 = 0;
  var S3 = 0;
  var S4 = 0;

  if (N >= 3) {
    S2 = (3 + (N ~/ 3) * 3) * (N ~/ 3) ~/ 2;
    if (N >= 5) {
      S3 = (5 + (N ~/ 5) * 5) * (N ~/ 5) ~/ 2;
    }
    if (N >= 5) {
      S4 = (15 + (N ~/ 15) * 15) * (N ~/ 15) ~/ 2;
    }
  }
  print(S1 + S4 - S2 - S3);
}
