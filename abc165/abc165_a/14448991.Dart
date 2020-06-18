import 'dart:io';

main(List<String> args) {
  var K = int.parse(stdin.readLineSync());
  List<int> AB =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  if (AB[0] ~/ K < AB[1] ~/ K || AB[0] % K == 0) {
    print("OK");
  } else {
    print("NG");
  }
}
