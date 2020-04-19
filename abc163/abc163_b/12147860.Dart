import 'dart:io';

main(List<String> args) {
  List NM = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  List<int> A =
      stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  int N = NM[0];
  int M = NM[1];

  int S = A.reduce((a, b) => a + b);

  if (S > N)
    print(-1);
  else
    print(N - S);
}
