import 'dart:io';

List dfs(n, m) {
  var ret = [];
  if (n == 1) {
    for (var i = 1; i <= m; i++) {
      ret.add([i]);
    }
  } else {
    for (var i = m; i > 0; i--) {
      //rint(ret);
      for (List<int> arr in dfs(n - 1, i)) {
        List tmp = arr + [i];
        ret.add(tmp);
      }
    }
  }
  //    print(ret);
  return (ret);
}

main(List<String> args) {
  List NMQ = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  var abcd = []..length = NMQ[2];
  for (var i = 0; i < NMQ[2]; i++) {
    abcd[i] = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  }
  var A = dfs(NMQ[0], NMQ[1]);
  var ans = 0;
  for (var arr in A) {
    var score = 0;
    for (var B in abcd) {
      if (arr[B[1] - 1] - arr[B[0] - 1] == B[2]) score += B[3];
    }
    if (score > ans) ans = score;
  }
  print(ans);
}
