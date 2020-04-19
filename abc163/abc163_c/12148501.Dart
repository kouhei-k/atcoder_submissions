import 'dart:io';
import 'dart:convert';

main(List<String> args) async {
  int N = int.parse(stdin.readLineSync());
  var lines = stdin.transform(utf8.decoder).transform(LineSplitter());
  // List<int> A =
  //     stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  var A = new List();
  await for (var line in lines) {
    A = line.split(" ").map((x) => int.parse(x)).toList();
    break;
  }
  var ans = new List.filled(N, 0);
  for (var x in A) {
    ans[x - 1] += 1;
  }
  for (var x in ans) {
    print(x);
  }
}
