import 'dart:io';

main(List<String> args) {
  List<int> HWN =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int H = HWN[0];
  int W = HWN[1];
  int N = HWN[2];
  List<int> XY =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int y = XY[0];
  int x = XY[1];

  var S = stdin.readLineSync();
  var T = stdin.readLineSync();

  var l = 1;
  var r = W;
  var u = 1;
  var d = H;

  for (var i = N - 1; i >= 0; i--) {
    if (T[i] == "L" || T[i] == "R") {
      if (T[i] == "L") {
        r += 1;
      } else {
        l -= 1;
      }
      if (r > W) r = W;
      if (l < 1) l = 1;
    } else {
      if (T[i] == "U") {
        d += 1;
      } else {
        u -= 1;
      }
      if (d > H) d = H;
      if (u < 1) u = 1;
    }
    if (S[i] == "L" || S[i] == "R") {
      if (S[i] == "L") {
        l += 1;
      } else {
        r -= 1;
      }
      if (r == 0 || l == W + 1) {
        break;
      }
    } else {
      if (S[i] == "U") {
        u += 1;
      } else {
        d -= 1;
      }
      if (u == H + 1 || d == 0) {
        break;
      }
    }
    //print([l, r, u, d].join(""));
  }

  if (l <= x && x <= r && u <= y && y <= d) {
    print("YES");
  } else {
    print("NO");
  }
}
