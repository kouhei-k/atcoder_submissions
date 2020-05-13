import "dart:io";


main(List<String> args) {
  int A = int.parse(stdin.readLineSync());
  int B = int.parse(stdin.readLineSync());
  int C = int.parse(stdin.readLineSync());
  int X = int.parse(stdin.readLineSync());
  int ans = 0;
  for (var i = 0; i <= A; i++) {
    for (var j = 0; j <= B; j++) {
      for (var k = 0; k <= C; k++) {
        if (X == 500 * i + 100 * j + 50 * k) ans++;
      }
    }
  }
  print(ans);
}
