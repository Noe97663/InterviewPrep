/* Calculate the sum without using addition
 * 
 * Brute force - bruh +
 * Bit Manipulation - XOR a and b for 1's = a
 *                    AND+<< a and b for carry 1's = b
 *                    do the same until carry is zero
 * O(1),O(1) - since we have size limits on the integers
 */

public class getSum {
    public int Calculate(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}