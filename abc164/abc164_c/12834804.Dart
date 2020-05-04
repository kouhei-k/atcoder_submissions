import 'dart:io';
import 'dart:convert';

main() async {
  int N = int.parse(stdin.readLineSync());
  var lines = stdin.transform(utf8.decoder).transform(LineSplitter());
  var S = []..length = N;
  var d = new Map();
  int counter = 0;
  await for (var line in lines) {
    var tmp = line;
    if (d.containsKey(tmp))
      d[tmp] += 1;
    else
      d[tmp] = 1;
    counter++;
    if (counter == N) break;
  }
  print(d.length);
}
