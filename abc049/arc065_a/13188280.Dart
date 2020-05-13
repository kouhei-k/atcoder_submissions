import 'dart:io';

main(List<String> args) {
  String S = stdin.readLineSync();
  int N = S.length;
  int id = N;
  bool flag = true;
  while (id > 1) {
    S = S.substring(0, id);
    if (S.endsWith("dreamer")) {
      id -= 7;
    } else if (S.endsWith("eraser")) {
      id -= 6;
    } else if (S.endsWith("dream") || S.endsWith("erase")) {
      id -= 5;
    } else {
      flag = false;
      break;
    }
  }
  if (flag) {
    print("YES");
  } else {
    print("NO");
  }
}
