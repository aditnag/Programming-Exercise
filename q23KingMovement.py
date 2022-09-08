# cook your dish here
class KingMovement:
    def numOfMoves(self):
        t = int(input())
        while t:
            r, c, k = map(int, input().strip().split())
            moves = 0
            if 1 <= r <= 8 and 1 <= c <= 8:
                for i in range(1, 9):
                    for j in range(1, 9):
                        if max(abs(i-r), abs(j-c)) <= k:
                            moves += 1
            print(moves)
            t -= 1


o = KingMovement()
o.numOfMoves()

# import java.util.*;
# import java.lang.*;
# import java.io.*;
#
# /* Name of the class has to be "Main" only if the class is public. */
# class Pair
# {
#     int x,y;
#     Pair(int a,int b)
#     {
#         x=a;
#         y=b;
# 	}
# }
# public class Main
# {
#     public static void main (String[] args) throws java.lang.Exception
#     {
#         Scanner sc = new Scanner(System.in);
#         int t = sc.nextInt();
#     	Pair nxt[] = new Pair[8];
#         nxt[0] = new Pair(1,1);
#         nxt[1] = new Pair(1,-1);
#         nxt[2] = new Pair(-1,1);
#         nxt[3] = new Pair(-1,-1);
#         nxt[4] = new Pair(0,1);
#         nxt[5] = new Pair(0,-1);
#         nxt[6] = new Pair(1,0);
#         nxt[7] = new Pair(-1,0);
#         while(t-->0)
#         {
#             int r = sc.nextInt()-1;
#             int c = sc.nextInt()-1;
#             int k = sc.nextInt();
#             boolean [][] dp = new boolean[8][8];
#             dp[r][c]=true;
#             while(k-->0)
#             {
#                 boolean [][] tmp = new boolean[8][8];
#             	for(int i=0;i<8;i++)
#                 {
#                     for(int j=0;j<8;j++)
#                     {
#                         if(dp[i][j])
#                         {
#                             tmp[i][j] = true;
#                             for(Pair nPos : nxt)
#                             {
#                                 int ni = i + nPos.x;
#                                 int nj = j + nPos.y;
#                                 if(ni>=0 && ni<8 && nj>=0 && nj<8)
#                                     tmp[ni][nj]= true;
#                             }
#                         }
#                     }
#                 }
#                 dp = tmp;
#         	}
#             int ans = 0;
#             for(int i=0;i<8;i++)
#             {
#                 for(int j=0;j<8;j++)
#                 {
#                     if(dp[i][j])
#                         ans++;
#                 }
#             }
#             System.out.println(ans);
#         }
#     }
# }
