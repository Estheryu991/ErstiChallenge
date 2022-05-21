public class Sugar_Cane_Agriculture {
    static int crop_production(int w, int h) {
        return w+h;
      // w is the grid width and h is the grid height
      // w ist die Gitterbreite und h ist die Gitterhöhe
   }
 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int w;
        w = in.nextInt();
        int h;
        h = in.nextInt();
        int sum;
        sum = crop_production(w, h);
        System.out.println(sum);
        in.close();
   // Rückgabesumme der beiden obigen Ganzzahlen
   }
}
