public class Cane {
	static String seeds(int x1, int v1, int x2, int v2) {
		if (v1 > v2) {
			int remainder = (x1 - x2) % (v2 - v1);
			if (remainder == 0) {
				return "YES";
			}
		}
		return "NO";
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int x1 = in.nextInt();
		int v1 = in.nextInt();
		int x2 = in.nextInt();
		int v2 = in.nextInt();
		System.out.println(seeds(x1, v1, x2, v2));
		in.close();
	}
}
