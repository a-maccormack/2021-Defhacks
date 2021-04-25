import java.io.*;
import java.util.*;

class socdist1 {
    public static void main(String[] args) throws IOException{
        
        BufferedReader in = new BufferedReader(new FileReader("socdist1.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("socdist1.out")));
        
        int N = Integer.parseInt( in.readLine() );
        String s = in.readLine();

        int currd = 100000000;
        int top1 = 1;
        int top2 = 1;
        int topAdd2 = 1;
        int gapstart = -1;
        for (int i = 0; i < N; i++) {
          boolean curr = s.charAt(i) == '1';
          if (curr) {
            if (gapstart == -1) {
              top1 = Math.max(top1, i);
              topAdd2 = Math.max(topAdd2, i/2);
              gapstart = i;
            }
            else {
              int j = (i-gapstart)/2;
              if (j >= top1) {
                top2 = top1;
                top1 = j;
              }
              else if (j > top2) {
                top2 = j;
              }
              topAdd2 = Math.max(topAdd2, (i-gapstart)/3);
              currd = Math.min(currd, i-gapstart);
              gapstart = i;
            }
          }
        }
        if (gapstart == -1) {
          topAdd2 = Math.max(topAdd2, N-1);
        }
        else {
          int j = N-gapstart-1;
          if (j >= top1) {
            top2 = top1;
            top1 = j;
          }
          else if (j > top2) {
            top2 = j;
          }
        }
        topAdd2 = Math.max(topAdd2, (N-gapstart-1)/2);
        out.println("" + Math.min(Math.max(Math.min(top1, top2), topAdd2), currd));
        out.close();
    }
}
