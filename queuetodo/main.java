public class Solution {
    public static int solution(int start, int length) {
        int xorres = 0, end = length;

        while (end > 0) {
            for (int i = start; i < start + end; i++) {
                xorres ^= i;
            }

            start += length;
            end--;
    }

    return xorres;
    }
}