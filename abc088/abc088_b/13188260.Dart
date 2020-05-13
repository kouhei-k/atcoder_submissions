import 'dart:io';

main(List<String> args) {
  int N = int.parse(stdin.readLineSync());
  List<int> a =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();

  a.sort((x, y) => y - x);
  int Alice = 0;
  int Bob = 0;
  for (var i = 0; i < N; i++) {
    if (i % 2 == 0) {
      Alice += a[i];
    } else {
      Bob += a[i];
    }
  }
  print(Alice - Bob);
}
