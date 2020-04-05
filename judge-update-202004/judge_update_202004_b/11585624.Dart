import 'dart:io';

main(List<String> args) {
  int N = int.parse(stdin.readLineSync());
  List R = [];
  List B = [];
  List XC;
  for (var i = 0; i < N; i++) {
    XC = stdin.readLineSync().split(" ");
    int x = int.parse(XC[0]);
    if (XC[1] == "R") {
      R.add(x);
    } else {
      B.add(x);
    }
  }
  R.sort();
  B.sort();
  for (var x in R) {
    print(x);
  }
  for (var x in B) {
    print(x);
  }
}
