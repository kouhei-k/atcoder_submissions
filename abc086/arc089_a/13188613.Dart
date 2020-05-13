import 'dart:convert';
import 'dart:io';
import 'dart:async';

main() async {
  var N = int.parse(stdin.readLineSync());
  var lines = stdin.transform(utf8.decoder).transform(LineSplitter());

  List<int> txy = [];
  bool flag = true;
  int count = 1;
  List<int> prev = [0, 0, 0];
  int diff = 0;
  int dis = 0;
  await for (var line in lines) {
    txy = line.split(" ").map((x) => int.parse(x)).toList();
    diff = (txy[0] - prev[0]);
    dis = ((txy[1] - prev[1]).abs() + (txy[2] - prev[2]).abs());
    if (diff >= dis && diff % 2 == dis % 2) {
      count++;
      prev[0] = txy[0];
      prev[1] = txy[1];
      prev[2] = txy[2];
      if (count > N) break;
    } else {
      flag = false;
      break;
    }
  }
  if (flag) {
    print("Yes");
  } else {
    print("No");
  }
}
