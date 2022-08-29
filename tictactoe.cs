using System;

namespace Project_1 {
    class MainClass {
        int [] playingfield = new int[3][3];

        public void initField() {
          foreach(int i in playingfield) {
            foreach(int j in playingfield[i]) {
              this.playingfield[i][j] = 0;
            }
          }
        }

        public static void Main (string[] args) {
            initField();
            Console.ReadKey ();
        }

        public bool CheckWinnings(int [] board) {

        }

        public void minimax(int [] board, int depth, bool MaxinPlayer) {

        }
    }
}
