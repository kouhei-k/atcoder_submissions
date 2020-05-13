import "dart:io";

main(List<String> args) {
  List NAB = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NAB[0];
  int A = NAB[1];
  int B = NAB[2];
  int ans = 0;
  for (var i = 1; i <= N; i++) {
    int tmp = i;
    int sum = 0;
    while (tmp > 0) {
      sum += tmp % 10;
      tmp ~/= 10;
    }
    if (sum >= A && sum <= B) ans += i;
  }
  print(ans);
}
