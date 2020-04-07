import 'dart:convert';
import 'dart:io';

main() async {
  List NQ = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NQ[0];
  int Q = NQ[1];
  var lines = stdin.transform(utf8.decoder).transform(LineSplitter());
  int count = 0;
  List gcds = [];
  bool flag = true;
  List A;
  List S;
  await for (var line in lines) {
    if (flag) {
      A = line.split(" ").map((x) => int.parse(x)).toList();
      flag = false;
    } else {
      S = line.split(" ").map((x) => int.parse(x)).toList();
      break;
    }
  }
  int tmp = A[0];
  gcds.add(tmp);
  for (var i = 1; i < NQ[0]; i++) {
    tmp = tmp.gcd(A[i]);
    gcds.add(tmp);
  }
  for (var s in S) {
    if (s.gcd(gcds.last) != 1) {
      print(s.gcd(gcds.last));
    } else {
      int l = -1;
      int r = NQ[0];
      while (l + 1 < r) {
        int mid = (l + r) ~/ 2;
        if (s.gcd(gcds[mid]) == 1) {
          r = mid;
        } else {
          l = mid;
        }
      }
      print(r + 1);
    }
  }
}
