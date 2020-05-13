import 'dart:io';

main(List<String> args) {
  int N = int.parse(stdin.readLineSync());
  Set<int> d = {};

  for (int i = 0; i < N; i++) {
    d.add(int.parse(stdin.readLineSync()));
  }
  print(d.length);
}
