package d3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;

class problem7087 {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		String[] data =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
			
		ArrayList<String> alpha = new ArrayList<>(Arrays.asList(data));
		
		for (int t = 1; t<T+1; t++) {
			int n = sc.nextInt();
			int cnt = 0;
			int idx = 0;
			
			ArrayList<String> wordList = new ArrayList<>();
			
			for (int i = 0; i<n; i++) {
				String word = sc.next();
				wordList.add(word);
			}
			
			Collections.sort(wordList);
			for (int i = 0; i<n; i++) {
				char wordChar = wordList.get(i).charAt(0);
				char alphaChar = alpha.get(idx).charAt(0);
				if (wordChar == alphaChar) {
					cnt += 1;
					idx += 1;
					if (idx == 26) {
						idx = 0;
					}
				}
			}
			
			System.out.println(wordList);
			
			System.out.printf("#%d %d", t , cnt);
			System.out.println();
		}
		
	}
}
