import "dart:io";

int a;
int b;
int c;

int dfs(int x, int y, int z) {
  if (x == a && y == b && z == c) return 1;
  int ret = 0;
  if (x != a) ret += dfs(x + 1, y, z);
  if (y != b && x >= y + 1) ret += dfs(x, y + 1, z);
  if (z != c && y >= z + 1) ret += dfs(x, y, z + 1);
  // print([x, y, z, ret].join(" "));
  return (ret);
}

main(List<String> args) {
  List A = stdin.readLineSync().split(" ").map((x) => int.parse(x)).toList();
  a = A[0];
  b = A[1];
  c = A[2];
  // print([a, b, c].join(" "));
  print(dfs(0, 0, 0));
}
