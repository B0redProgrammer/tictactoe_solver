using System;

namespace Project_1 {
    class MainClass {
        static int[,] playingfield = new int[3, 3];

        public static void initField() {
          for(int i = 0; i<playingfield.GetLength(0); i++) {
            for(int j = 0; j<playingfield.GetLength(1); j++) {
              playingfield[i, j] = 0;
            }
          }
        }

        public static void Main (string[] args) {
            initField();
            Console.ReadKey();
        }

        public static bool CheckWinnings(int [] board) {

        }


        public static void minimax(int [] board, int depth, bool MaxinPlayer) {

        }
    }
}
