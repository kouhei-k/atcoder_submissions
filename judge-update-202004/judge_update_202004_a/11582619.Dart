import 'dart:io';

main(List<String> args) {
  List<int> SLR =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  if (SLR[0] < SLR[1]) {
    print(SLR[1]);
  } else if (SLR[0] > SLR[2]) {
    print(SLR[2]);
  } else {
    print(SLR[0]);
  }
}
